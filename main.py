import sys

from PyQt5.QtCore import QProcess
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3

from kasta.current_time import SystemInfo
from kasta.kasta_assistant import Kasta
from kasta.gui import KastaPage, WelcomePage, CreateWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widgets = CreateWidgets()
    app.exec()
