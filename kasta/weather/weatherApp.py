import datetime as dt
import requests
import json
from urllib.request import urlopen

url='http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response)

API_KEY = open('kasta/weather/apikey.txt','r').read()
print(API_KEY)
CITY = data['city']
BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={CITY}&APPID={API_KEY}'

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

response = requests.get(BASE_URL).json()
temperature = round(kelvin_to_celsius(response['main']['temp']),2)
feels_like_temperature = round(kelvin_to_celsius(response['main']['feels_like']),2)
pressure = response['main']['pressure']
humidity = response['main']['humidity']
wind = response['wind']['speed']
description = response['weather'][0]['description']
sunrise_time = (dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])).strftime("%H:%M")
sunset_time = (dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])).strftime("%H:%M")


class Weather:

    @staticmethod
    def get_weather(text):
        if 'weather' in text:
            return f"Currently in {CITY} is {description}, the temperature is {temperature} degrees Celsius. The feel like temperature is around {feels_like_temperature} degrees Celsius." \
                   f" The pressure is {pressure} hectopascals. Humidity {humidity} percent. Wind {wind}."

        if 'whether' in text:
            return f"Currently in {CITY} is {description}, the temperature is {temperature} degrees Celsius. The feel like temperature is around {feels_like_temperature} degrees Celsius." \
                   f" The pressure is {pressure} hectopascals. Humidity {humidity} percent. Wind {wind}."

        if 'sunrise time' in text:
            return f'For {CITY} sunrise will be at {sunrise_time} and Sunset at {sunset_time}.'

        if 'sunset time' in text:
            return f'For {CITY} sunrise will be at {sunrise_time} and Sunset at {sunset_time}.'




