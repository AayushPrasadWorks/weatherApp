from flask import Flask, escape, request

import os
import urllib.request
import json
import getWeather


api_key = os.getenv('WEATHERMAP_API_KEY')


app = Flask(__name__)

#gets weather history for next 7 days in current city
@app.route('/weather',methods =['GET'])
def weatherLookUp():
  if api_key is None:
      return "No API key"
  if request.method == 'GET':
    location = request.args.get("location", None)
    return getWeather.getCurrentWeather(location, api_key)


#gets weather history for next 7 days in current city
@app.route('/sevenDay',methods =['GET'])
def weatherHist():
  if api_key is None:
      return "No API key"
  if request.method == 'GET':
    location = request.args.get("location", None)
    return getWeather.getSevenDay(location, api_key)

    


  
  #url = "api.openweathermap.org/data/2.5/weather?q=New York&appid="+api_key
  #response = urllib.request.urlopen(url).read() 
 


def main():
  hostname = os.getenv('FLASK_HOST')
  if hostname is None:
    hostname = '127.0.0.1'
  

  print ("Running on %s" %(hostname))
  app.run(host= hostname)
  
  
if __name__ == "__main__":
  main()
