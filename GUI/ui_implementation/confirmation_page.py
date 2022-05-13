from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import (QColor, QIcon)
from PySide2.QtWidgets import *

from GUI.ui_python_files.ui_confirmation_page import Ui_Form


class ConfirmationPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.greenmarkLabel.setIcon(QIcon("icons/greenmark.png"))

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()