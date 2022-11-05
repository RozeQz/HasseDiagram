from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtCore import pyqtSignal

# Закрытие окна создания диаграммы Хассе
class MainWindow(QMainWindow):
    window_closed = pyqtSignal()

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()