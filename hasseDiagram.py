import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['toolbar'] = 'toolmanager'

DIAGRAM_HEIGHT = 50
DIAGRAM_WIDTH = 50

class HasseDiagram():
    # Используется агрегация (HasseDiagram не может существовать без BinaryRelation)
    def __init__(self, bin_rel):
        self._bin_rel = bin_rel

    # private метод задачи позиции вершин диаграммы
    def __set_position(self) -> dict:
        pos = {}
        delta_height = DIAGRAM_HEIGHT / len(self._bin_rel.dominance_levels())
        delta_width = 0
        for k, v in self._bin_rel.dominance_levels().items():
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
        print(self._bin_rel.get_dominance_list())
        print("Словарь доминации (ключ - над кем, значения - кто): ", self._bin_rel.second_elements(self._bin_rel.get_dominance_list()))
        print("Словарь доминации (ключ - кто, значения - над кем): ",
              self._bin_rel.second_elements(self._bin_rel.get_dominance_list(), reverse=True))
        G.add_edges_from(self._bin_rel.get_dominance_list())
        print(self._bin_rel.dominance_levels())

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