# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'notesarzbcJ.ui'
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
        Form.setMinimumSize(QSize(1000, 800))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 20, 1000, 800))
        self.widget.setMinimumSize(QSize(1000, 800))
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
        self.scrollArea.setGeometry(QRect(0, 100, 1000, 700))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1000, 700))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(400, 200))
        self.frame.setStyleSheet(u"background-color: gray;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 400, 200))
        self.label.setStyleSheet(u"padding: 10px")
        self.label.setWordWrap(True)

        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1, Qt.AlignLeft|Qt.AlignTop)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.exitButton = QPushButton(self.widget)
        self.exitButton.setObjectName(u"exitButton")
        self.exitButton.setGeometry(QRect(870, 30, 93, 28))
        self.exitButton.setStyleSheet(u"background-color: white\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Notes</p><p><br/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("Form", u"xddxdxdx", None))
        self.exitButton.setText(QCoreApplication.translate("Form", u"EXIT", None))
    # retranslateUi

