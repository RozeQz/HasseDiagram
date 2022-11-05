import sys
from PyQt6.QtWidgets import QApplication
from mainMenu import MainMenu


def ui_application():
    app = QApplication(sys.argv)
    window = MainMenu()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    ui_application()