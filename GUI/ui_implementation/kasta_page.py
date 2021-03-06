import os
import sys
import threading
from PySide2 import QtCore
from PySide2.QtCore import QThread, QPoint, QTimer
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import *
from functools import partial
from DataBase.Connection import ConnectDatabase
from GUI.ui_implementation.add_application_page import AddApplicationPage
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
        self.add_app_page = AddApplicationPage()


        self.ui.endButton.clicked.connect(self.kasta_thread.stop)
        self.ui.endButton.clicked.connect(self.set_listen_button_enabled)
        self.ui.endButton.clicked.connect(self.set_type_button_enabled)
        self.ui.startButton.clicked.connect(self.set_parameters)

        self.ui.enterCommandButton.clicked.connect(self.text_changing_thread.start)
        self.ui.enterCommandButton.clicked.connect(self.take_typed_command)
        self.ui.enterCommandButton.clicked.connect(self.kasta_thread.kasta.do_typed_command)

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.openAppButton.clicked.connect(self.open_app_page)

        # self.t1.start()

        self.ui.label_3.setPixmap("icons/kaastavector.png")
        self.ui.helpButton.setIcon(QIcon("icons/question_mark.png"))
        self.ui.myNotesButton.setIcon(QIcon("icons/note.png"))
        self.ui.keyboardLabel.setIcon(QIcon("icons/keyboardicon.png"))
        self.ui.speakerIcon.setIcon(QIcon("icons/speaker.png"))
        self.ui.assistantLabel.setIcon(QIcon("icons/assistant_icon.png"))
        self.ui.openAppButton.setIcon(QIcon("icons/website.png"))
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))
        self.ui.logoutButton.setIcon(QIcon("icons/logout.png"))

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.command_typed = False
        self.command_listened = False

        self.ui.myNotesButton.clicked.connect(self.switch_to_notes)
        self.old_position = None # FIX

    def open_app_page(self):
        self.add_app_page = AddApplicationPage()
        self.add_app_page.create_app_page.ui.addButton.clicked.connect(self.kasta_thread.kasta.get_open_commands_from_db)
        self.add_app_page.ui.refreshButton.clicked.connect(self.refresh_commands)
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.kasta_thread.kasta.user_email)[0][0]
        self.add_app_page.user_id = idUsers
        print(self.add_app_page.user_id)
        commands = connection.get_commands(idUsers)

        #print(commands)
        #print(len(commands))
        if len(commands) > 0:
            buttons = []
            for x in range(len(commands)):
                key_word = commands[x][0]
                url = commands[x][1]
                command_id = connection.get_id_command(key_word)[0][0]
                #print('keyword: ' + key_word)
                #print('url: ' + url)
                #print('command id: ' + str(command_id))

                buttons.append(self.add_app_page.add_application_widget(x, key_word, url))
                buttons[x].clicked.connect(partial(connection.delete_command_with_id, command_id))
                buttons[x].clicked.connect(self.kasta_thread.kasta.get_open_commands_from_db)
                #buttons[x].clicked.connect(self.pass_apps)
                buttons[x].clicked.connect(self.open_app_page)
        else:
            self.add_app_page.create_no_app_label()
        self.add_app_page.show()

    '''def pass_apps(self):
        self.kasta_thread.kasta.apps = self.add_app_page.apps
        '''

    def switch_to_notes(self):
        self.my_notes = MyNotesPage()
        self.my_notes.ui.refreshButton.clicked.connect(self.refresh_notes)
        connection = ConnectDatabase()
        idUsers = connection.returnIdUser(self.kasta_thread.kasta.user_email)[0][0]
        self.my_notes.user_id = idUsers
        print(self.my_notes.user_id)
        notes = connection.get_notes(idUsers)
        #print('number of notes:' + str(len(notes)))
        #print('user id:' + str(idUsers))
        if len(notes) > 0:
            if len(notes) % 2 == 0:
                row_number = int(len(notes)/2)
            else:
                row_number = int(len(notes)/2) + 1

            #print('number of rows:' + str(row_number))
            note_number = 0 ## current number of note
            buttons = []
            id_notes = []
            for x in range(row_number):
                for y in range(2):
                    if note_number == len(notes):
                        break
                    else:
                        note_id = connection.get_id_note(notes[note_number][0])[0][0]
                        #print('Note id: ' + str(note_id))
                        #print('Note number: ' + str(note_number))

                        buttons.append(self.my_notes.create_new_widget(x, y, notes[note_number][0], note_id)) ## ostatni numer to id notatki
                        buttons[note_number].clicked.connect(partial(connection.delete_note_with_id, note_id))
                        buttons[note_number].clicked.connect(self.my_notes.close)

                        buttons[note_number].clicked.connect(self.switch_to_notes)
                        #print('Added action to ' + buttons[note_number].objectName() + ' ' + 'delete note ' + str(note_id))
                        #print('list_len: ' + str(len(buttons)))
                        #print('created note ' + str(note_number))
                        #print(note_id)

                        #buttons[note_number].setText(buttons[note_number].objectName())
                        #print('Dodano: ' + buttons[note_number].objectName())
                        note_number += 1
        else:
            self.my_notes.create_no_notes_frame()
        self.my_notes.show()

    def refresh_notes(self):
        self.my_notes.close()
        self.switch_to_notes()

    def refresh_commands(self):
        self.add_app_page.close()
        self.open_app_page()

    def set_parameters(self):
        if not self.kasta_thread.kasta.is_action_performed:
            self.command_typed = False
            self.ui.typeTextEdit.setText('')
            print(self.command_typed)

    def set_type_button_disabled(self):
        if not self.kasta_thread.kasta.is_action_performed:
            self.ui.enterCommandButton.setEnabled(False)

    def set_type_button_enabled(self):
        if not self.kasta_thread.kasta.is_speaking:
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


    #TODO:
    def exit(self):
        if not self.kasta_thread.kasta.is_speaking and not self.kasta_thread.kasta.is_action_performed:
            #self.kasta_thread.kasta.terminate_kasta()
            self.close()
            exit(0)

        #self.kasta_thread.terminate()
        #self.close()

    def logout(self):
        pass
