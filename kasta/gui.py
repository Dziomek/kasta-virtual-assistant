import sys
import time
import threading
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread
from kasta.speaking_listening import Kasta


###### WorkerThread zawiera kaste, WelcomePage zawiera WorkerThreada


class WelcomePage(QDialog):
    def __init__(self):
        super(WelcomePage, self).__init__()
        loadUi("welcomepage.ui", self)
        self.startButton.clicked.connect(self.begin)
        self.endButton.clicked.connect(self.end)
        self.worker = WorkerThread()  # to run Kasta in background
        self.is_running = False  # to prevent clicking start button when Kasta in already running
        self.isEndClicked = False
        t1 = threading.Thread(target=self.change_text)  # changing text live
        t1.start()

    def end(self):
        self.isEndClicked = True
        self.worker.kasta.speak('Goodbye')
        time.sleep(0.5)
        sys.exit()

    def begin(self):
        if not self.is_running:
            self.is_running = True
            self.worker.start()

    def change_text(self):
        while True:
            self.lineEdit.setText(self.worker.kasta.text)
            if self.isEndClicked:
                break


class WorkerThread(QThread):
    def __init__(self):
        super().__init__()
        self.kasta = Kasta()

    def run(self):
        self.kasta.listen()










