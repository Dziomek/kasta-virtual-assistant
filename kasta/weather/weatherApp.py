import datetime as dt
import requests
import json
from urllib.request import urlopen


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


class Weather:
    def __init__(self):
        self.city, self.BASE_URL, self.response, self.temperature, self.response, self.feels_like_temperature \
            = (None, None, None, None, None, None)
        self.pressure, self.humidity, self.wind, self.sunrise_time, self.sunset_time, self.description \
            = (None, None, None, None, None, None)
        self.API_KEY = open('kasta/weather/apikey.txt', 'r').read()

    def get_weather(self, key_word, city):
        if city:
            self.city = city.replace(city[0], city[0].upper())

        else:
            url = 'http://ipinfo.io/json'
            self.city = json.load(urlopen(url))['city']
        self.BASE_URL = f'http://api.openweathermap.org/data/2.5/weather?q={self.city}&APPID={self.API_KEY}'
        self.response = requests.get(self.BASE_URL).json()
        self.temperature = round(kelvin_to_celsius(self.response['main']['temp']), 2)
        self.feels_like_temperature = round(kelvin_to_celsius(self.response['main']['feels_like']), 2)
        self.pressure = self.response['main']['pressure']
        self.humidity = self.response['main']['humidity']
        self.wind = self.response['wind']['speed']
        self.description = self.response['weather'][0]['description']
        self.sunrise_time = (dt.datetime.utcfromtimestamp(self.response['sys']['sunrise'] + self.response['timezone'])).strftime(
            "%H:%M")
        self.sunset_time = (dt.datetime.utcfromtimestamp(self.response['sys']['sunset'] + self.response['timezone'])).strftime("%H:%M")

        if 'weather' or 'whether' in key_word:
            return f"Currently in {self.city} is {self.description}, the temperature is {self.temperature} degrees Celsius. The feel like temperature is around {self.feels_like_temperature} degrees Celsius." \
                       f" The pressure is {self.pressure} hectopascals. Humidity {self.humidity} percent. Wind {self.wind}."
        elif 'sunrise' in key_word:
            return f'For {self.city} sunrise will be at {self.sunrise_time} and Sunset at {self.sunset_time}.'
        elif 'sunset' in key_word:
            return f'For {self.city} sunrise will be at {self.sunrise_time} and Sunset at {self.sunset_time}.'
