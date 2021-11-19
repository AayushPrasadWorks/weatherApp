from datetime import datetime
import requests
import json



def getCurrentWeather(location, api_key):
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q='
    api_url = api_url+location+'&appid='+api_key+'&units=imperial'
    print(api_url)
    res = requests.get(api_url)
    response = res.json()
    if response["cod"] is not 200:
        return None
    return response


def getSevenDay(location, api_key):
    response = getCurrentWeather(location, api_key)
    if response["cod"] is not 200:
        return None
    api_url = 'https://api.openweathermap.org/data/2.5/onecall/timemachine?'
    api_url = api_url+'lat='+str(response["coord"]["lat"])+'&lon='+str(response["coord"]["lon"])+'&dt='+str(response["dt"])+'&exclude=hourly,minutely'+'&appid='+api_key+'&units=imperial'
    print(api_url)
    res = requests.get(api_url)
    response = res.json()
    return response
    

    