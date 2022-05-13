# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirmation_pagezKTvRx.ui'
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
        self.label.setGeometry(QRect(220, 50, 461, 361))
        self.label.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(250, 110, 411, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(220, 180, 461, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_4.setAlignment(Qt.AlignCenter)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 350, 461, 31))
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_5.setAlignment(Qt.AlignCenter)
        self.greenmarkLabel = QPushButton(self.widget)
        self.greenmarkLabel.setObjectName(u"greenmarkLabel")
        self.greenmarkLabel.setGeometry(QRect(400, 240, 101, 81))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.greenmarkLabel.setFont(font1)
        self.greenmarkLabel.setStyleSheet(u"QPushButton{\n"
"background-color: #2b3038;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../../icons/greenmark.png", QSize(), QIcon.Normal, QIcon.Off)
        self.greenmarkLabel.setIcon(icon)
        self.greenmarkLabel.setIconSize(QSize(100, 100))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:28pt;\">Account </span><span style=\" font-size:28pt; font-weight:600;\">confirmed</span></p><p><span style=\" font-size:28pt;\"><br/></span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">You've successfully confirmed your account</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:11pt;\">You will be taken to the login page in 5 seconds.</span></p></body></html>", None))
        self.greenmarkLabel.setText("")
    # retranslateUi

