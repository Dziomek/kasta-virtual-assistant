from PySide2 import QtCore
from PySide2.QtGui import (QColor)
from PySide2.QtWidgets import *
from GUI.ui_python_files.ui_register_page import Ui_Form

from DataBase.Connection import ConnectDatabase

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

    def register(self):
        firstName = self.ui.firstNameLabel.text()
        lastName = self.ui.lastNameLabel.text()
        email = self.ui.emailLabel.text()
        password = self.ui.passwordLabel.text()
        password2 = self.ui.password2Label.text()
        date = self.ui.dateEdit.text()

        token = '123-test'
        validAccount = 'not'

        if not (firstName and lastName and email and password and password2 and date):
            print('Nie wszystkie dane sa uzupelnione')
        else:
            if password == password2:

                # DATABASE CONNECTION
                connection = ConnectDatabase()
                if not connection.checkUserExists(email):

                    connection = ConnectDatabase() # tu powtarzam połączenie ponieważ ono się wcześniej zamyka i trzeba znów otworzyć więc
                    # to do optymalizacji
                    connection.insertRegisterData(firstName, lastName, email, password, date, token, validAccount)
                    print("registered")
                else:
                    print('Taki uzytkownik juz istnieje !')

            else:
                print('Hasla nie pasuja ')


        pass