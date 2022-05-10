from PySide2 import QtCore
from PySide2.QtCore import QSize, QPoint, QRect
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QMainWindow, QFrame, QLabel, QPushButton

from GUI.ui_python_files.ui_notes import Ui_Form


class MyNotesPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        ###############
        self.ui.exitButton.clicked.connect(self.exit_page)

    def create_new_widget(self, row_number, column_number, note_text, idNotes):
        new_frame_name = "frame_" + str(idNotes)
        new_button_name = "button_" + str(idNotes)
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
        self.frame.setObjectName(new_frame_name)
        self.frame.setMinimumSize(QSize(400, 200))
        self.frame.setStyleSheet(u"background-color: gray;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 400, 200))
        self.label.setWordWrap(True)
        self.label.setText(note_text)
        self.label.setStyleSheet(u"padding: 10px;")
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(new_button_name)
        self.deleteButton.setGeometry(QRect(290, 10, 93, 28))
        self.deleteButton.setStyleSheet(u"background-color: white;")
        self.ui.gridLayout.addWidget(self.frame, row_number, column_number, 1, 1, Qt.AlignLeft | Qt.AlignTop)

        print(new_button_name)
        print(new_frame_name)

    def exit_page(self):
        self.close()

    def delete_note(self, idNotes):
        pass


    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()