import multiprocessing
import threading
import random
import time

import wikipedia
from PySide2.QtCore import QThread
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
import kasta.note.makeNote
import kasta.wolfram.wolframAlpha
import kasta.rockpaperscisorrs.game
import kasta.read_note.readNote
from .weather.weatherApp import Weather
import kasta.headsortails.tossCoin
from .youtube.youtube_playing import YoutubeService
from datetime import datetime
from playsound import playsound
from DataBase.Connection import ConnectDatabase

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
        self.appFirstRun = True

        ####

        self.user_email = ''
        self.user_name = ''

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
        self.json_list.append(load_json('kasta/rockpaperscisorrs/rockpapersisorrs_data.json'))
        self.json_list.append(load_json('kasta/note/note_data.json'))
        #self.json_list.append(load_json('kasta/read_note/read_note_data.json'))

        self.is_listening = False
        self.is_speaking = False

        ####
        self.response = ''




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
                self.response = kasta.greetings.greetings.sayHello()
                print(self.response), self.speak(self.response)
            case "say_time":
                playsound('kasta/sound2.wav')
                self.response = kasta.date.date.Date.say_time(self.text)
                print(self.response), self.speak(self.response)
            case "say_thank_you":
                playsound('kasta/sound2.wav')
                self.response = kasta.acknowledgement.acknowledgment.thank_you()
                print(self.response), self.speak(self.response)
            case "general_response":
                playsound('kasta/sound2.wav')
                self.response = kasta.general_response.general_response.GeneralResponse.general_response(
                    self.text)
                print(self.response), self.speak(self.response)
            case "open_app":
                playsound('kasta/sound2.wav')
                p = multiprocessing.Process(target=OpenApp.open_application, args=(key_word,))
                p.start()
                p.join()
                ##print(say_open_app), self.speak(say_open_app)
                self.response = f"Opening {key_word.split(' ', 2)[1]}"
            case "tell_jokes":
                playsound('kasta/sound2.wav')
                self.response = kasta.jokes.jokes_app.tell_joke()
                print(self.response), self.speak(self.response)
            case "tell_news":
                playsound('kasta/sound2.wav')
                self.response = kasta.news.news.tell_news()
                print(self.response), self.speak(self.response)
            case "play_yt":
                playsound('kasta/sound2.wav')
                p = multiprocessing.Process(target=YoutubeService.play_on_yt, args=(self.text, key_word,))
                p.start()
                p.join()
            case "calculate":
                playsound('kasta/sound2.wav')
                self.response = kasta.wolfram.wolframAlpha.Calculate.makeCalculations(self.text)
                print(self.response), self.speak(self.response)
            case "weather":
                weather = Weather()
                if self.text != "weather" and self.text != "whether":
                    weather.city = self.text.split(' ')[1]
                    ##weather.city = weather.city.replace(weather.city[-1], '') ## usuniecie znaku /n na koncu miasta
                else:
                    weather.city = ''
                playsound('kasta/sound2.wav')
                self.response = weather.get_weather(key_word, weather.city)
                print(self.response), self.speak(self.response)
            case "flip_coin":
                playsound('kasta/sound2.wav')
                self.response = kasta.headsortails.tossCoin.tossCoin()
                print(self.response), self.speak(self.response)
            case "play_song":
                playsound('kasta/sound2.wav')
                self.speak("Choose among rock, paper or scissors.")
                while True:
                    nowyTekst = self.listen2()
                    print(nowyTekst)
                    self.stop_listening()
                    if 'rock' in nowyTekst:
                        self.speak('Mata is very good. Do you want to play this song')
                        nowyTekst2 = self.listen2()
                        self.stop_listening()
                        if 'yes' in nowyTekst2:
                            self.speak('Ok. i will play it ')
                            self.listen()
                            break
            case "play_game":
                playsound('kasta/sound2.wav')
                self.speak("Choose among rock, paper or scissors.")
                while True:
                    user_choose = self.listen2()
                    print(user_choose)
                    self.stop_listening()
                    if 'rock' in user_choose or 'paper' in user_choose or 'scissors' in user_choose:
                        self.response = kasta.rockpaperscisorrs.game.game(user_choose)
                        print(self.response), self.speak(self.response)
                        self.listen()
                        break

            case "make_note":
                playsound('kasta/sound2.wav')
                self.speak("What is the topic of your note?")
                while True:
                    title = self.listen2()
                    print(title)
                    self.stop_listening()
                    self.speak(f"Your note topis is {title}. Do you like it ?")
                    response = self.listen2()
                    print(response)
                    self.stop_listening()

                    if "yes" in response:
                        self.speak("I will record your thoughts. Do it quick. Start one second after signal")
                        playsound('kasta/sound2.wav')

                        note = self.listen2()
                        print(note)
                        self.stop_listening()
                        connection = ConnectDatabase()
                        idUsers = connection.returnIdUser(self.user_email)
                        UserId = idUsers[0][0]

                        kasta.note.makeNote.make_note(title, note, UserId)  #### 47 Linijka zwraca None - > do poprawy
                        time.sleep(1)
                        self.speak("I have passed your note to database.")
                        self.listen()

                        break
                    elif "no" in response:
                        self.speak("What is the topic of your note?")
            case "read_note":
                pass

    def speak(self, text):
        self.is_speaking = True
        time.sleep(0.5) # po to, by moc jeszcze wylaczyc kaste, zanim zacznie mowic (bug fix)
        print('Speaking:' + str(self.is_speaking))
        self.engine.say(text)
        self.engine.runAndWait()
        '''else:
            self.engine.endLoop()
            self.engine.stop()
            self.engine = pyttsx3.init()
            self.engine.say(text)
            self.engine.runAndWait()
        '''
        # sleep do wywalenia ze względu na długi czas oczekiwania (problem w make_note) - do obserwacji ~jn
        #time.sleep(2) # po to, by bezpiecznie wylaczyc kaste po zakonczeniu mowienia (bug fix)
        self.is_speaking = False
        print('Speaking:' + str(self.is_speaking))

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
        if self.appFirstRun:
            self.greet_user()
        self.appFirstRun = False
        if not self.is_listening:
            print('listening...')
            self.stream.start_stream()
            self.is_listening = True
            is_done = False
            while True:
                data = self.stream.read(4000, exception_on_overflow=False)
                if len(data) == 0:
                    break
                if self.rec.AcceptWaveform(data):
                    self.text = self.rec.Result()[13:-1]  # od 12 po to, żeby wypisać samą komendę (bez 'text' itp)
                    self.text = self.text.replace('"', '')
                    self.text = self.text.replace(self.text[-1], '')
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
                        self.speak("I didn't find it in my dictionary. Please try again")
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
        if self.is_listening:
            self.is_listening = False
            print('Listening:' + str(self.is_listening))
            self.stream.stop_stream()
            self.text = ""
            print('listening stopped')

    def terminate_kasta(self):
        self.engine.stop()
        self.stream.close()
        self.p.terminate()


class KastaWorker(QThread):
    def __init__(self):
        super().__init__()
        self.kasta = Kasta()

    def run(self):
        self.kasta.listen()

    def stop(self):
        if not self.kasta.is_speaking:
            self.terminate()
            self.kasta.stop_listening()


