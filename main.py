import sys
from PySide2.QtWidgets import QApplication

from GUI.ui_implementation.create_gui import CreateGui
from GUI.ui_implementation.confirmation_page import ConfirmationPage



if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_gui = CreateGui()
    # widgets = CreateWidgets()
    sys.exit(app.exec_())
