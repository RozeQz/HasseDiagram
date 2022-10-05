import re
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout
from ui_mainwindow import Ui_MainWindow
from binaryRelation import BinaryRelation
from hasseDiagram import HasseDiagram

def ui_application():
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())

def main():
    ui_application()

    # A = {1, 2, 3, 4, 5}
    # R = [(1,2), (1,3), (1,4), (1,5), (2,4), (2,5), (3,4), (3,5), (4,5)]

    # Ввод данных
    new_R = []
    A = set(map(int, re.findall(r'\w+', input())))  # Ввод числового множества
    R = re.findall(r'\([^)]*\)', input())           # Ввод бинарного отношения перечислением пар
    for i in R:
        R_str = tuple(map(str, re.findall(r'\w+\.?\w*', i)))    # Преобразуем в пару строковых значений
        try:
            R_int = tuple(map(int, R_str))          # Преобразуем в пару целочисленных значений
            new_R.append(R_int)
        except ValueError:
            try:
                R_float = tuple(map(float, R_str))  # Преобразуем в пару чисел с плавающей запятой
                new_R.append(R_float)
            except ValueError:
                new_R.append(R_str)
    R = new_R

    print("Введенное множество: " + str(A))
    print("Введенное бинарное отношение: " + str(R))

    R1 = BinaryRelation(A, R)
    print("Введенная матрица:")
    print(R1.get_matrix())
    print("Транспонированная матрица:")
    print(R1.get_transposed_matrix())
    if R1.is_reflexive():
        print("Бинарное отношение рефлексивно!")
    elif R1.is_irreflexive():
        print("Бинарное отношение иррефлексивно!")
    else:
        print("Бинарное отношение нерефлексивно!")
    print("Бинарное отношение симметрично!") if R1.is_symmetrical() else print("Бинарное отношение несимметрично!")
    print("Бинарное отношение транзитивно!") if R1.is_transitive() else print("Бинарное отношение нетранзитивно!")
    print("Бинарное отношение антисимметрично!") if R1.is_antisymm() else print(
        "Бинарное отношение не антисимметрично!")
    print(R1.class_of_relation())


if __name__ == '__main__':
    main()