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
import kasta.openApp.open_applications
import kasta.jokes.jokes_app
import kasta.news.news
from .youtube.youtube_playing import play_on_yt
import time
from playsound import playsound
import speech_recognition as sr

class Kasta:
    def __init__(self):
        self.listener = sr.Recognizer() ### to make app faster
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
        self.json_list.append(load_json('kasta/wiki/wikipedia_data.json'))
        self.json_list.append(load_json('kasta/greetings/greetings_data.json'))
        self.json_list.append(load_json('kasta/general_response/general_response_data.json'))
        self.json_list.append(load_json('kasta/date/date_data.json'))
        self.json_list.append(load_json('kasta/openApp/openApp_data.json'))
        self.json_list.append(load_json('kasta/jokes/jokes_data.json'))
        self.json_list.append(load_json('kasta/news/news_data.json'))
        self.json_list.append(load_json('kasta/acknowledgement/acknowledgement_data.json'))
        self.json_list.append(load_json('kasta/youtube/youtube_data.json'))

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
                say_open_app = kasta.openApp.open_applications.OpenApp.OpenAplication(self.text)
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
                p = multiprocessing.Process(target=play_on_yt, args=(self.text, key_word,))
                p.start()
                p.join()

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

    def listen(self):
        print('listening...')
        self.stream.start_stream()
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
                                print(self.text)
                                break

                except KeyError:
                    print('JSON file error')






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
