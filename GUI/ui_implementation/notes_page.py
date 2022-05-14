from PySide2 import QtCore
from PySide2.QtCore import QSize, QPoint, QRect
from PySide2.QtGui import Qt, QIcon
from PySide2.QtWidgets import QMainWindow, QFrame, QLabel, QPushButton

from DataBase.Connection import ConnectDatabase
from GUI.ui_implementation.add_note_page import AddNotePage
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
        self.ui.exitButton.setIcon(QIcon("icons/x_icon.png"))
        self.ui.addNoteButton.setIcon(QIcon("icons/plus_icon.png"))

        self.add_note_page = AddNotePage()
        self.ui.addNoteButton.clicked.connect(self.build)

        self.user_id = 0



    def create_new_widget(self, row_number, column_number, note_text, idNotes):
        new_frame_name = "frame_" + str(idNotes)
        new_button_name = "button_" + str(idNotes)
        self.frame = QFrame(self.ui.scrollAreaWidgetContents)
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
        self.label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setText(note_text)
        self.deleteButton = QPushButton(self.frame)
        self.deleteButton.setObjectName(u"deleteButton")
        self.deleteButton.setGeometry(QRect(410, 10, 31, 28))
        self.deleteButton.setStyleSheet(u"QPushButton{\n"
                                        "background-color: #20242a;\n"
                                        "color: #20242a;\n"
                                        "border-radius: 10px;\n"
                                        "}")
        #icon = QIcon()
        #icon.addFile(u"../../icons/x_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        #self.deleteButton.setIcon(icon)
        self.deleteButton.setIcon(QIcon("icons/x_icon.png"))
        self.deleteButton.setIconSize(QSize(32, 32))
        self.ui.refreshButton.setIcon(QIcon("icons/refresh.png"))


        self.ui.gridLayout.addWidget(self.frame, row_number, column_number, 1, 1, Qt.AlignLeft | Qt.AlignTop)

        self.deleteButton.setObjectName(new_button_name)
        self.frame.setObjectName(new_frame_name)

        #print(new_button_name + ' ' + new_frame_name)
        return self.deleteButton

    def exit_page(self):
        self.close()
        self.add_note_page.close()

    def delete_note(self, idNotes, connection):
        connection.delete_note_with_id(idNotes)

    def build(self):
        self.add_note_page = AddNotePage()
        self.add_note_page.user_id = self.user_id
        print("Przekazane do add_note: " + str(self.add_note_page.user_id))
        self.add_note_page.show()


    def mousePressEvent(self, event):
        self.old_position = event.globalPos()

    def mouseMoveEvent(self, event):
        delta = QPoint(event.globalPos() - self.old_position)
        self.move(self.x() + delta.x(), self.y() + delta.y())
        self.old_position = event.globalPos()