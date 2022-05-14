# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'otpdwOztV.ui'
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
        Form.resize(1050, 730)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 70, 871, 611))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(220, 50, 461, 521))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 230, 321, 261))
        self.label_2.setStyleSheet(u"background-color: #20242a;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 110, 401, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.otpLabel = QLineEdit(self.widget)
        self.otpLabel.setObjectName(u"otpLabel")
        self.otpLabel.setGeometry(QRect(320, 310, 260, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.otpLabel.setFont(font1)
        self.otpLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.otpLabel.setAlignment(Qt.AlignCenter)
        self.loginButton = QPushButton(self.widget)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setGeometry(QRect(350, 380, 191, 41))
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
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 190, 401, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.sendAgainButton = QPushButton(self.widget)
        self.sendAgainButton.setObjectName(u"sendAgainButton")
        self.sendAgainButton.setGeometry(QRect(310, 450, 291, 28))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(8)
        self.sendAgainButton.setFont(font3)
        self.sendAgainButton.setLayoutDirection(Qt.RightToLeft)
        self.sendAgainButton.setStyleSheet(u"background-color: transparent;\n"
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
        self.infoLabel = QLabel(self.widget)
        self.infoLabel.setObjectName(u"infoLabel")
        self.infoLabel.setGeometry(QRect(300, 250, 301, 20))
        self.infoLabel.setStyleSheet(u"color: red;")
        self.infoLabel.setAlignment(Qt.AlignCenter)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(620, 60, 41, 41))
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
        self.label.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<strong>ENTER </strong>OTP", None))
        self.otpLabel.setPlaceholderText(QCoreApplication.translate("Form", u"Unique six-digits code", None))
        self.loginButton.setText(QCoreApplication.translate("Form", u"Go to Log In", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:8pt;\">Check your email, there is a unique code, enter it below</span></p></body></html>", None))
        self.sendAgainButton.setText(QCoreApplication.translate("Form", u"Did you get the code? Click here to send again.", None))
        self.infoLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
        self.exitButton.setText("")
    # retranslateUi

