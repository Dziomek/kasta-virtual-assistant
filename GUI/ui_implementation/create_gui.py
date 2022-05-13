import time

from PySide2.QtCore import QThread

from GUI.ui_implementation.faq import FAQPage
from GUI.ui_implementation.kasta_page import KastaPage
from GUI.ui_implementation.login_page import LoginPage
from GUI.ui_implementation.notes_page import MyNotesPage
from GUI.ui_implementation.register_page import RegisterPage
from GUI.ui_implementation.splash import SplashScreen
from GUI.ui_implementation.otp_page import OtpPage
from GUI.ui_implementation.confirmation_page import ConfirmationPage
from PySide2 import QtWidgets, QtCore
import threading


class CreateGui:
    def __init__(self):
        self.main_page = SplashScreen()
        self.register_page = RegisterPage()
        self.kasta_page = KastaPage()
        self.otp_page = OtpPage()
        self.confirmation_page = ConfirmationPage()
        self.faq_page = FAQPage()
        self.my_notes_page = MyNotesPage()
        self.main_page.login_page.ui.registerButton.clicked.connect(self.login_to_register)
        self.main_page.login_page.ui.loginButton.clicked.connect(self.login_to_kasta_or_otp)
        #self.main_page.login_page.ui.loginButton.clicked.connect(self.login_to_otp)
        self.register_page.ui.backButton.clicked.connect(self.register_to_login)
        self.register_page.ui.registerButton.clicked.connect(self.register_to_otp)
        #metoda do zmiany okienka z register na otpPage
        self.otp_page.ui.loginButton.clicked.connect(self.otp_page.confirm_account)
        self.otp_page.ui.loginButton.clicked.connect(self.otp_to_login)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.confirmation_to_login)
        self.kasta_page.ui.helpButton.clicked.connect(self.kasta_to_faq)


    def empty_text_fields(self):
        self.register_page.ui.errorLabel.setText('')
        self.register_page.ui.firstNameLabel.setText('')
        self.register_page.ui.lastNameLabel.setText('')
        self.register_page.ui.firstNameLabel.setText('')
        self.register_page.ui.emailLabel.setText('')
        self.register_page.ui.passwordLabel.setText('')
        self.register_page.ui.password2Label.setText('')
        ##
        self.main_page.login_page.ui.emailLabel.setText('')
        self.main_page.login_page.ui.passwordLabel.setText('')

    def empty_error_labels(self):
        self.register_page.ui.errorLabel.setText('')
        self.main_page.login_page.ui.errorLabel.setText('')

    def empty_otp_field(self):
        self.otp_page.ui.otpLabel.setText('')

    #######################################################

    def login_to_register(self):
        self.main_page.login_page.close()
        self.register_page.show()
        ##
        self.empty_error_labels()
        self.empty_text_fields()

    def login_to_kasta_or_otp(self):
        data = self.main_page.login_page.login()
        if self.main_page.login_page.logged_in and self.main_page.login_page.validAccount == 'True':
            self.kasta_page.kasta_thread.kasta.user_email = data[0]
            self.kasta_page.kasta_thread.kasta.user_name = data[1]
            self.kasta_page.kasta_thread.kasta.user_id = data[2]
            self.kasta_page.ui.userEmailLabel.setText(data[0])
            self.kasta_page.ui.userNameLabel.setText(data[1])
            print(self.kasta_page.kasta_thread.kasta.user_email, self.kasta_page.kasta_thread.kasta.user_name)
            self.main_page.login_page.close()
            self.kasta_page.show()

        elif self.main_page.login_page.logged_in and self.main_page.login_page.validAccount == 'False':
            self.otp_page.email_in_otp = self.main_page.login_page.email  # PRZEKAZANIE MAILA
            self.main_page.login_page.close()
            self.otp_page.show()

    '''def login_to_otp(self):
        if self.main_page.login_page.logged_in and self.main_page.login_page.validAccount == 'False':
            self.otp_page.email_in_otp = self.main_page.login_page.email # PRZEKAZANIE MAILA
            self.main_page.login_page.close()
            self.otp_page.show()
    '''

    def register_to_login(self):
        self.register_page.close()
        self.main_page.login_page.show()
        ##
        self.empty_error_labels()
        self.empty_text_fields()

    def register_to_otp(self):
        if self.register_page.successfully_registered:
            self.register_page.close()
            self.otp_page.email_in_otp = self.register_page.email # PRZEKAZANIE MAILA
            self.otp_page.show()

    def confirmation_to_login(self):
        self.confirmation_page.close()
        self.main_page.login_page.show()
        self.confirmation_page.close()
        self.main_page.login_page.show()
        ##
        self.empty_error_labels()
        self.empty_text_fields()
        self.empty_otp_field()
        self.timer.stop()

    def otp_to_login(self):
        if self.otp_page.is_confirmed:
            self.otp_page.close()
            self.confirmation_page.show()
            self.timer.start(5000)

    def kasta_to_faq(self):
        self.faq_page.show()

    def kasta_to_notes(self):
        self.my_notes_page.show()





