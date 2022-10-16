import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['toolbar'] = 'toolmanager'

DIAGRAM_HEIGHT = 50
DIAGRAM_WIDTH = 50

class HasseDiagram():
    # Используется агрегация (HasseDiagram не может существовать без BinaryRelation)
    def __init__(self, bin_rel):
        self._bin_rel = bin_rel

    # Массив доминирования (соединения на диаграмме Хассе)
    def __get_dominance_list(self) -> list:
        edge_list = [(x, y) for x, y in self._bin_rel.R if x != y]
        new_edge_list = edge_list.copy()
        for (x, y) in edge_list:
            for z in list(self._bin_rel.A):
                if ((x, z) in edge_list) and ((z, y) in edge_list):
                    try:
                        new_edge_list.remove((x, y))
                    except ValueError:
                        pass
        return new_edge_list

    # Словарь уровней доминирования (key = уровень; value = массив вершин)
    def __dominance_levels(self) -> dict:
        dominance_dict = dict(sorted(self._bin_rel.second_elements(self.__get_dominance_list(), reverse=True).items()))
        levels_dict = {}
        for k, v in list(dominance_dict.items()):
            if not v:
                levels_dict.setdefault(1, []).append(k)  # уровень доминирования = 1, если элемент ни над кем не доминирует
                dominance_dict.pop(k)  # удаляем рассмотренную вершину

        while dominance_dict:
            for k, v in list(dominance_dict.items()):
                for el in v:
                    for i in range(1, len(levels_dict) + 1):
                        if el in levels_dict[i]:
                            levels_dict.setdefault(i + 1, []).append(k)  # если элемент доминирует над элементом под ним, то элемент находится на следующем уровне доминирования
                            if len(v) > 1:
                                dominance_dict[k].remove(el)  # удаляем рассмотренную вершину
                            else:
                                dominance_dict.pop(k)  # удаляем рассмотренную вершину

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

    # private метод задачи позиции вершин диаграммы
    def __set_position(self) -> dict:
        pos = {}
        delta_height = DIAGRAM_HEIGHT / len(self.__dominance_levels())
        for k, v in self.__dominance_levels().items():
            delta_width = DIAGRAM_WIDTH / (len(v) + 1)
            count = 1
            for i in v:
                pos.setdefault(i, (count * delta_width, (k - 1) * delta_height))
                count += 1
        return pos

    def draw(self):
        print(self._bin_rel.second_elements(self._bin_rel.R))

        pos = self.__set_position()   # задаем позиции вершин

        G = nx.Graph()
        G.add_nodes_from(self._bin_rel.A)
        print(self.__get_dominance_list())
        print("Словарь доминации (ключ - над кем, значения - кто): ", self._bin_rel.second_elements(
            self.__get_dominance_list()))
        print("Словарь доминации (ключ - кто, значения - над кем): ",
              self._bin_rel.second_elements(self.__get_dominance_list(), reverse=True))
        G.add_edges_from(self.__get_dominance_list())
        print(self.__dominance_levels())

        # Удаляем ненужные кнопки на панели инструментов
        unwanted_buttons = ['pan', 'help', 'subplots']
        fig = plt.figure()
        for button in unwanted_buttons:
            fig.canvas.manager.toolmanager.remove_tool(button)

        if (self._bin_rel.class_of_relation() != 'not an order'):
            options = {
                "arrowsize": 18,
                "font_size": 15,
                "font_color": "black",
                "node_size": 1000,
                "node_color": "tab:blue", #148aff tab:blue
                "edgecolors": "black",
                "with_labels": True,
                "width": 2
            }
            # plt.title("Диаграмма Хассе")
            nx.draw(G, pos, **options)
            plt.show()