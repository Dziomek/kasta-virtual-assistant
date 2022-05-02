# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kasta_pageAzZDSU.ui'
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
        Form.resize(1400, 832)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 80, 1081, 711))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(90, 0, 951, 701))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label.setScaledContents(False)
        self.label.setWordWrap(False)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(180, 460, 781, 211))
        self.label_2.setStyleSheet(u"background-color: #20242a;\n"
"border-radius: 30px;")
        self.emailLabel = QLineEdit(self.widget)
        self.emailLabel.setObjectName(u"emailLabel")
        self.emailLabel.setGeometry(QRect(210, 490, 491, 40))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(9)
        self.emailLabel.setFont(font)
        self.emailLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.startButton = QPushButton(self.widget)
        self.startButton.setObjectName(u"startButton")
        self.startButton.setGeometry(QRect(730, 490, 191, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.startButton.setFont(font1)
        self.startButton.setStyleSheet(u"QPushButton{\n"
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
        self.label_title = QLabel(self.widget)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setGeometry(QRect(100, 0, 941, 141))
        font2 = QFont()
        font2.setFamily(u"Segoe UI")
        font2.setPointSize(40)
        self.label_title.setFont(font2)
        self.label_title.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_description = QLabel(self.widget)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setGeometry(QRect(90, 110, 951, 41))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(14)
        self.label_description.setFont(font3)
        self.label_description.setStyleSheet(u"color: #837c73")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.endButton = QPushButton(self.widget)
        self.endButton.setObjectName(u"endButton")
        self.endButton.setGeometry(QRect(730, 610, 191, 41))
        self.endButton.setFont(font1)
        self.endButton.setStyleSheet(u"QPushButton{\n"
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
        self.helpButton = QPushButton(self.widget)
        self.helpButton.setObjectName(u"helpButton")
        self.helpButton.setGeometry(QRect(840, 250, 81, 71))
        self.helpButton.setStyleSheet(u"QPushButton{\n"
"background-color: #2b3038;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../icons/help_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.helpButton.setIcon(icon)
        self.helpButton.setIconSize(QSize(100, 100))
        self.helpButton.setFlat(False)
        self.userEmailLabel = QLabel(self.widget)
        self.userEmailLabel.setObjectName(u"userEmailLabel")
        self.userEmailLabel.setGeometry(QRect(110, 20, 251, 16))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        self.userEmailLabel.setFont(font4)
        self.userEmailLabel.setStyleSheet(u"color: #837c73")
        self.userNameLabel = QLabel(self.widget)
        self.userNameLabel.setObjectName(u"userNameLabel")
        self.userNameLabel.setGeometry(QRect(110, 50, 131, 16))
        self.userNameLabel.setFont(font4)
        self.userNameLabel.setStyleSheet(u"color: #837c73")
        self.kastaLabel = QLabel(self.widget)
        self.kastaLabel.setObjectName(u"kastaLabel")
        self.kastaLabel.setGeometry(QRect(210, 600, 491, 51))
        self.kastaLabel.setStyleSheet(u"background-color: rgba(0,0,0,0);\n"
"border: 2px solid rgba(0,0,0,0);\n"
"border-bottom-color: #ff662b;\n"
"color: rgb(212, 192, 169);\n"
"paddinf-bottom: 7px;")
        self.kastaLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.kastaLabel.setWordWrap(True)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 170, 291, 281))
        self.label_3.setStyleSheet(u"background-image: url(:/nowyPrzedrostek/kaastavector.png);")
        self.label_3.setPixmap(QPixmap(u":/nowyPrzedrostek/kaastavector.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(False)
        self.label_description_3 = QLabel(self.widget)
        self.label_description_3.setObjectName(u"label_description_3")
        self.label_description_3.setGeometry(QRect(850, 330, 61, 41))
        self.label_description_3.setFont(font3)
        self.label_description_3.setStyleSheet(u"color: #837c73")
        self.label_description_3.setAlignment(Qt.AlignCenter)
        self.addCommandButton = QPushButton(self.widget)
        self.addCommandButton.setObjectName(u"addCommandButton")
        self.addCommandButton.setGeometry(QRect(100, 80, 141, 41))
        self.addCommandButton.setFont(font1)
        self.addCommandButton.setStyleSheet(u"QPushButton{\n"
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
        self.myCommandsButton = QPushButton(self.widget)
        self.myCommandsButton.setObjectName(u"myCommandsButton")
        self.myCommandsButton.setGeometry(QRect(260, 80, 141, 41))
        self.myCommandsButton.setFont(font1)
        self.myCommandsButton.setStyleSheet(u"QPushButton{\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText("")
        self.emailLabel.setPlaceholderText(QCoreApplication.translate("Form", u"listening...", None))
        self.startButton.setText(QCoreApplication.translate("Form", u"Start listening", None))
        self.label_title.setText(QCoreApplication.translate("Form", u"<strong>KASTA</strong> VA", None))
        self.label_description.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Virtual Assistant</span></p></body></html>", None))
        self.endButton.setText(QCoreApplication.translate("Form", u"Stop listening", None))
        self.helpButton.setText("")
        self.userEmailLabel.setText(QCoreApplication.translate("Form", u"xdxdxd", None))
        self.userNameLabel.setText(QCoreApplication.translate("Form", u"xdxdxd", None))
        self.kastaLabel.setText("")
        self.label_3.setText("")
        self.label_description_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">Helper</span></p><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.addCommandButton.setText(QCoreApplication.translate("Form", u"Add command", None))
        self.myCommandsButton.setText(QCoreApplication.translate("Form", u"My commands", None))
    # retranslateUi

