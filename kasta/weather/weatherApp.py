import datetime as dt
import requests
import json
from urllib.request import urlopen
from kasta.json_loader import load_json

'''url = 'http://ipinfo.io/json'
response = urlopen(url)
data = json.load(response
'''

API_KEY = open('kasta/weather/apikey.txt', 'r').read()
print(API_KEY)


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


def weather_parameters(city):
    pass


class Weather:

    @staticmethod
    def get_weather(key_word, city):
        city = city.replace(city[0], city[0].upper())
        BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={API_KEY}'
        response = requests.get(BASE_URL).json()
        temperature = round(kelvin_to_celsius(response['main']['temp']), 2)
        feels_like_temperature = round(kelvin_to_celsius(response['main']['feels_like']), 2)
        pressure = response['main']['pressure']
        humidity = response['main']['humidity']
        wind = response['wind']['speed']
        description = response['weather'][0]['description']
        sunrise_time = (dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])).strftime(
            "%H:%M")
        sunset_time = (dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])).strftime("%H:%M")

        match key_word:
            case 'weather':
                return f"Currently in {city} is {description}, the temperature is {temperature} degrees Celsius. The feel like temperature is around {feels_like_temperature} degrees Celsius." \
                   f" The pressure is {pressure} hectopascals. Humidity {humidity} percent. Wind {wind}."

            case "whether":
                return f"Currently in {city} is {description}, the temperature is {temperature} degrees Celsius. The feel like temperature is around {feels_like_temperature} degrees Celsius." \
                    f" The pressure is {pressure} hectopascals. Humidity {humidity} percent. Wind {wind}."

            case "sunrise time":
                return f'For {city} sunrise will be at {sunrise_time} and Sunset at {sunset_time}.'

            case 'sunset time':
                return f'For {city} sunrise will be at {sunrise_time} and Sunset at {sunset_time}.'
