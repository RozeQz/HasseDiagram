import numpy as np

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

    # Классы бинарных отношений
    def class_of_relation(self) -> str:
        if self.is_transitive():
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
            return "not an order"