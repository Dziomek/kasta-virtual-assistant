import threading
from PySide2 import QtCore
from PySide2.QtCore import QThread, QPoint
from PySide2.QtWidgets import *
from GUI.ui_python_files.ui_kasta_page import Ui_Form
from kasta.kasta_assistant import Kasta, KastaWorker
import multiprocessing


class KastaPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        ########
        # to prevent clicking start button when Kasta in already running
        self.listening_thread = KastaWorker()
        self.text_changing_thread = threading.Thread(target=self.change_text)  # changing text live
        self.ui.startButton.clicked.connect(self.listening_thread.start)
        self.ui.startButton.clicked.connect(self.text_changing_thread.start)
        self.ui.endButton.clicked.connect(self.listening_thread.stop)
        
        # self.t1.start()

        self.ui.label_3.setPixmap("icons/kaastavector.png")

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.user_email = ''

    def change_text(self):
        self.ui.startButton.clicked.disconnect(self.text_changing_thread.start)
        while True:
            self.ui.emailLabel.setText(self.listening_thread.kasta.text)
            self.ui.kastaLabel.setText(self.listening_thread.kasta.response)

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()

