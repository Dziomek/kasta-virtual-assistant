import threading
from PySide2 import QtCore
from PySide2.QtCore import QThread, QPoint, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *

from DataBase.Connection import ConnectDatabase
from GUI.ui_implementation.faq import FAQPage
from GUI.ui_implementation.notes_page import MyNotesPage
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
        self.my_notes = MyNotesPage()


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
        self.ui.keyboardLabel.setIcon(QIcon("icons/keyboardicon.png"))
        self.ui.speakerIcon.setIcon(QIcon("icons/speaker.png"))

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.command_typed = False
        self.command_listened = False

        self.ui.myNotesButton.clicked.connect(self.switch_to_notes)

        self.old_position = None # FIX

    def switch_to_notes(self):
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.kasta_thread.kasta.user_email)[0][0]
        notes = connection.get_notes(idUsers)
        print(notes[1][0])
        print('number of notes:' + str(len(notes)))
        print('user id:' + str(idUsers))
        if len(notes) % 2 == 0:
            row_number = int(len(notes)/2)
        else:
            row_number = int(len(notes)/2) + 1

        print('number of rows:' + str(row_number))
        note_number = 0 ## current number of note
        for x in range(row_number):
            for y in range(2):
                if note_number == len(notes):
                    break
                else:
                    self.my_notes.create_new_widget(x, y, notes[note_number][0])
                    print('created note ' + str(note_number))
                    note_number += 1
        self.my_notes.show()

    def set_parameters(self):
        if not self.kasta_thread.kasta.is_action_performed:
            self.command_typed = False
            self.ui.typeTextEdit.setText('')
            print(self.command_typed)

    def set_type_button_disabled(self):
        if not self.kasta_thread.kasta.is_action_performed:
            self.ui.enterCommandButton.setEnabled(False)

    def set_type_button_enabled(self):
        self.ui.enterCommandButton.setDisabled(False)

    def set_listen_button_disabled(self):
        if not self.kasta_thread.kasta.is_speaking:
            if not self.kasta_thread.kasta.is_action_performed:
                self.ui.startButton.setEnabled(False)


    def set_listen_button_enabled(self):
        if not self.kasta_thread.kasta.is_speaking:
            if not self.kasta_thread.kasta.is_listening:
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
        if not self.kasta_thread.kasta.is_listening:
            if not self.kasta_thread.kasta.is_speaking:
                if not self.kasta_thread.kasta.is_action_performed:
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

