# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_applicationKyQZlJ.ui'
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
        Form.resize(1106, 873)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(120, 50, 911, 451))
        self.widget.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 10, 911, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(850, 10, 41, 41))
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
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 110, 911, 221))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 911, 221))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.refreshButton = QPushButton(self.widget)
        self.refreshButton.setObjectName(u"refreshButton")
        self.refreshButton.setGeometry(QRect(100, 360, 61, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.refreshButton.setFont(font1)
        self.refreshButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.refreshButton.setIcon(icon1)
        self.refreshButton.setIconSize(QSize(70, 70))
        self.refreshButton.setFlat(False)
        self.addAppButton = QPushButton(self.widget)
        self.addAppButton.setObjectName(u"addAppButton")
        self.addAppButton.setGeometry(QRect(30, 360, 61, 61))
        self.addAppButton.setFont(font1)
        self.addAppButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../icons/plus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addAppButton.setIcon(icon2)
        self.addAppButton.setIconSize(QSize(70, 70))
        self.addAppButton.setFlat(False)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(560, 380, 121, 41))
        font2 = QFont()
        font2.setPointSize(14)
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(660, 380, 51, 41))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(720, 380, 101, 41))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: white;")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Applications to open</p></body></html>", None))
        self.exitButton.setText("")
        self.refreshButton.setText("")
        self.addAppButton.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"SYNTAX:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"open", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"key word", None))
    # retranslateUi

