import sys

from PyQt5.QtCore import QProcess
from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3

import kasta.gui
from kasta.current_time import SystemInfo
from kasta.speaking_listening import Kasta
from kasta.gui import WelcomePage
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QDialog, QApplication


if __name__ == '__main__':

    app = QApplication(sys.argv)
    welcome = WelcomePage()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(welcome)
    widget.setFixedHeight(800)
    widget.setFixedWidth(1200)
    widget.show()

    try:
        app.exec()
    except:
       print('Exiting')

