import re
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from binaryRelation import BinaryRelation

class HasseDiagram(BinaryRelation):
    def __init__(self, bin_rel):
        self._A = bin_rel.get_A()
        self._R = bin_rel.get_R()

    def get_R(self) -> list:
        return self._R

    def set_R(self, r):
        self._R = r

    def get_A(self) -> set:
        return self._A

    def set_A(self, a):
        self._A = a

    def draw(self):
        pass