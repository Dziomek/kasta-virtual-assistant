# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_applicationjYsPaR.ui'
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
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QSize(460, 100))
        self.frame.setStyleSheet(u"background-color: #20242a;\n"
"font: 10pt \"Arial\";\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 71, 16))
        self.label.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(310, 10, 111, 16))
        self.label_2.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(780, 10, 51, 41))
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QSize(30, 30))
        self.keyWordLabel = QLabel(self.frame)
        self.keyWordLabel.setObjectName(u"keyWordLabel")
        self.keyWordLabel.setGeometry(QRect(30, 50, 261, 31))
        self.urlLabel = QLabel(self.frame)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setGeometry(QRect(310, 50, 561, 31))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignTop)

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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Applications to open</p></body></html>", None))
        self.exitButton.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"key word", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"application url", None))
        self.deleteButton.setText("")
        self.keyWordLabel.setText(QCoreApplication.translate("Form", u"xdxdxdxdxddx", None))
        self.urlLabel.setText(QCoreApplication.translate("Form", u"xdxdxdxdxddx", None))
        self.refreshButton.setText("")
        self.addAppButton.setText("")
    # retranslateUi

