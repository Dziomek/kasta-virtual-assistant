import wikipedia
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
from .wikipedia_search import WikiSearch
import json
import kasta.greetings
import kasta.date
import kasta.acknowledgment
import kasta.general_response

class Kasta:
    def __init__(self):
        self.engine = pyttsx3.init()
        #self.engine.connect('finished-utterance', self.stop_listening)
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)
        self.model = Model("model")
        self.rec = KaldiRecognizer(self.model, 16000)
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8000)
        self.text = ""
        self.data = None
        self.load_json()

    def load_json(self):
        with open('kasta/data.json') as f:
            self.data = json.load(f)
            for command in self.data['commands']:
                print(command)

    def decision_making_process(self, i):
        print(self.data['commands'][i]['action'])
        match self.data['commands'][i]['action']:
            case "wiki_search":
                try:
                    person = WikiSearch.wiki_person(self.text)
                    wiki = wikipedia.summary(person, sentences=2)
                    print(wiki), self.speak(wiki)
                except KeyboardInterrupt:
                    print('dziwne')
            case "say_hello":
                say_hello_response = kasta.greetings.sayHello()
                print(say_hello_response), self.speak(say_hello_response)
            case "say_time":
                say_time_response = kasta.date.Date.say_time(self.text)
                print(say_time_response), self.speak(say_time_response)
            case "say_thank_you":
                say_acknowledgment = kasta.acknowledgment.thank_you()
                print(say_acknowledgment), self.speak(say_acknowledgment)
            case "general_response":
                say_general_response = kasta.general_response.GeneralResponse.general_response(self.text)
                print(say_general_response), self.speak(say_general_response)




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

                for i in range(len(self.data['commands'])):
                    print(f'wywolanie {i}, current text: {self.text}')
                    if self.data['commands'][i]['name'] in self.text  :
                        try:
                            self.decision_making_process(i)
                            break
                        except Exception:
                            self.speak('Something went wrong. Please try again')



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
