from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal

# Закрытие главного меню (приложения целиком)
class MainMenu(QMainWindow):
    def closeEvent(self, event):
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

# Закрытие окна создания диаграммы Хассе
class MainWindow(QMainWindow):
    window_closed = pyqtSignal()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()