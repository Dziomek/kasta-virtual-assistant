from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *

from DataBase.Connection import ConnectDatabase
from GUI.ui_implementation.main_page import MainPage
from GUI.ui_python_files.ui_otp import Ui_Otp
from GUI.ui_implementation.login_page import LoginPage


class OtpPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Otp()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.email_in_otp = ""
        self.result = ""
        self.is_confirmed = False

    def checkOTP(self):
        otpCode = self.ui.otpLabel.text()
        # metoda sprawdzająca poprawność i aktywująca konto
        # dodać w loginie, nadrzędny if który sprawdza czy konto jest valid

    def confirm_account(self):
        connection = ConnectDatabase()
        sql_select_query = "select token from Users where email='" + self.email_in_otp + "'"
        cursor = connection.cursor
        cursor.execute(sql_select_query)
        result = cursor.fetchall()[0][0]

        print(result)
        print(self.ui.otpLabel.text())
        print(result == self.ui.otpLabel.text())
        if result == self.ui.otpLabel.text():
            self.is_confirmed = True
            print('confirmed')
            ###sql_select_query = "UPDATE Users SET validAccount='True' WHERE email='" + self.email_in_otp + "'"
            ###cursor.execute(sql_select_query)
