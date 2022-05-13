import sys
from PySide2.QtWidgets import QApplication

from GUI.ui_implementation.create_gui import CreateGui
from GUI.ui_implementation.confirmation_page import ConfirmationPage
from GUI.ui_implementation.kasta_page import KastaPage

if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_gui = CreateGui() #- PO ZAKONCZENIU TESTOW URUCHOMIMY TO PONOWNIE
    #kasta_page = KastaPage() # TYMCZASOWO, PODCZAS ROBIENIA KASTY
    #kasta_page.show()
    #widgets = CreateWidgets()
    sys.exit(app.exec_())
