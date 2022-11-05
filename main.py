import sys
from PyQt6.QtWidgets import QApplication
from ui_mainmenu import Ui_MainMenu
from mainWindow import MainMenu

def ui_application():
    app = QApplication(sys.argv)
    window = MainMenu()
    ui = Ui_MainMenu()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    ui_application()