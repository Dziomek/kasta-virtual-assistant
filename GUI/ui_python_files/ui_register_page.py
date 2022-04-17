# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_pageuMcRGl.ui'
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


class Ui_Form(object):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(965, 806)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 20, 831, 761))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 751, 721))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 70, 491, 651))
        self.label_2.setStyleSheet(u"background-color: #20242a;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 100, 751, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.lastNameLabel = QLineEdit(self.widget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(280, 300, 260, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.lastNameLabel.setFont(font1)
        self.lastNameLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.passwordLabel = QLineEdit(self.widget)
        self.passwordLabel.setObjectName(u"passwordLabel")
        self.passwordLabel.setGeometry(QRect(280, 440, 260, 40))
        self.passwordLabel.setFont(font1)
        self.passwordLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.passwordLabel.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.registerButton = QPushButton(self.widget)
        self.registerButton.setObjectName(u"registerButton")
        self.registerButton.setGeometry(QRect(310, 640, 201, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
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
"}\n"
"")
        self.firstNameLabel = QLineEdit(self.widget)
        self.firstNameLabel.setObjectName(u"firstNameLabel")
        self.firstNameLabel.setGeometry(QRect(280, 230, 260, 40))
        self.firstNameLabel.setFont(font1)
        self.firstNameLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.emailLabel = QLineEdit(self.widget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(280, 370, 260, 40))
        self.emailLabel.setFont(font1)
        self.emailLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.password2Label = QLineEdit(self.widget)
        self.password2Label.setObjectName(u"password2Label")
        self.password2Label.setGeometry(QRect(280, 510, 260, 40))
        self.password2Label.setFont(font1)
        self.password2Label.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.password2Label.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.dateEdit = QDateEdit(self.widget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(280, 580, 261, 21))
        self.dateEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(170, 190, 491, 20))
        self.errorLabel.setStyleSheet(u"color: red;")
        self.errorLabel.setAlignment(Qt.AlignCenter)
        self.backButton = QPushButton(self.widget)
        self.backButton.setObjectName(u"backButton")
        self.backButton.setGeometry(QRect(560, 640, 51, 41))
        self.backButton.setFont(font2)
        self.backButton.setStyleSheet(u"QPushButton{\n"
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
"}\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<strong>REGISTER</strong>", None))
        self.lastNameLabel.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.passwordLabel.setPlaceholderText(QCoreApplication.translate("Form", u"Passoword", None))
        self.registerButton.setText(QCoreApplication.translate("Form", u"Register Now", None))
        self.firstNameLabel.setPlaceholderText(QCoreApplication.translate("Form", u"Frist Name", None))
        self.emailLabel.setPlaceholderText(QCoreApplication.translate("Form", u"email", None))
        self.password2Label.setPlaceholderText(QCoreApplication.translate("Form", u"Confirm Password", None))
        self.errorLabel.setText("")
        self.backButton.setText(QCoreApplication.translate("Form", u"Back", None))
    # retranslateUi

