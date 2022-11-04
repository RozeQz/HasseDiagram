import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from ui_mainwindow import Ui_MainWindow
from ui_mainmenu import Ui_MainMenu

def ui_application():
    # app = QApplication(sys.argv)
    # window = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(window)
    # window.show()
    # sys.exit(app.exec())

    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainMenu()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    ui_application()