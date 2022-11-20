import random

import numpy as np


# Класс Бинарного отношения
class BinaryRelation:
    def __init__(self, a, r):
        self.__A = []
        self.__R = []
        for x in a:
            if x not in self.__A:
                self.__A.append(x)
        for x in r:
            if x not in self.__R:
                self.__R.append(x)

    @property
    def R(self) -> list:
        return self.__R

    @R.setter
    def R(self, r):
        self.__R = []
        for x in r:
            if x not in self.__R:
                self.__R.append(x)

    @property
    def A(self) -> list:
        return self.__A

    @A.setter
    def A(self, a):
        self.__A = []
        for x in a:
            if x not in self.__A:
                self.__A.append(x)

    # Матричное представление бинарного отношения
    def get_matrix(self):
        matrix = np.zeros((len(self.__A), len(self.__A)), dtype=int)
        arr = list(self.A)
        for (row, col) in self.R:
            matrix[arr.index(row)][arr.index(col)] += 1
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
        second_elements = {b for (a, b) in self.R}  # множество вторых элементов
        for (a, b) in self.R:
            for c in second_elements:
                if (b, c) in self.R and (a, c) not in self.R:  # if xRy and yRz => xRz
                    return False
        return True

    # Антисимметричность
    def is_antisymm(self) -> bool:
        for x in range(len(self.A)):
            for y in range(x, len(self.A)):
                if self.get_matrix()[x][y] and self.get_matrix()[y][x]:
                    if x != y:
                        return False
        return True

    # Является ли порядком
    def is_order(self) -> bool:
        return self.is_transitive() and not self.is_symmetrical() and (self.is_reflexive() or self.is_irreflexive())

    # Сделать отношение рефлексивным
    def make_reflexive(self):
        if not self.is_reflexive():
            for k in self.A:
                if (k, k) not in self.R:
                    self.R.append((k, k))

    def make_irreflexive(self):
        if not self.is_irreflexive():
            for k in self.A:
                if (k, k) in self.R:
                    self.R.remove((k, k))

    # Сделать отношение антисимметричным
    def make_antisymmetric(self):
        if not self.is_antisymm():
            for (x, y) in self.R:
                for (a, b) in self.R:
                    if (x != y) and (x == b) and (y == a):  # Если есть пример, нарушающий антисимметричность
                        self.R.remove((y, x))  # Удаляем пару, которая нарушает антисимметричность

    # Сделать отношение несимметричным
    def make_not_symmetrical(self):
        while self.is_symmetrical():
            for (x, y) in self.R:
                if (x != y) and ((y, x) in self.R):
                    if random.choice([True, False]):
                        self.R.remove((y, x))
                    else:
                        self.R.remove((x, y))

    # Сделать отношение транзитивным
    def make_transitive(self):
        if not self.is_transitive():
            for (a, b) in self.R:
                for (c, d) in self.R:
                    if ((b == c) and (a != b) and ((a, d) not in self.R)):
                        self.R.append((a, d))

    # Сделать отношением порядка
    def make_order(self):
        while not self.is_order():
            counter = 0
            while not self.is_order() and counter < 5:
                if random.choice([True, False]):
                    self.make_not_symmetrical()
                else:
                    self.make_irreflexive()
                self.make_transitive()
                counter += 1
            if counter >= 5:
                self.make_reflexive()
                self.make_transitive()

    # Классы бинарных отношений
    def class_of_relation(self) -> str:
        if self.is_order():
            if self.is_reflexive():
                if self.is_antisymm():
                    return "partial order"
                else:
                    return "preorder"
            elif self.is_irreflexive():
                if self.is_antisymm():
                    return "strict order"
                else:
                    return "strict preorder"
        else:
            if self.is_reflexive() and self.is_symmetrical():
                if self.is_transitive():
                    return "equivalence"
                else:
                    return "tolerance"
            else:
                return "unknown"

    # Словарь вторых элементов пары (key = первый элемент пары; value = массив вторых элементов)
    # reverse=True - словарь первых элементов пары
    def second_elements(self, ls, reverse=False) -> dict:
        result = {}
        for i in self.A:
            result.setdefault(i, [])
        for first, second in ls:
            if not reverse:
                result.setdefault(first, []).append(second)
            else:
                result.setdefault(second, []).append(first)
        return result
