from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import (QColor, QIcon)
from PySide2.QtWidgets import *
from GUI.ui_python_files.ui_login_page import Ui_Form
from DataBase.Connection import ConnectDatabase

import hashlib


class LoginPage(QDialog):
    def __init__(self):
        super(LoginPage, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # MAIN WINDOW LABEL
        # QtCore.QTimer.singleShot(1500, lambda: self.ui.label.setText("<strong>Działa</strong> elegancko"))
        # QtCore.QTimer.singleShot(1500, lambda: self.setStyleSheet("background-color: #222; color: #FFF"))

        # Buttons event
        #self.ui.loginButton.clicked.connect(self.login)
        # self.ui.registerButton.clicked.connect(self.showRegisterForm)

        self.ui.label_7.setPixmap('icons/kaastavector.png')

        ######
        self.logged_in = False
        self.validAccount = False
        self.connection = None

        self.name = ''
        self.email = '' # user data that will be passed to kasta page
        self.id = ''

        self.ui.exitButton.setIcon(QIcon('icons/x_icon.png'))
        self.ui.exitButton.clicked.connect(self.exit)

    def login(self):
        # get fields
        self.email = self.ui.emailLabel.text()
        password = self.ui.passwordLabel.text()

        if not self.email or not password:
            self.ui.errorLabel.setText('Missing fields. Please try again')
        else:
            # DATABASE CONNECTION
            self.connection = ConnectDatabase()

            # CHECKED HASH PASSWORD
            hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

            records = self.connection.loginAuthentication(self.email, hashedPassword)
            if records:
                self.name = self.connection.get_user_name(self.email)[0][0]
                self.id = self.connection.returnIdUser(self.email)[0][0]
                self.logged_in = True
                for record in records:
                    self.validAccount = record[7]
                    return self.email, self.name, self.id
            else:
                self.ui.errorLabel.setText("Wrong email or password. Please try again")

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()

    def exit(self):
        self.close()
