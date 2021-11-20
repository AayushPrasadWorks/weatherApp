from flask import Flask, escape, request

import os
import urllib.request
import json

from flask.json import JSONDecoder, jsonify
from flask.wrappers import Response
from flask_cors import CORS

import getWeather



#Use this api key definition to use when running on docker container
#api_key = os.getenv('WEATHERMAP_API_KEY')

#sample api key
api_key= 'd4450502dc2d565c203526c49b66b8cc'

app = Flask(__name__)
CORS(app)


"""

This method recieves the client's request and gets the weather given a city name and the api key
from OpenWeatherMap

endpoint = '/weather'
"""
@app.route('/weather',methods =['GET'])
def weatherLookUp():
  if api_key is None:
      return "No API key"
  if request.method == 'GET':
    location = request.args.get("location", None)
    print('return')
    
    return json.dumps(getWeather.getCurrentWeather(location, api_key))


#gets weather history for next 7 days in current city
@app.route('/sevenDayAvg',methods =['GET'])
def weatherHist():
  if api_key is None:
      return "No API key"
  if request.method == 'GET':
    location = request.args.get("location", None)
    res = json.dumps(getWeather.getSevenDay(location, api_key))
    print(res)
    return res
    


  
  #url = "api.openweathermap.org/data/2.5/weather?q=New York&appid="+api_key
  #response = urllib.request.urlopen(url).read() 
 


def main():  
  app.run(host='0.0.0.0')
  
  
if __name__ == "__main__":
  main()
