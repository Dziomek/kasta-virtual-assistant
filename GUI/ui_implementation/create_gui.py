from PySide2.QtCore import QThread
from GUI.ui_implementation.kasta_page import KastaPage
from GUI.ui_implementation.login_page import LoginPage
from GUI.ui_implementation.register_page import RegisterPage
from GUI.ui_implementation.splash import SplashScreen
from GUI.ui_implementation.otp_page import OtpPage
from PySide2 import QtWidgets
import threading


class CreateGui:
    def __init__(self):
        self.main_page = SplashScreen()
        self.register_page = RegisterPage()
        self.kasta_page = KastaPage()
        self.otp_page = OtpPage()
        self.main_page.login_page.ui.registerButton.clicked.connect(self.switch_to_registration_page)
        self.main_page.login_page.ui.loginButton.clicked.connect(self.switch_to_kasta_page)
        self.register_page.ui.backButton.clicked.connect(self.switch_back_to_login_page)
        self.register_page.ui.registerButton.clicked.connect(self.switch_to_otp_page)
        #metoda do zmiany okienka z register na otpPage
        self.otp_page.ui.loginButton.clicked.connect(self.otp_page.confirm_account)
        self.otp_page.ui.loginButton.clicked.connect(self.switch_from_otp_to_login)

    def switch_to_registration_page(self):
        self.main_page.login_page.close()
        self.register_page.ui.errorLabel.setText("")
        self.register_page.show()

    def switch_to_kasta_page(self):
        if self.main_page.login_page.logged_in:
            self.main_page.login_page.close()
            self.kasta_page.show()

    def switch_back_to_login_page(self):
        self.register_page.close()
        self.main_page.login_page.ui.errorLabel.setText("")
        self.main_page.login_page.show()

    def switch_to_otp_page(self):
        if self.register_page.successfully_registered:
            self.register_page.close()
            self.otp_page.email_in_otp = self.register_page.email
            self.otp_page.show()

    def switch_from_otp_to_login(self):
        if self.otp_page.is_confirmed:
            self.otp_page.close()
            self.main_page.login_page.show()
