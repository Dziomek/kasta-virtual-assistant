import sys
from PySide2.QtWidgets import QApplication
from GUI.ui_implementation.splash import SplashScreen

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SplashScreen()
    # widgets = CreateWidgets()
    sys.exit(app.exec_())
