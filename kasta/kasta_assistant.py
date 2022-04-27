import multiprocessing
import threading

import wikipedia
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
from kasta.wiki.wikipedia_search import WikiSearch
import json
from .json_loader import load_json
import kasta.greetings.greetings
import kasta.date.date
import kasta.acknowledgement.acknowledgment
import kasta.general_response.general_response
from kasta.openApp.open_applications import OpenApp
import kasta.jokes.jokes_app
import kasta.news.news
import kasta.wolfram.wolframAlpha
import kasta.weather.weatherApp
import kasta.headsortails.tossCoin
from .youtube.youtube_playing import YoutubeService
from datetime import datetime
from playsound import playsound

USERNAME = 'Pawel'  # tymczasowo


class Kasta:
    def __init__(self):
        self.engine = pyttsx3.init()
        # self.engine.connect('finished-utterance', self.stop_listening)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.model = Model("model")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.text = ""
        self.data = None
        #########
        self.json_list = []
        self.json_list.append(load_json('kasta/date/date_data.json'))
        self.json_list.append(load_json('kasta/openApp/openApp_data.json'))
        self.json_list.append(load_json('kasta/wiki/wikipedia_data.json'))
        self.json_list.append(load_json('kasta/jokes/jokes_data.json'))
        self.json_list.append(load_json('kasta/news/news_data.json'))
        self.json_list.append(load_json('kasta/youtube/youtube_data.json'))
        self.json_list.append(load_json('kasta/wolfram/wolfram_data.json'))
        self.json_list.append(load_json('kasta/greetings/greetings_data.json'))
        self.json_list.append(load_json('kasta/general_response/general_response_data.json'))
        self.json_list.append(load_json('kasta/acknowledgement/acknowledgement_data.json'))
        self.json_list.append(load_json('kasta/weather/weather_data.json'))
        self.json_list.append(load_json('kasta/headsortails/headsortails_data.json'))
        self.json_list.append(load_json('kasta/spotify/spotify_data.json'))

    def decision_making_process(self, i, key_word):
        print(f'Keyword: {key_word}')
        print(f"Action: {self.json_list[i]['commands']['action']}")
        match self.json_list[i]['commands']['action']:
            case "wiki_search":
                playsound('kasta/sound2.wav')
                try:
                    person = WikiSearch.wiki_person(self.text)
                    wiki = wikipedia.summary(person, sentences=2)
                    print(wiki), self.speak(wiki)
                except Exception:
                    print('Unfortunately I did not find this page. Please try again')
            case "say_hello":
                playsound('kasta/sound2.wav')
                say_hello_response = kasta.greetings.greetings.sayHello()
                print(say_hello_response), self.speak(say_hello_response)
            case "say_time":
                playsound('kasta/sound2.wav')
                say_time_response = kasta.date.date.Date.say_time(self.text)
                print(say_time_response), self.speak(say_time_response)
            case "say_thank_you":
                playsound('kasta/sound2.wav')
                say_acknowledgment = kasta.acknowledgement.acknowledgment.thank_you()
                print(say_acknowledgment), self.speak(say_acknowledgment)
            case "general_response":
                playsound('kasta/sound2.wav')
                say_general_response = kasta.general_response.general_response.GeneralResponse.general_response(
                    self.text)
                print(say_general_response), self.speak(say_general_response)
            case "open_app":
                playsound('kasta/sound2.wav')
                p = multiprocessing.Process(target=OpenApp.open_application, args=(key_word,))
                p.start()
                p.join()
                ##print(say_open_app), self.speak(say_open_app)
            case "tell_jokes":
                playsound('kasta/sound2.wav')
                tell_jokes = kasta.jokes.jokes_app.tell_joke()
                print(tell_jokes), self.speak(tell_jokes)
            case "tell_news":
                playsound('kasta/sound2.wav')
                tell_news = kasta.news.news.tell_news()
                print(tell_news), self.speak(tell_news)
            case "play_yt":
                p = multiprocessing.Process(target=YoutubeService.play_on_yt, args=(self.text, key_word,))
                p.start()
                p.join()
            case "calculate":
                playsound('kasta/sound2.wav')
                calculate = kasta.wolfram.wolframAlpha.Calculate.makeCalculations(self.text)
                print(calculate), self.speak(calculate)
            case "weather":
                playsound('kasta/sound2.wav')
                weather = kasta.weather.weatherApp.Weather.get_weather(self.text)
                print(weather), self.speak(weather)
            case "flip_coin":
                playsound('kasta/sound2.wav')
                coin = kasta.headsortails.tossCoin.tossCoin()
                print(coin), self.speak(coin)
            case "play_song":
                playsound('kasta/sound2.wav')
                self.speak("I will open spotify in a minute. What song do you want me to play?")
                while True:
                    nowyTekst = self.listen2()
                    print(nowyTekst)
                    self.stop_listening()
                    if 'windows' in nowyTekst:
                        self.speak('Mata is very good. Do you want to play this song')
                        nowyTekst2 = self.listen2()
                        self.stop_listening()
                        if 'yes' in nowyTekst2:
                            self.speak('Ok. i will play it ')
                            self.listen()
                            break


    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        '''else:
            self.engine.endLoop()
            self.engine.stop()
            self.engine = pyttsx3.init()
            self.engine.say(text)
            self.engine.runAndWait()
        '''

    def greet_user(self):
        """Greets the user according to the time"""
        playsound('kasta/sound3.wav')
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(f"Good morning {USERNAME}")
        elif (hour >= 12) and (hour < 16):
            self.speak(f"Good afternoon {USERNAME}")
        elif (hour >= 16) and (hour < 19):
            self.speak(f"Good Evening {USERNAME}")
        self.speak("I am Kasta. How may I assist you?")

    def listen(self):
        #self.greet_user()
        print('listening...')
        self.stream.start_stream()
        is_done = False
        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                self.text = self.rec.Result()[12:-1]  # od 12 po to, żeby wypisać samą komendę (bez 'text' itp)
                self.text = self.text.replace('"', '')
                try:
                    for i in range(len(self.json_list)):
                        for j in range(len(self.json_list[i]['commands']['name'])):
                            if self.json_list[i]['commands']['name'][j] in self.text:
                                self.decision_making_process(i, self.json_list[i]['commands']['name'][j])
                                is_done = True

                        if is_done:
                            is_done = False
                            break
                except KeyError:
                    print('JSON file error')

    def listen2(self):
        print('listening2...')
        self.stream.start_stream()

        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                self.text = self.rec.Result()[12:-1]  # od 12 po to, żeby wypisać samą komendę (bez 'text' itp)
                self.text = self.text.replace('"', '')

                return self.text

    ##print(self.rec.FinalResult())

    '''def onWord(self, name, location, length):
        print ('word', name, location, length)
        if location > 10:
            self.engine.stop()
    '''

    def stop_listening(self):
        self.stream.stop_stream()
        self.text = ""
        print('listening stopped')

    def terminate_kasta(self):
        self.engine.stop()
        self.stream.close()
        self.p.terminate()
