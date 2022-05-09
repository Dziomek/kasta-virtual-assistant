import threading
from PySide2 import QtCore
from PySide2.QtCore import QThread, QPoint, QTimer
from PySide2.QtGui import QIcon
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
        self.kasta_thread = KastaWorker()
        self.text_changing_thread = threading.Thread(target=self.change_text)  # changing text live
        self.ui.startButton.clicked.connect(self.kasta_thread.start)
        self.ui.startButton.clicked.connect(self.text_changing_thread.start)
        self.ui.startButton.clicked.connect(self.set_type_button_disabled)
        self.ui.startButton.clicked.connect(self.set_listen_button_disabled)


        self.ui.endButton.clicked.connect(self.kasta_thread.stop)
        self.ui.endButton.clicked.connect(self.set_listen_button_enabled)
        self.ui.endButton.clicked.connect(self.set_type_button_enabled)
        self.ui.startButton.clicked.connect(self.set_parameters)

        self.ui.enterCommandButton.clicked.connect(self.text_changing_thread.start)
        self.ui.enterCommandButton.clicked.connect(self.take_typed_command)
        self.ui.enterCommandButton.clicked.connect(self.kasta_thread.kasta.do_typed_command)

        # self.t1.start()

        self.ui.label_3.setPixmap("icons/kaastavector.png")
        self.ui.helpButton.setIcon(QIcon("icons/help_icon.png"))

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.user_email = ''

        self.command_typed = False
        self.command_listened = False

    def set_parameters(self):
        self.command_typed = False
        self.ui.typeTextEdit.setText('')
        print(self.command_typed)

    def set_type_button_disabled(self):
        self.ui.enterCommandButton.setEnabled(False)

    def set_type_button_enabled(self):
        self.ui.enterCommandButton.setDisabled(False)

    def set_listen_button_disabled(self):
        if not self.kasta_thread.kasta.is_speaking:
            self.ui.startButton.setEnabled(False)

    def set_listen_button_enabled(self):
        if not self.kasta_thread.kasta.is_speaking:
            if not self.kasta_thread.kasta.is_action_performed:
                self.ui.startButton.setDisabled(False)

    def change_text(self):
        self.ui.enterCommandButton.clicked.disconnect(self.text_changing_thread.start)
        self.ui.startButton.clicked.disconnect(self.text_changing_thread.start)
        while True:
            if not self.command_typed:
                self.ui.emailLabel.setText(self.kasta_thread.kasta.text)
            self.ui.kastaLabel.setText(self.kasta_thread.kasta.response)
            if self.kasta_thread.kasta.is_listening:
                self.ui.listeningLabel.setText('listening...')
            else:
                self.ui.listeningLabel.setText('')

    def take_typed_command(self):
        if not self.kasta_thread.kasta.is_listening and not self.kasta_thread.kasta.is_speaking:
            self.command_typed = True
            self.kasta_thread.kasta.text = self.ui.typeTextEdit.text()
            print(self.kasta_thread.kasta.text)
            print(self.command_typed)

    #########################################


    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()

