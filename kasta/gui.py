import sys
import time
import threading
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import QThread
from kasta.kasta_assistant import Kasta


###### WorkerThread zawiera kaste, WelcomePage zawiera WorkerThreada


class WelcomePage(QDialog):
    def __init__(self):
        super(WelcomePage, self).__init__()
        loadUi("welcome_page.ui", self)

    def go_to_kasta(self):
        self.widget.setCurrentIndex(1)


class KastaPage(QDialog):
    def __init__(self):
        super(KastaPage, self).__init__()
        loadUi("kasta_page.ui", self)
        self.startButton.clicked.connect(self.begin)
        self.stopButton.clicked.connect(self.stop)
        self.endButton.clicked.connect(self.end)
        self.worker = WorkerThread()  # to run Kasta in background
        self.is_running = False  # to prevent clicking start button when Kasta in already running
        self.isEndClicked = False

        self.t1 = threading.Thread(target=self.change_text)  # changing text live
        self.t1.start()

    def end(self):
        # TODO!

        '''if not self.is_running:
            del self.worker.kasta
                exit(0)

        else:
            self.worker.terminate()
            self.t1.join()
            self.worker.kasta.stop_listening()
            self.listeningLabel.setText('')
            time.sleep(0.5)
            sys.exit()'''

    def begin(self):
        if not self.is_running:
            self.is_running = True
            self.worker.start()
            self.listeningLabel.setText('listening...')

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.worker.terminate()
            self.worker.kasta.stop_listening()
            self.listeningLabel.setText('')

    def change_text(self):
        while True:
            self.lineEdit.setText(self.worker.kasta.text)
            if self.isEndClicked:
                break


class CreateWidgets:  # implements widget managing
    def __init__(self):
        self.welcome_page = WelcomePage()
        self.kasta_page = KastaPage()
        self.widget = QtWidgets.QStackedWidget()
        self.widget.addWidget(self.welcome_page)
        self.widget.addWidget(self.kasta_page)
        self.widget.setFixedHeight(800)
        self.widget.setFixedWidth(1200)
        self.widget.show()
        self.welcome_page.getStartedButton.clicked.connect(self.go_to_kasta)

    def go_to_kasta(self):
        self.widget.setCurrentIndex(1)


class WorkerThread(QThread):
    def __init__(self):
        super().__init__()
        self.kasta = Kasta()

    def run(self):
        self.kasta.listen()












