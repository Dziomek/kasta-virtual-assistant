from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from DataBase.Connection import ConnectDatabase
from GUI.ui_python_files.ui_create_app import Ui_Form


class CreateAppPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))
        self.ui.addButton.clicked.connect(self.add_app_to_database)

        self.user_id = 0

    def add_app_to_database(self):
        if self.ui.keywordTextEdit.text() and self.ui.urlTextEdit.text():
            connection = ConnectDatabase()
            connection.insert_app(self.ui.keywordTextEdit.text(), self.ui.urlTextEdit.text(), self.user_id)
            #print(f'Added successfully')
            self.ui.keywordTextEdit.setText('')
            self.ui.urlTextEdit.setText('')
            self.ui.errorLabel.setStyleSheet(u"color: rgb(4, 136, 63);")
            self.ui.errorLabel.setText('Application added successfully')
        else:
            self.ui.errorLabel.setStyleSheet(u"color: red;")
            self.ui.errorLabel.setText('Missing fields. Please try again')

    def exit(self):
        self.close()
        self.ui.urlTextEdit.setText('')
        self.ui.keywordTextEdit.setText('')
        self.ui.errorLabel.setText('')

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()