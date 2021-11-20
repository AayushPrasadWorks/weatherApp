import React from 'react';
import { useState } from 'react';
import ReactDOM from 'react-dom';
import './index.css';



/*
This function show the current weather of an input location

The request is taken in as JSON and parsed for information accordingly

If a city cannot be found, an alert message is given to the user

*/
function getLocWeather(location) {
  const request = {
    // content-type header should not be specified!
    method: 'GET',
    
  };

  //replace url with where the flask server is running
  var url = 'http://127.0.0.1:5000/weather?location='+location
  fetch(url, request)
  .then(response => response.json())
  .then(result => {
    if(result === null){
      alert("Invalid Input");
      return;
    }

     console.log(result);
     const obj = JSON.parse(result);
     
     if(obj.cod !== 200){
       return;
     }

     var cur = document.getElementById("Current")
     document.getElementById("weatherType").src = 'http://openweathermap.org/img/w/'+obj.weather[0].icon+'.png';
     cur.innerHTML = obj.main.temp;
     document.getElementById("weatherDes").innerHTML = obj.weather[0].main;
     document.getElementById("High").innerHTML = obj.main.temp_max;
     document.getElementById("Low").innerHTML =obj.main.temp_min;
     document.getElementById("feels").innerHTML =obj.main.feels_like;
     document.getElementById("wndSpeed").innerHTML =obj.wind.speed;
  })  
 
}

/*
This method renders the fields and functions nessesary to get the user input of
a city name.

*/
function InputLocation(){

  const [input, setInput] = useState(' ');

  /*
     This function is called when the user is ready to submit a request for the 
     weather in a city of their chosing

   */
  function handleSubmit(e) {
    
    console.log('You clicked submit.');
    
    console.log(input);
    getLocWeather(input)
    
  }
  
  return (
    <div className="get-location">
      <label>Enter City: </label>
      <input type="text" id="location" name="location" onInput={e => setInput(e.target.value)}></input>
      <br></br>
      <button id="sumbit" onClick={handleSubmit}>submit</button>
    </div>
    
  )
}

/*
This function renders the front page of the application

*/
ReactDOM.render(<InputLocation />, document.getElementById('root'));

