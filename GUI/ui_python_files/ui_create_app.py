# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_appDEmiyl.ui'
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
        Form.resize(774, 532)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 20, 661, 391))
        self.widget.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 661, 91))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(600, 10, 41, 41))
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
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 140, 113, 22))
        self.keywordTextEdit = QLineEdit(self.widget)
        self.keywordTextEdit.setObjectName(u"keywordTextEdit")
        self.keywordTextEdit.setGeometry(QRect(10, 160, 311, 40))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(9)
        self.keywordTextEdit.setFont(font1)
        self.keywordTextEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(340, 160, 311, 51))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(18)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: white;")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.urlTextEdit = QLineEdit(self.widget)
        self.urlTextEdit.setObjectName(u"urlTextEdit")
        self.urlTextEdit.setGeometry(QRect(10, 240, 311, 40))
        self.urlTextEdit.setFont(font1)
        self.urlTextEdit.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(340, 250, 311, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: white;")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(250, 320, 160, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(13)
        self.addButton.setFont(font3)
        self.addButton.setStyleSheet(u"QPushButton{\n"
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
        self.errorLabel = QLabel(self.widget)
        self.errorLabel.setObjectName(u"errorLabel")
        self.errorLabel.setGeometry(QRect(0, 100, 661, 20))
        self.errorLabel.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Add app to open</p><p><br/></p></body></html>", None))
        self.exitButton.setText("")
        self.keywordTextEdit.setText("")
        self.keywordTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"enter key word...", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">key word (ex. nutka1, moja stronka)</span></p></body></html>", None))
        self.urlTextEdit.setText("")
        self.urlTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"enter url...", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">url (ex. https://www.youtube.com/)</span></p><p><span style=\" font-size:11pt;\"><br/></span></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.errorLabel.setText("")
    # retranslateUi

