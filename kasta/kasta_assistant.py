import multiprocessing
import threading
import random
import time

import wikipedia
from PySide2 import QtCore
from PySide2.QtCore import QThread
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
from kasta.wiki.wikipedia_search import WikiSearch
import json
from .json_loader import make_json, load_apps
import kasta.greetings.greetings
import kasta.date.date
import kasta.acknowledgement.acknowledgment
import kasta.general_response.general_response
from kasta.openApp.open_applications import OpenApp
import kasta.jokes.jokes_app
import kasta.news.news
import kasta.note.makeNote
from kasta.note.type_note import type_note
import kasta.wolfram.wolframAlpha
import kasta.rockpaperscisorrs.game
import kasta.read_note.readNote
import kasta.help.help
import SMSService.smsService
import kasta.remindMe.reminder
from .weather.weatherApp import Weather
import kasta.headsortails.tossCoin
import kasta.googlesearch.googlesearch
from .youtube.youtube_playing import YoutubeService
from datetime import datetime
from playsound import playsound
from DataBase.Connection import ConnectDatabase
from EmailService.emailService import MailService
from .notification.notification import notify_me


class Kasta:
    def __init__(self):
        ################ LISTENING/SPEAKING PARAMETERS ##############

        self.engine = pyttsx3.init()
        # self.engine.connect('finished-utterance', self.stop_listening)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.model = Model("model")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        ######################################
        self.text = ''
        self.response = ''
        self.json_list = make_json()
        self.data = None
        self.appFirstRun = True
        #######################################
        self.is_listening = False
        self.is_speaking = False
        self.is_action_performed = False

        ################### USER DATA #####################

        self.user_email = ''
        self.user_name = ''
        self.user_id = ''
        self.phoneNumber = ''
        self.apps = {}

        print(self.apps)


    def get_open_commands_from_db(self):
        connection = ConnectDatabase()
        self.apps = load_apps()
        apps_db = connection.get_commands(self.user_id)
        for command in apps_db:
            self.apps[command[0]] = command[1]

        #print(self.apps)


    def speak(self, text):
        self.is_speaking = True
        timer = QtCore.QTimer()
        timer.start(500)# po to, by moc jeszcze wylaczyc kaste, zanim zacznie mowic (bug fix)
        timer.stop()
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
        # time.sleep(2) # po to, by bezpiecznie wylaczyc kaste po zakonczeniu mowienia (bug fix)
        self.is_speaking = False
        print('Speaking:' + str(self.is_speaking))

    def listen(self):
        '''if self.appFirstRun:
            self.greet_user()'''
        self.appFirstRun = False
        if not self.is_listening and not self.is_action_performed and not self.is_speaking:
            print('listening...')
            self.text = ""
            self.stream.start_stream()
            self.is_listening = True

            while True:
                data = self.stream.read(4000, exception_on_overflow=False)
                if len(data) == 0:
                    break
                if self.rec.AcceptWaveform(data):
                    self.text = self.rec.Result()[13:-1]  # od 12 po to, żeby wypisać samą komendę (bez 'text' itp)
                    self.text = self.text.replace('"', '')
                    self.text = self.text.replace(self.text[-1], '')

                    self.find_action_in_json()

    def listen2(self):
        print('listening2...')
        self.stream.start_stream()

        while True:
            data = self.stream.read(4000, exception_on_overflow=False)
            if len(data) == 0:
                break
            if self.rec.AcceptWaveform(data):
                self.text = self.rec.Result()[13:-1]  # od 12 po to, żeby wypisać samą komendę (bez 'text' itp)
                self.text = self.text.replace('"', '')
                self.text = self.text.replace(self.text[-1], '')

                return self.text

    ##print(self.rec.FinalResult())

    '''def onWord(self, name, location, length):
        print ('word', name, location, length)
        if location > 10:
            self.engine.stop()
    '''

    '''def take_typed_command(self, text):
        if not self.is_listening:
            self.typed_text = text'''

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

    def do_typed_command(self):
        print(self.user_id)
        p1 = threading.Thread(target=self.find_action_in_json)
        p1.start()





    ########################### DECISIONS #########################







    def decision_making_process(self, i, key_word):
        self.is_action_performed = True
        self.response = ''
        print(f'Keyword: {key_word}')
        print(f"Action: {self.json_list[i]['commands']['action']}")
        match self.json_list[i]['commands']['action']:
            case "help":
                self.help_action()
            case "wiki_search":
                self.wiki_search_action()
            case "say_hello":
                self.say_hello_action()
            case "say_time":
                self.say_time_action()
            case "say_thank_you":
                self.say_thank_you_action()
            case "general_response":
                self.general_response_action()
            case "open_app":
                self.open_app_action(self.text.split('open', 2)[1].strip(), self.apps)
            case "tell_jokes":
                self.tell_jokes_action()
            case "tell_news":
                self.tell_news_action()
            case "play_yt":
                self.play_yt_action(key_word)
            case "calculate":
                self.calculate_action()
            case "weather":
               self.weather_action(key_word)
            case "flip_coin":
                self.flip_coin_action()
            case "play_song":  ##### do wywalenia
                self.play_song_action()
            case "play_game":
                self.play_game_action()
            case "make_note":
                self.make_note_action()
            case "read_note":
                self.read_note_action()
            case "email_note":
                self.email_note_action()
            case "send_sms":
                pass
            case "notify":
                self.notify_action()
            case "search_google":
                self.search_google_action()
            case "remind_me":
                self.remind_me_action()
            case "type_note":
                self.type_note_action()

    def greet_user(self):
        """Greets the user according to the time"""
        playsound('kasta/sound3.wav')
        hour = datetime.now().hour
        if (hour >= 6) and (hour < 12):
            self.speak(f"Good morning {self.user_name}")
        elif (hour >= 12) and (hour < 16):
            self.speak(f"Good afternoon {self.user_name}")
        elif (hour >= 16) and (hour < 19):
            self.speak(f"Good Evening {self.user_name}")
        self.speak("I am Kasta. How may I assist you?")

    def find_action_in_json(self):
        is_done = False
        print('jestem tu')
        if not self.is_speaking:
            try:
                for i in range(len(self.json_list)):
                    for j in range(len(self.json_list[i]['commands']['name'])):
                        if self.json_list[i]['commands']['name'][j] in self.text:
                            self.decision_making_process(i, self.json_list[i]['commands']['name'][j])
                            is_done = True

                    if is_done:
                        break
            except KeyError:
                self.speak("I didn't find it in my dictionary. Please try again")
                print('JSON file error')


    ########################### ACTIONS #########################





    def help_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.help.help.helpMe()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def wiki_search_action(self):
        playsound('kasta/sound2.wav')
        try:
            person = WikiSearch.wiki_person(self.text)
            self.response = wikipedia.summary(person, sentences=2)
            print(self.response), self.speak(self.response)
        except Exception:
            print('Unfortunately I did not find this page. Please try again')
        self.is_action_performed = False

    def say_hello_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.greetings.greetings.sayHello()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def say_time_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.date.date.Date.say_time(self.text)
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def say_thank_you_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.acknowledgement.acknowledgment.thank_you()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def general_response_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.general_response.general_response.GeneralResponse.general_response(
            self.text)
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def open_app_action(self, key_word, apps_list):
        playsound('kasta/sound2.wav')
        p = multiprocessing.Process(target=OpenApp.open_application, args=(key_word, apps_list, ))
        p.start()
        p.join()
        self.response = f"Opening application"
        self.is_action_performed = False

    def tell_jokes_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.jokes.jokes_app.tell_joke()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def tell_news_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.news.news.tell_news()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def play_yt_action(self, key_word):
        playsound('kasta/sound2.wav')
        p = multiprocessing.Process(target=YoutubeService.play_on_yt, args=(self.text, key_word,))
        p.start()
        p.join()
        self.is_action_performed = False

    def calculate_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.wolfram.wolframAlpha.Calculate.makeCalculations(self.text)
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def weather_action(self, key_word):
        weather = Weather()
        if self.text != "weather" and self.text != "whether":
            weather.city = self.text.split(' ')[1]
            ##weather.city = weather.city.replace(weather.city[-1], '') ## usuniecie znaku /n na koncu miasta

        else:
            weather.city = ''
        playsound('kasta/sound2.wav')
        self.response = weather.get_weather(key_word, weather.city)
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def flip_coin_action(self):
        playsound('kasta/sound2.wav')
        self.response = kasta.headsortails.tossCoin.tossCoin()
        print(self.response), self.speak(self.response)
        self.is_action_performed = False

    def play_song_action(self):
        playsound('kasta/sound2.wav')
        self.speak("Choose among rock, paper or scissors.")
        self.is_action_performed = False
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
        self.is_action_performed = False

    def play_game_action(self):
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
        self.is_action_performed = False

    def make_note_action(self):
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
                note = note.strip()
                print(note)
                self.stop_listening()
                connection = ConnectDatabase()
                idUsers = connection.returnIdUser(self.user_email)
                UserId = idUsers[0][0]

                kasta.note.makeNote.make_note(title, note, UserId)
                time.sleep(1)
                self.speak("I have passed your note to database.")
                self.listen()

                break
            elif "no" in response:
                self.speak("What is the topic of your note?")
        self.is_action_performed = False

    def read_note_action(self):
        playsound('kasta/sound2.wav')
        self.speak("I will read your all notes topics. Chose one of them.")
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.user_email)
        UserId = idUsers[0][0]

        topics = connection.returnNotesTopics(UserId)
        print(topics)
        topics_list = []

        for topic in topics:
            print(topic[0])
            self.speak(topic[0])
            topics_list.append(topic[0])

        while True:
            user_choose = self.listen2()
            for topic in topics_list:
                if topic in user_choose:
                    self.stop_listening()
                    print('topic', topic)
                    print(user_choose)

                    self.speak(f"Is {user_choose} correct ?")

                    response = self.listen2()
                    print(response)
                    self.stop_listening()

                    if "yes" in response:
                        user_choose = user_choose.strip()
                        self.response = connection.returnNote(user_choose, UserId)
                        if self.response is not None:
                            self.response = self.response[0][0]
                            print(self.response)
                            self.speak(self.response), print(self.response)
                    elif "no" in response:
                        self.speak('Choose a topic'), print('Choose a topic')
                        break
            break
        self.listen()
        self.is_action_performed = False

    def send_note_via_phone(self):
        playsound('kasta/sound2.wav')
        self.speak("I will read your all notes topics. Chose one of them.")
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.user_email)
        UserId = idUsers[0][0]

        topics = connection.returnNotesTopics(UserId)
        print(topics)
        topics_list = []

        for topic in topics:
            print(topic[0])
            self.speak(topic[0])
            topics_list.append(topic[0])

        while True:
            user_choose = self.listen2()
            for topic in topics_list:
                if topic in user_choose:
                    self.stop_listening()
                    print('topic', topic)
                    print(user_choose)

                    self.speak(f"Is {user_choose} correct ?")

                    response = self.listen2()
                    print(response)
                    self.stop_listening()

                    if "yes" in response:
                        user_choose = user_choose.strip()
                        self.response = connection.returnNote(user_choose, UserId)
                        if self.response is not None:
                            description = self.response[0][0]
                            topic = user_choose

                            smsservice = SMSService.smsService.SendSms()
                            user_phone_number = '+48' + self.phoneNumber
                            smsservice.send_note(topic, description, user_phone_number)

                    elif "no" in response:
                        self.speak('Choose a topic'), print('Choose a topic')
                        break
            break
        self.listen()
        self.is_action_performed = False

    def email_note_action(self):
        playsound('kasta/sound2.wav')
        self.speak("I will read your all notes topics. Chose one of them.")
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.user_email)
        UserId = idUsers[0][0]

        topics = connection.returnNotesTopics(UserId)
        print(topics)
        topics_list = []

        for topic in topics:
            print(topic[0])
            self.speak(topic[0])
            topics_list.append(topic[0])

        while True:
            user_choose = self.listen2()
            for topic in topics_list:
                if topic in user_choose:
                    self.stop_listening()
                    print('topic', topic)
                    print(user_choose)

                    self.speak(f"Is {user_choose} correct ?")

                    response = self.listen2()
                    print(response)
                    self.stop_listening()

                    if "yes" in response:
                        user_choose = user_choose.strip()
                        note = connection.returnNote(user_choose, UserId)
                        self.response = note
                        if self.response is not None:
                            self.response = self.response[0][0]

                            ##email
                            sendmail = MailService()
                            sendmail.sendNoteViaEmail(self.user_name, self.user_email, user_choose, note[0][0])

                            self.response = f"Your note with topic {user_choose} and with content {self.response} was sent to your email."
                            self.speak(self.response),
                            print(self.response)

                    elif "no" in response:
                        self.speak('Choose a topic'), print('Choose a topic')
                        break
            break
        self.listen()
        self.is_action_performed = False

    def notify_action(self):
        print(self.text)
        notify_me(self.text)
        self.is_action_performed = False

    def search_google_action(self):
        playsound('kasta/sound2.wav')
        search = self.text.split(" ", 3)[3]
        response = kasta.googlesearch.googlesearch.search_google(search)
        self.response = f"Searching {search} in Google"
        self.is_action_performed = False

    def remind_me_action(self):
        playsound('kasta/sound2.wav')
        self.speak("What reminder should i set?")

        while True:
            reminder = self.listen2()
            print(reminder)
            self.stop_listening()

            self.speak('please tell when it happens')
            date = self.listen2()
            print(date)
            self.stop_listening()

            self.speak(f"Your new reminder is {reminder} is set to {date}. Is it correct?")
            response = self.listen2()
            print(response)
            self.stop_listening()
            if 'yes' in response:
                self.speak('I will sent your reminder to your phone number which is associated with your '
                           'account.')
                smsservice = SMSService.smsService.SendSms()
                user_phone_number = '+48' + self.phoneNumber
                smsservice.send_reminder(reminder, date, user_phone_number)

                self.listen()
                break
        self.is_action_performed = False

    def type_note_action(self):
        playsound('kasta/sound2.wav')
        type_note(self.text, self.user_id)
        self.speak('I saved your note')
        self.is_action_performed = False



###################################### WORKING THREAD ###############################







class KastaWorker(QThread):
    def __init__(self):
        super().__init__()
        self.kasta = Kasta()

    def run(self):
        self.kasta.listen()

    def stop(self):
        if self.kasta.is_listening:
            if not self.kasta.is_speaking:
                if not self.kasta.is_action_performed:
                    self.terminate()
                    self.kasta.stop_listening()






