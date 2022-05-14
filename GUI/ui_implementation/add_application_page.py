from PySide2 import QtCore
from PySide2.QtCore import QPoint, QSize, QRect
from PySide2.QtGui import QIcon, Qt
from PySide2.QtWidgets import QMainWindow, QFrame, QLabel, QPushButton

from GUI.ui_python_files.ui_add_application import Ui_Form


class AddApplicationPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.ui.exitButton.clicked.connect(self.exit)
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))
        self.ui.refreshButton.setIcon(QIcon("icons/refresh.png"))
        self.ui.addAppButton.setIcon(QIcon("icons/plus_icon.png"))


        self.user_id = 0

    def add_application_widget(self, row_number, key_word, url):
        url_frame_name = "frame_url_" + str(row_number)
        key_word_frame_name = "frame_keyword_" + str(row_number)
        delete_button_name = "button_" + str(row_number)
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
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
        self.deleteButton.setIcon(QIcon("icons/x_icon.png"))
        self.deleteButton.setIconSize(QSize(30, 30))
        self.keyWordLabel = QLabel(self.frame)
        self.keyWordLabel.setObjectName(u"keyWordLabel")
        self.keyWordLabel.setGeometry(QRect(30, 50, 261, 31))
        self.urlLabel = QLabel(self.frame)
        self.urlLabel.setObjectName(u"urlLabel")
        self.urlLabel.setGeometry(QRect(310, 50, 561, 31))



        self.keyWordLabel.setObjectName(key_word_frame_name)
        self.urlLabel.setObjectName(url_frame_name)
        self.deleteButton.setObjectName(delete_button_name)
        self.keyWordLabel.setText(key_word)
        self.urlLabel.setText(url)
        self.label.setText('key word')
        self.label_2.setText('application url')
        self.ui.gridLayout.addWidget(self.frame, row_number, 0, 1, 1, Qt.AlignTop)

        return self.deleteButton



    def exit(self):
        self.close()

    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()