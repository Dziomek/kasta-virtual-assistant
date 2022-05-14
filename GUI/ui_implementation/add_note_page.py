from PySide2 import QtCore
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from GUI.ui_python_files.ui_add_note import Ui_Form


class AddNotePage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))

    def exit(self):
        self.close()