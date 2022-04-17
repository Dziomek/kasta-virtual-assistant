import threading
from PySide2 import QtCore
from PySide2.QtCore import QThread
from PySide2.QtWidgets import *
from GUI.ui_python_files.ui_kasta_page import Ui_Form
from kasta.kasta_assistant import Kasta
import multiprocessing


class KastaPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ########
        self.is_end_clicked = False
        self.is_running = False  # to prevent clicking start button when Kasta in already running
        self.listening_thread = ListeningThread()
        self.ui.startButton.clicked.connect(self.begin)
        self.ui.endButton.clicked.connect(self.stop)
        self.text_changing_thread = threading.Thread(target=self.change_text)  # changing text live
        self.is_text_changing_thread_active = False
        # self.t1.start()

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def begin(self):
        if not self.is_running:
            self.listening_thread.start()
            if not self.is_text_changing_thread_active:
                self.text_changing_thread.start()

            self.is_running = True
            self.is_text_changing_thread_active = True

            ##self.listeningLabel.setText('listening...')

    def stop(self):
        if self.is_running:
            self.is_running = False
            self.listening_thread.terminate()
            self.listening_thread.kasta.stop_listening()

            ##self.listeningLabel.setText('')

    def change_text(self):
        while True:
            self.ui.emailLabel.setText(self.listening_thread.kasta.text)

            if self.is_end_clicked:
                break


class ListeningThread(QThread):
    def __init__(self):
        super().__init__()
        self.kasta = Kasta()

    def run(self):
        self.kasta.listen()
