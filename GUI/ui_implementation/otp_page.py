from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *

from DataBase.Connection import ConnectDatabase
from EmailService.emailService import MailService
from GUI.ui_implementation.main_page import MainPage
from GUI.ui_python_files.ui_otp import Ui_Otp
from GUI.ui_implementation.login_page import LoginPage
from EmailService.token import generateToken


class OtpPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Otp()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Button on action
        self.ui.sendAgainButton.clicked.connect(self.sendAgain)

        self.email_in_otp = ""
        self.result = ""
        self.is_confirmed = False

    def checkOTP(self):
        otpCode = self.ui.otpLabel.text()
        # metoda sprawdzająca poprawność i aktywująca konto
        # dodać w loginie, nadrzędny if który sprawdza czy konto jest valid

    def confirm_account(self):
        self.is_confirmed = False
        connection = ConnectDatabase()
        sql_select_query = "select token from Users where email='" + self.email_in_otp + "'"
        cursor = connection.cursor
        cursor.execute(sql_select_query)

        result = cursor.fetchall()
        if result:
            for record in result:
                result = record[0]

        print(result)
        print(self.ui.otpLabel.text())
        print(result == self.ui.otpLabel.text())
        if result == self.ui.otpLabel.text():
            self.is_confirmed = True
            print('confirmed')
            connection = ConnectDatabase()
            connection.updateValidationAccount(self.email_in_otp)

    def sendAgain(self):
        self.ui.infoLabel.setText('We have sent the new code again!')
        token = generateToken()
        # DATABASE CONNECTION
        connection = ConnectDatabase()
        connection.newOtpCode(self.email_in_otp, token)

        # SEND VERIFY EMAIL TO USER
        sendEmail = MailService()
        firstName = 'User'
        lastName = ''
        sendEmail.emailVerification(firstName, lastName, self.email_in_otp, token)

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()