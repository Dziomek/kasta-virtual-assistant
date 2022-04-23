from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3
from kasta.current_time import SystemInfo


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
                if "time today" in self.text:
                    print(self.text)
                    self.speak(SystemInfo.get_time())
                elif "today" in self.text:
                    self.speak("Thanks, I'm fine.")
                else:
                    self.speak(self.text)
                    print(self.text)

    ##print(self.rec.FinalResult())

    def onWord(self, name, location, length):
        print ('word', name, location, length)
        if location > 10:
            self.engine.stop()

    def stop_listening(self):
        self.stream.stop_stream()
        self.text = ""
        print('listening stopped')

    def terminate_kasta(self):
        self.engine.stop()
        self.stream.close()
        self.p.terminate()
