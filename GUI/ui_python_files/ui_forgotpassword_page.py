# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forgotpassword_pageWEhsSZ.ui'
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
        Form.resize(932, 716)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 60, 871, 611))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(250, 30, 511, 521))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 30, 321, 521))
        self.label_2.setStyleSheet(u"background-color: #20242a;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(360, 40, 391, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(30)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.emailLabel = QLineEdit(self.widget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(420, 300, 260, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.emailLabel.setFont(font1)
        self.emailLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.resetButton = QPushButton(self.widget)
        self.resetButton.setObjectName(u"resetButton")
        self.resetButton.setGeometry(QRect(450, 390, 191, 41))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(13)
        self.resetButton.setFont(font2)
        self.resetButton.setStyleSheet(u"QPushButton{\n"
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
        self.label_4.setGeometry(QRect(360, 190, 401, 71))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(34)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.backToLoginButton = QPushButton(self.widget)
        self.backToLoginButton.setObjectName(u"backToLoginButton")
        self.backToLoginButton.setGeometry(QRect(620, 490, 121, 28))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(8)
        self.backToLoginButton.setFont(font4)
        self.backToLoginButton.setLayoutDirection(Qt.RightToLeft)
        self.backToLoginButton.setStyleSheet(u"background-color: transparent;\n"
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
        self.label_5.setGeometry(QRect(360, 90, 391, 81))
        font5 = QFont()
        font5.setFamily(u"Segoe UI")
        font5.setPointSize(20)
        self.label_5.setFont(font5)
        self.label_5.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">FORGOT</span></p></body></html>", None))
        self.emailLabel.setPlaceholderText(QCoreApplication.translate("Form", u"email", None))
        self.resetButton.setText(QCoreApplication.translate("Form", u"Reset Password", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Enter your e-mail address, if we have it in the system,</span></p><p align=\"center\"><span style=\" font-size:8pt;\"> we will send you a link to change your password.</span></p></body></html>", None))
        self.backToLoginButton.setText(QCoreApplication.translate("Form", u"Back to login", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>your <span style=\" font-weight:600;\">password</span></p></body></html>", None))
    # retranslateUi

