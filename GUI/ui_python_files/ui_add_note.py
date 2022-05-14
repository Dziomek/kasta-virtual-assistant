# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_noteIngBip.ui'
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
        Form.resize(721, 563)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(80, 40, 581, 451))
        self.widget.setStyleSheet(u"background-color: #2b3038;\n"
"border-radius: 30px;")
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(60, 160, 460, 200))
        self.frame.setMinimumSize(QSize(460, 200))
        self.frame.setStyleSheet(u"background-color: #20242a;\n"
"font: 10pt \"Arial\";\n"
"color: white;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.noteTextEdit = QLineEdit(self.frame)
        self.noteTextEdit.setObjectName(u"noteTextEdit")
        self.noteTextEdit.setGeometry(QRect(0, 50, 461, 151))
        self.noteTextEdit.setStyleSheet(u"font: 10pt \"Arial\";\n"
"color: white;\n"
"padding: 10px;")
        self.noteTextEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(520, 10, 41, 41))
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
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(120, 20, 341, 81))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(32)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.addButton = QPushButton(self.widget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(240, 380, 91, 41))
        font1 = QFont()
        font1.setFamily(u"Segoe UI")
        font1.setPointSize(13)
        self.addButton.setFont(font1)
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
        self.errorLabel.setGeometry(QRect(0, 120, 581, 20))
        self.errorLabel.setStyleSheet(u"color: rgb(212, 192, 169);")
        self.errorLabel.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.noteTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"type text...", None))
        self.exitButton.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Add your note</p><p><br/></p></body></html>", None))
        self.addButton.setText(QCoreApplication.translate("Form", u"Add", None))
        self.errorLabel.setText("")
    # retranslateUi

