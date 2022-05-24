from PySide2 import QtCore
from PySide2.QtCore import QPoint
from PySide2.QtGui import QIcon
from PySide2.QtWidgets import QMainWindow

from GUI.ui_python_files.ui_forgotpassword_page import Ui_Form


class ForgotPasswordPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.resetButton.clicked.connect(self.reset_password)
        self.ui.backToLoginButton.setIcon(QIcon("icons/x_icon.png"))

    def reset_password(self):
        email = self.ui.emailLabel.text()



        pass

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()


