import networkx as nx
from hasseNode import HasseNode

DIAGRAM_HEIGHT = 50
DIAGRAM_WIDTH = 50


# Класс Диаграммы Хассе
class HasseDiagram:
    # Используется агрегация (HasseDiagram не может существовать без BinaryRelation)
    def __init__(self, bin_rel):
        self.__bin_rel = bin_rel

    # Массив доминирования (соединения на диаграмме Хассе)
    def __get_dominance_list(self) -> list:
        edge_list = self.__bin_rel.R
        new_edge_list = edge_list.copy()

        for (x, y) in edge_list:
            if (y, x) in edge_list:
                new_edge_list.remove((x, y))

        edge_list = new_edge_list.copy()
        new_edge_list = edge_list.copy()

        for (x, y) in edge_list:
            for z in list(self.__bin_rel.A):
                if ((x, z) in edge_list) and ((z, y) in edge_list):
                    try:
                        new_edge_list.remove((x, y))
                    except ValueError:
                        pass
        return new_edge_list

    # Словарь уровней доминирования (key = уровень; value = массив вершин)
    def __dominance_levels(self) -> dict:
        dominance_dict = dict(sorted(self.__bin_rel.second_elements(self.__get_dominance_list(), reverse=True).items()))
        levels_dict = {}
        for k, v in list(dominance_dict.items()):
            if not v:
                levels_dict.setdefault(1, []).append(
                    k)  # уровень доминирования = 1, если элемент ни над кем не доминирует
                dominance_dict.pop(k)  # удаляем рассмотренную вершину

        while dominance_dict:  # TODO: уменьшить вложенность
            for k, v in list(dominance_dict.items()):
                for el in v:
                    for i in range(1, len(levels_dict) + 1):
                        if el in levels_dict[i]:
                            levels_dict.setdefault(i + 1, []).append(
                                k)  # если элемент доминирует над элементом под ним, то элемент находится на следующем уровне доминирования
                            if len(v) > 1:
                                try:
                                    dominance_dict[k].remove(el)  # удаляем рассмотренную вершину
                                except:
                                    pass
                            else:
                                dominance_dict.pop(k)  # удаляем рассмотренную вершину

        # если на последнем уровне стоят элементы разного уровня доминации
        for k, v in list(reversed(levels_dict.items())):
            for el in v:
                dict_of_elements = self.__bin_rel.second_elements(self.__get_dominance_list())
                if dict_of_elements[el]:
                    for x in dict_of_elements[el]:
                        try:
                            if x not in levels_dict[k + 1]:
                                levels_dict.setdefault(k + 1, []).append(x)
                        except KeyError:
                            levels_dict.setdefault(k + 1, []).append(x)

        # чистим доминирование сверху вниз
        nodes = set()
        for k, v in list(reversed(levels_dict.items())):
            temp_level = list()
            for el in v:
                if el in nodes:
                    temp = []
                    [temp.append(x) for x in levels_dict[k] if x not in nodes]
                    levels_dict[k] = temp
                else:
                    temp_level.append(el)
            for i in temp_level:
                nodes.add(i)

        # убираем дубликаты
        nodes = set()
        for k, v in list(reversed(levels_dict.items())):
            for el in v:
                if el in nodes:
                    temp = []
                    [temp.append(x) for x in levels_dict[k] if x not in temp]
                    levels_dict[k] = temp
                else:
                    nodes.add(el)

        return levels_dict

    # private метод создания вершин диаграммы
    def __create_nodes(self):
        self.__nodes = []
        delta_height = DIAGRAM_HEIGHT / len(self.__dominance_levels())
        for k, v in self.__dominance_levels().items():
            delta_width = DIAGRAM_WIDTH / (len(v) + 1)
            count = 1
            for i in v:
                self.__nodes.append(HasseNode(i, (count * delta_width, (k - 1) * delta_height), k))
                count += 1

    # Словарь для метода draw библиотеки networkx
    def __get_nodes_to_draw(self) -> dict:
        position = {}
        for x in self.__nodes:
            position.setdefault(x.name, x.pos)
        return position

    def get_nodes_by_level(self, lvl) -> list:
        arr = []
        for x in self.__nodes:
            if x.level == lvl:
                arr.append(x)
        return arr

    def get_node_by_name(self, n) -> HasseNode:
        for x in self.__nodes:
            if x.name == n:
                return x

    def get_bin_rel(self):
        return self.__bin_rel

    def draw(self):
        self.__create_nodes()  # задаем позиции вершин

        G = nx.Graph()
        G.add_nodes_from(self.__bin_rel.A)
        print("Словарь доминации (ключ - над кем, значения - кто): ", self.__bin_rel.second_elements(
            self.__get_dominance_list()))
        print("Словарь доминации (ключ - кто, значения - над кем): ",
              self.__bin_rel.second_elements(self.__get_dominance_list(), reverse=True))
        G.add_edges_from(self.__get_dominance_list())

        options = {
            "arrowsize": 18,
            "font_size": 15,
            "font_color": "black",
            "node_size": 1000,
            "node_color": "tab:blue",  # 148aff tab:blue
            "edgecolors": "black",
            "with_labels": True,
            "width": 2
        }
        # plt.title("Диаграмма Хассе")
        nx.draw(G, self.__get_nodes_to_draw(), **options)
