class HasseNode:
    '''
    Класс вершины диаграммы Хассе.
    Вся информация о названии вершины, её позиции и параметрах.
    '''
    def __init__(self, name, pos, level, options=None):
        # self._options = options if options is not None else {"node_color": "tab:blue"} #148aff tab:blue
        self.__name = name
        self.__pos = pos
        self.__level = level

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, n):
        self.__name = n

    @property
    def pos(self) -> tuple:
        return self.__pos

    @pos.setter
    def pos(self, p):
        self.__pos = p

    @property
    def level(self) -> int:
        return self.__level

    @level.setter
    def level(self, lvl):
        self.__level = lvl

    # @property
    # def options(self):
    #     return self._options
    #
    # @options.setter
    # def options(self, opt):
    #     self._options = opt
