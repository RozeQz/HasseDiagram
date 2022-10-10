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
        arr = list(self._A)
        for (row, col) in self._R:
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
        second_elements = {b for (a, b) in self._R}    # множество вторых элементов
        for (a, b) in self._R:
            for c in second_elements:
                if (b, c) in self._R and (a, c) not in self._R:     # if xRy and yRz => xRz
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
        for i in self._A:
            result.setdefault(i, [])
        for first, second in ls:
            if not reverse:
                result.setdefault(first, []).append(second)
            else:
                result.setdefault(second, []).append(first)
        return result

    # Массив доминирования (соединения на диаграмме Хассе)
    def get_dominance_list(self) -> list:
        edge_list = [(x, y) for x, y in self._R if x != y]
        new_edge_list = edge_list.copy()
        for (x, y) in edge_list:
            for z in list(self._A):
                if ((x, z) in edge_list) and ((z, y) in edge_list):
                    try:
                        new_edge_list.remove((x, y))
                    except ValueError:
                        pass
        return new_edge_list

    # Словарь уровней доминирования (key = уровень; value = массив вершин)
    def dominance_levels(self) -> dict:
        dominance_dict = dict(sorted(self.second_elements(self.get_dominance_list(), reverse=True).items()))
        levels_dict = {}
        for k, v in list(dominance_dict.items()):
            if not v:
                levels_dict.setdefault(1, []).append(k)     # уровень доминирования = 1, если элемент ни над кем не доминирует
                dominance_dict.pop(k)                       # удаляем рассмотренную вершину

        while dominance_dict:
            for k, v in list(dominance_dict.items()):
                for el in v:
                    for i in range(1, len(levels_dict) + 1):
                        if el in levels_dict[i]:
                            levels_dict.setdefault(i + 1, []).append(k)     # если элемент доминирует над элементом под ним, то элемент находится на следующем уровне доминирования
                            if len(v) > 1:
                                dominance_dict[k].remove(el)                # удаляем рассмотренную вершину
                            else:
                                dominance_dict.pop(k)                       # удаляем рассмотренную вершину

        nodes = set()
        for k, v in list(reversed(levels_dict.items())):
            for el in v:
                if el in nodes:
                    levels_dict[k].remove(el)
                else:
                    nodes.add(el)

        return levels_dict
