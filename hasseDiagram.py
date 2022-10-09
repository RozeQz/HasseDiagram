from binaryRelation import BinaryRelation
import networkx as nx
import matplotlib.pyplot as plt
plt.rcParams['toolbar'] = 'toolmanager'

DIAGRAM_HEIGHT = 50
DIAGRAM_WIDTH = 50

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

    def draw(self):
        pos = {}
        print(self.second_elements(self._R))

        delta_height = DIAGRAM_HEIGHT / len(self.dominance_levels())
        delta_width = 0
        for k, v in self.dominance_levels().items():
            try:
                delta_width = DIAGRAM_WIDTH / len(v)
            except (ZeroDivisionError):
                pass
            count = 0
            for i in v:
                pos.setdefault(i, (count * delta_width, (k - 1) * delta_height))
                count += 1

        G = nx.Graph()
        G.add_nodes_from(self._A)
        print(self.get_dominance_list())
        print("Словарь доминации (ключ - над кем, значения - кто): ", self.second_elements(self.get_dominance_list()))
        print("Словарь доминации (ключ - кто, значения - над кем): ",
              self.second_elements(self.get_dominance_list(), reverse=True))
        G.add_edges_from(self.get_dominance_list())
        print(pos)

        # Удаляем ненужные кнопки на панели инструментов
        unwanted_buttons = ['pan', 'help', 'subplots']
        fig = plt.figure()
        for button in unwanted_buttons:
            fig.canvas.manager.toolmanager.remove_tool(button)

        if (self.class_of_relation() != 'not an order'):
            options = {
                "arrowsize": 18,
                "font_size": 15,
                "font_color": "white",
                "node_size": 600,
                "node_color": "blue",
                "edgecolors": "black",
                "with_labels": True
            }
            nx.draw(G, pos, **options)
            plt.show()
        else:
            return "There are conditions that are not provided."