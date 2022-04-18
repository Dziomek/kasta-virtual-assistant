from PySide2 import QtCore
from PySide2.QtGui import (QColor)
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
        self.ui.loginButton.clicked.connect(self.login)
        #self.ui.registerButton.clicked.connect(self.showRegisterForm)

        ######
        self.logged_in = False
        self.validAccount = False
        self.email = ''

    def login(self):

        # get fields
        self.email = self.ui.emailLabel.text()
        password = self.ui.passwordLabel.text()

        # if że puste pola
        if not self.email or not password:
            self.ui.errorLabel.setText('Missing fields. Please try again')
        else:
            # DATABASE CONNECTION
            connection = ConnectDatabase()

            # CHECKED HASH PASSWORD
            hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

            records = connection.loginAuthentication(self.email, hashedPassword)

            if records:
                self.logged_in = True
                for record in records:
                    self.validAccount = record[7]
            else:
                self.ui.errorLabel.setText("Wrong email or password. Please try again")


    '''def showRegisterForm(self):
        pass
    '''
