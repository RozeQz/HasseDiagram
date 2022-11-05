from ui_mainmenu import Ui_MainMenu
from ui_mainwindow import Ui_MainWindow
from ui_theorydialog import Ui_TheoryDialog
from mainWindow import MainWindow
from PyQt6.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox

class MainMenu(QMainWindow, Ui_MainMenu):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.parent = parent

        self.btn_create.clicked.connect(self.open_hasse)
        self.btn_theory.clicked.connect(self.open_theory)

    # Переопределенный метод класс QWidget - обработчик закрытия
    def closeEvent(self, event):    # Закрытие главного меню (приложения целиком)
        reply = QMessageBox()
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setWindowTitle("Подтверждение закрытия")
        reply.setText("Вы уверены, что хотите закрыть приложение?")
        reply.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        reply.setDefaultButton(QMessageBox.StandardButton.No)
        ret = reply.exec()

        if ret == QMessageBox.StandardButton.Yes:
            event.accept()

            for window in QApplication.topLevelWidgets():   # Закрытие всех дочерних окон
                window.close()

        else:
            event.ignore()

    def open_hasse(self):
        window = MainWindow()
        window.window_closed.connect(self.open_mainmenu)
        ui = Ui_MainWindow()
        ui.setupUi(window, self)
        window.show()
        self.setVisible(False)

    def open_mainmenu(self):
        self.setVisible(True)

    def open_theory(self):
        global theory
        theory = QDialog()
        ui = Ui_TheoryDialog()
        ui.setupUi(theory)
        theory.show()