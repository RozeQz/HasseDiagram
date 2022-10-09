from binaryRelation import BinaryRelation
import networkx as nx
import matplotlib.pyplot as plt
import random
import ast

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

    def trans_zamikanie(self, ls, reverse=False) -> dict:       # reverse=True - обратное транзитивное замыкание
        result = {}
        for i in self._A:
            result.setdefault(i, [])
        for first, second in ls:
            if not reverse:
                result.setdefault(first, []).append(second)
            else:
                result.setdefault(second, []).append(first)
        self.primes = []
        for num in self._A:
            prime = True
            for i in range(2, num):
                if (num % i == 0):
                    prime = False
            if prime:
                self.primes.append(num)
        return result

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

    def draw(self):
        pos = {}
        print(self.trans_zamikanie(self._R))
        # origin = -len(list(self.result.keys()))-5
        randlist = list(range(1, len(list(self.trans_zamikanie(self._R).keys())) + 1))
        print(randlist)
        for a in (list(self.trans_zamikanie(self._R).keys())):
            if a == 1:
                pos.setdefault(a, ((len(list(self.trans_zamikanie(self._R).keys())) / 2), -len(list(self.trans_zamikanie(self._R).keys())) * 2 - 4))
            elif a in self.primes:
                pos.setdefault(a, (a, -len(list(self.trans_zamikanie(self._R).keys())) * 2))
            elif len(list(self.trans_zamikanie(self._R)[a])) == 1:
                exitr = random.choice(randlist)
                pos.setdefault(a, (exitr, 0))
                randlist.remove(exitr)
            else:
                exitr = random.choice(randlist)
                pos.setdefault(a, (exitr, (-len(list(self.trans_zamikanie(self._R)[a]))) * 2))
                randlist.remove(exitr)

        T = nx.Graph()
        T.add_nodes_from(self._A)
        print(self.get_dominance_list())
        print("Словарь доминации (ключ - над кем, значения - кто): ", self.trans_zamikanie(self.get_dominance_list()))
        T.add_edges_from(self.get_dominance_list())
        print(pos)
        plt.figure()
        if (self.class_of_relation() != 'not an order'):
            nx.draw(T, pos, node_color='black', node_size=600, font_size=15, font_color='yellow', with_labels=True,
                    arrowsize=18, edge_color='green')
            plt.show()
        else:
            return "There are conditions that are not provided."