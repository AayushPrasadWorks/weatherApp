from datetime import datetime
import urllib.request
import json

"""

This method gets the weather given a city name and the api key
from OpenWeatherMap

the request is formed through appending the api call url from OpenWeatherApi 
with the appropriate values

"""

def getCurrentWeather(location, api_key):
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_url = api_url+location+'&appid='+api_key+'&units=imperial'
    print(api_url)
    
    try:
        request = urllib.request.Request(api_url) 
        request.add_header('Accept', 'application/json') 
        with urllib.request.urlopen(request) as response: 
            source = response.read().decode('utf-8')
        return source   
    except urllib.error.HTTPError as e:
        return None
        

        

    
   
   


"""
def helpGetLoc(location, api_key):
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_url = api_url+location+'&appid='+api_key+'&units=imperial'
    print(api_url)
    res = requests.get(api_url)
    print('RE: '+res)
    response = res.json()
    if response["cod"] is not 200:
        return None
    return response


def getSevenDay(location, api_key):
    response = helpGetLoc(location, api_key)
    if response["cod"] is not 200:
        return None
    api_url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?'
    api_url = api_url+'lat='+str(response["coord"]["lat"])+'&lon='+str(response["coord"]["lon"])+'&dt='+str(response["dt"])+'&exclude=hourly,minutes'+'&appid='+api_key+'&units=imperial'
    print(api_url)
    res = requests.get(api_url)
    print(res)
    response = json.dumps(res)
    return response
    

"""