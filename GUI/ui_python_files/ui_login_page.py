# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_pageatFLWH.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

#import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(882, 667)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 30, 871, 611))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 30, 461, 521))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 321, 521))
        self.label_2.setStyleSheet(u"background-color: #20242a;\n"
"border-radius: 30px;")
        self.label_2.setScaledContents(False)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 80, 401, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.emailLabel = QLineEdit(self.widget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(420, 220, 260, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.emailLabel.setFont(font1)
        self.emailLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.passwordLabel = QLineEdit(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(420, 290, 260, 40))
        self.passwordLabel.setFont(font1)
        self.passwordLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.passwordLabel.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(450, 380, 191, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
        self.loginButton.setFont(font2)
        self.loginButton.setStyleSheet(u"QPushButton{\n"
"background-color:  rgb(212, 192, 169);\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #837c73;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"background-color: #ff662b;;\n"
"}")
        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(470, 470, 151, 31))
        self.registerButton.setFont(font2)
        self.registerButton.setStyleSheet(u"QPushButton{\n"
"background-color:  rgb(212, 192, 169);\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #837c73;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"background-color: #ff662b;;\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(350, 440, 401, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(360, 190, 401, 20))
        self.errorLabel.setStyleSheet(u"color: red;")
        self.errorLabel.setAlignment(Qt.AlignCenter)
        self.verifyButton = QPushButton(self.widget)
        self.verifyButton.setObjectName(u"verifyButton")
        self.verifyButton.setGeometry(QRect(360, 180, 401, 21))
        self.verifyButton.setStyleSheet(u"background-color: transparent;\n"
"color: red;\n"
"\n"
"QPushButton{\n"
"background-color:  transparent;\n"
"color: red;;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c40808;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"background-color: #ff662b;;\n"
"}")
        self.forgotPasswordButton = QPushButton(self.widget)
        self.forgotPasswordButton.setObjectName(u"forgotPasswordButton")
        self.forgotPasswordButton.setGeometry(QRect(420, 330, 121, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(8)
        self.forgotPasswordButton.setFont(font3)
        self.forgotPasswordButton.setLayoutDirection(Qt.RightToLeft)
        self.forgotPasswordButton.setStyleSheet(u"background-color: transparent;\n"
"color: rgb(212, 192, 169);\n"
"\n"
"QPushButton{\n"
"background-color:  transparent;\n"
"color: rgb(212, 192, 169);\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: #c40808;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"padding-left: 5px;\n"
"padding-right: 5px;\n"
"background-position: calc(100% - 10px)center;\n"
"background-color: #ff662b;;\n"
"}")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setEnabled(True)
        self.label_5.setGeometry(QRect(50, 310, 301, 71))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: #272c34;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setEnabled(True)
        self.label_6.setGeometry(QRect(50, 380, 301, 41))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(21)
        self.label_6.setFont(font4)
        self.label_6.setStyleSheet(u"color: #272c34;")
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(100, 80, 201, 201))
        self.label_7.setStyleSheet(u"background-image: url(:/logo/kaastavector.png);")
        self.label_7.setPixmap(QPixmap(u"../../icons/kaastavector.png"))
        self.label_7.setScaledContents(True)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(700, 40, 41, 41))
        self.exitButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../icons/x_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QSize(30, 30))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<strong>LOG </strong>IN", None))
        self.emailLabel.setPlaceholderText(QCoreApplication.translate("Form", u"email", None))
        self.passwordLabel.setPlaceholderText(QCoreApplication.translate("Form", u"password", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.registerButton.setText(QCoreApplication.translate("Form", u"Register Now", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:9pt;\">You don't have an account ?</span></p></body></html>", None))
        self.errorLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.verifyButton.setText("")
        self.forgotPasswordButton.setText(QCoreApplication.translate("Form", u"Forgot password?", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<strong>KASTA </strong>VA", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Virtual Assistant</p></body></html>", None))
        self.label_7.setText("")
        self.exitButton.setText("")
    # retranslateUi

