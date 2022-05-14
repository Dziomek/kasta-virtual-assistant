from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from DataBase.Connection import ConnectDatabase
from GUI.ui_python_files.ui_add_note import Ui_Form


class AddNotePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))
        self.ui.addButton.clicked.connect(self.add_note_to_database)

        self.user_id = 0

    def add_note_to_database(self):
        if self.ui.noteTextEdit.text():
            note_text = self.ui.noteTextEdit.text()
            connection = ConnectDatabase()
            connection.insertNote('', note_text, self.user_id)
            print(note_text + ' added successfully')
            self.ui.noteTextEdit.setText('')
            self.ui.errorLabel.setStyleSheet(u"color: rgb(4, 136, 63);")
            self.ui.errorLabel.setText('Note added successfully')
            return note_text
        else:
            self.ui.errorLabel.setStyleSheet(u"color: red;")
            self.ui.errorLabel.setText('Please insert text of your note')

    def exit(self):
        self.close()

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()