# Класс вершины Диаграммы Хассе
class HasseNode:
    def __init__(self, name, pos, level, options=None):
        # self._options = options if options is not None else {"node_color": "tab:blue"} #148aff tab:blue
        self._name = name
        self._pos = pos
        self._level = level

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, n):
        self._name = n

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, p):
        self._pos = p

    @property
    def level(self):
        return self._level

    @level.setter
    def level(self, lvl):
        self._level = lvl

    # @property
    # def options(self):
    #     return self._options
    #
    # @options.setter
    # def options(self, opt):
    #     self._options = opt