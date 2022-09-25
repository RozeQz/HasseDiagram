import numpy as np
import re

# Класс Бинарного отношения
class BinaryRelation:
    def __init__(self, a, r):
        self._A = a
        self._R = r

    def get_R(self) -> list:
        return self._R

    def set_R(self, r):
        self._R = r

    def get_A(self) -> set:
        return self._A

    def set_A(self, a):
        self._A = a

    # Матричное представление бинарного отношения
    def get_matrix(self):
        matrix = np.zeros((len(self._A), len(self._A)), dtype=int)
        for (row, col) in self._R:
            matrix[row - 1][col - 1] += 1
        return matrix

    # Транспонированная матрица
    def get_transposed_matrix(self):
        return self.get_matrix().T

    # Рефлексивность
    def is_reflexive(self) -> bool:
        return set(self.get_matrix().diagonal()) == {1}

    # Иррефлексивность
    def is_irreflexive(self) -> bool:
        return set(self.get_matrix().diagonal()) == {0}

    # Симметричность
    def is_symmetrical(self) -> bool:
        return (self.get_matrix().T == self.get_matrix()).all()

    # Транзитивность
    def is_transitive(self) -> bool:
        seconds_elements = {b for (a, b) in self._R}
        for (a, b) in self._R:
            for c in seconds_elements:
                if (b, c) in self._R and (a, c) not in self._R:
                    return False
        return True

    # Антисимметричность
    def is_antisymm(self) -> bool:
        for x in range(len(self._A)):
            for y in range(x, len(self._A)):
                if self.get_matrix()[x][y] and self.get_matrix()[y][x]:
                    if x != y:
                        return False
        return True


def main():
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


if __name__ == '__main__':
    main()