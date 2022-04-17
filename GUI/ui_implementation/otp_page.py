from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
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


    def checkOTP(self):
        otpCode = self.ui.otpLabel.text()
        #metoda sprawdzająca poprawność i aktywująca konto
        # dodać w loginie, nadrzędny if który sprawdza czy konto jest valid