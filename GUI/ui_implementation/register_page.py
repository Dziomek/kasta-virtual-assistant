from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
from GUI.ui_python_files.ui_register_page import Ui_Form

from DataBase.Connection import ConnectDatabase
from EmailService.emailService import MailService

from EmailService.token import generateToken

import hashlib



class RegisterPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Buttons event
        self.ui.registerButton.clicked.connect(self.register)

        self.email = ''
        self.hashedPassword = ''
        self.successfully_registered = False

    def register(self):
        firstName = self.ui.firstNameLabel.text()
        lastName = self.ui.lastNameLabel.text()
        self.email = self.ui.emailLabel.text()
        password = self.ui.passwordLabel.text()
        password2 = self.ui.password2Label.text()
        date = self.ui.dateEdit.text()


        # GENERATE TOKEN

        token = generateToken()
        validAccount = 'False'

        valid_email = False

        if not (firstName and lastName and self.email and password and password2 and date):
            self.ui.errorLabel.setText('Missing fields. Please try again.')
        else:
            if '@' not in self.email:
                self.ui.errorLabel.setText('Invalid email. Please try again.')
            else:
                parts = self.email.split('@', 2)
                if '.' in parts[1] and parts[1].index('.') != 0:
                    valid_email = True
                else:
                    self.ui.errorLabel.setText('Invalid email. Please try again.')

                if valid_email:
                    if len(password) < 8:
                        self.ui.errorLabel.setText('Password should contain at least 8 characters.')
                    else:
                        if password == password2:

                            #GENERATE HASHED PASSWORD
                            self.hashedPassword = hashlib.sha256(password.encode('utf-8')).hexdigest()

                            # DATABASE CONNECTION
                            connection = ConnectDatabase()
                            if not connection.checkUserExists(self.email):

                                connection = ConnectDatabase()  # tu powtarzam połączenie ponieważ ono się wcześniej zamyka i trzeba znów otworzyć więc
                                # to do optymalizacji
                                connection.insertRegisterData(firstName, lastName, self.email, self.hashedPassword , date, token,
                                                              validAccount)
                                self.ui.errorLabel.setText('Registered.')
                                self.successfully_registered = True
                                #SEND VERIFY EMAIL TO USER
                                sendEmail = MailService()
                                sendEmail.emailVerification(firstName, lastName, self.email, token)

                            else:
                                self.ui.errorLabel.setText('User with this email already exists.')

                        else:
                            self.ui.errorLabel.setText('Invalid password confirmation. Please try again.')
