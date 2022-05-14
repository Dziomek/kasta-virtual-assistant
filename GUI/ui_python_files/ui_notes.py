# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notesSftMJy.ui'
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
        Form.resize(1082, 851)
        Form.setMinimumSize(QSize(1000, 500))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 70, 1000, 651))
        self.widget.setMinimumSize(QSize(1000, 500))
        self.widget.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 981, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(34)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 100, 1000, 450))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 450))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(460, 200))
        self.frame.setStyleSheet(u"background-color: #20242a;\n"
"font: 10pt \"Arial\";\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 49, 460, 151))
        self.label.setStyleSheet(u"padding: 10px")
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(410, 10, 31, 28))
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../icons/x_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deleteButton.setIcon(icon)
        self.deleteButton.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(930, 20, 41, 41))
        self.exitButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        self.exitButton.setIcon(icon)
        self.exitButton.setIconSize(QSize(30, 30))
        self.addNoteButton = QPushButton(self.widget)
        self.addNoteButton.setObjectName(u"addNoteButton")
        self.addNoteButton.setGeometry(QRect(20, 570, 61, 61))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.addNoteButton.setFont(font1)
        self.addNoteButton.setStyleSheet(u"QPushButton{\n"
"background-color: #20242a;\n"
"color: #20242a;\n"
"border-radius: 10px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: black;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../icons/plus_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.addNoteButton.setIcon(icon1)
        self.addNoteButton.setIconSize(QSize(70, 70))
        self.addNoteButton.setFlat(False)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Notes</p><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"xddxdxdx", None))
        self.deleteButton.setText("")
        self.exitButton.setText("")
        self.addNoteButton.setText("")
    # retranslateUi

