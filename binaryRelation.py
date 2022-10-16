import numpy as np

# Класс Бинарного отношения
class BinaryRelation:
    def __init__(self, a, r):
        self.__A = a
        self.__R = r

    @property
    def R(self) -> list:
        return self.__R

    @R.setter
    def R(self, r):
        self.__R = r

    @property
    def A(self) -> set:
        return self.__A

    @A.setter
    def A(self, a):
        self.__A = a

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
        second_elements = {b for (a, b) in self.R}    # множество вторых элементов
        for (a, b) in self.R:
            for c in second_elements:
                if (b, c) in self.R and (a, c) not in self.R:     # if xRy and yRz => xRz
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
        return self.is_transitive() and not self.is_symmetrical()

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
