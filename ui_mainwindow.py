# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
from PyQt6 import QtCore, QtGui, QtWidgets
from binaryRelation import BinaryRelation
from hasseDiagram import HasseDiagram


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(300, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(300, 180))
        MainWindow.setMaximumSize(QtCore.QSize(300, 180))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_symm = QtWidgets.QLabel(self.centralwidget)
        self.lbl_symm.setGeometry(QtCore.QRect(20, 240, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_symm.setFont(font)
        self.lbl_symm.setText("")
        self.lbl_symm.setObjectName("lbl_symm")
        self.lbl_reflex = QtWidgets.QLabel(self.centralwidget)
        self.lbl_reflex.setGeometry(QtCore.QRect(20, 210, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_reflex.setFont(font)
        self.lbl_reflex.setText("")
        self.lbl_reflex.setObjectName("lbl_reflex")
        self.edt_setR = QtWidgets.QTextEdit(self.centralwidget)
        self.edt_setR.setGeometry(QtCore.QRect(20, 60, 260, 60))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.edt_setR.setFont(font)
        self.edt_setR.setObjectName("edt_setR")
        self.lbl_props = QtWidgets.QLabel(self.centralwidget)
        self.lbl_props.setGeometry(QtCore.QRect(20, 180, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_props.setFont(font)
        self.lbl_props.setObjectName("lbl_props")
        self.edt_setA = QtWidgets.QTextEdit(self.centralwidget)
        self.edt_setA.setGeometry(QtCore.QRect(20, 20, 260, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.edt_setA.setFont(font)
        self.edt_setA.setObjectName("edt_setA")
        self.lbl_antisym = QtWidgets.QLabel(self.centralwidget)
        self.lbl_antisym.setGeometry(QtCore.QRect(20, 270, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_antisym.setFont(font)
        self.lbl_antisym.setText("")
        self.lbl_antisym.setObjectName("lbl_antisym")
        self.btn_run = QtWidgets.QPushButton(self.centralwidget)
        self.btn_run.setGeometry(QtCore.QRect(110, 140, 81, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.btn_run.setFont(font)
        self.btn_run.setObjectName("btn_run")
        self.lbl_trans = QtWidgets.QLabel(self.centralwidget)
        self.lbl_trans.setGeometry(QtCore.QRect(20, 300, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_trans.setFont(font)
        self.lbl_trans.setText("")
        self.lbl_trans.setObjectName("lbl_trans")
        self.lbl_class = QtWidgets.QLabel(self.centralwidget)
        self.lbl_class.setGeometry(QtCore.QRect(20, 340, 260, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(9)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.lbl_class.setFont(font)
        self.lbl_class.setObjectName("lbl_class")
        self.lbl_bin_class = QtWidgets.QLabel(self.centralwidget)
        self.lbl_bin_class.setGeometry(QtCore.QRect(20, 370, 260, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_bin_class.setFont(font)
        self.lbl_bin_class.setStyleSheet("color: rgb(184, 0, 0);\n"
                                         "font-weight: bold;\n"
                                         "font-size: 12;\n"
                                         "font-family: Arial;")
        self.lbl_bin_class.setText("")
        font.setPointSize(9)
        self.lbl_bin_class.setObjectName("lbl_bin_class")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Manual editing!
        self.add_functions(MainWindow)  # Добавление сигналов

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Диаграмма Хассе"))
        self.edt_setR.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setR.setPlaceholderText(_translate("MainWindow", "Введите бинарное отношение R:"))
        self.lbl_props.setText(_translate("MainWindow", "Свойства бинарного отношения:"))
        self.edt_setA.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setA.setPlaceholderText(_translate("MainWindow", "Введите множество А:"))
        self.btn_run.setText(_translate("MainWindow", "Выполнить"))
        self.lbl_class.setText(_translate("MainWindow", "Класс бинарного отношения:"))

    def create_diagram(self, bin_rel) -> HasseDiagram:
        print("Диаграмма хассе на множестве ", bin_rel.A)
        return HasseDiagram(bin_rel)

    def add_functions(self, win):
        # self.btn_run.clicked.connect(lambda: self.create_diagram(self.input()[0]))
        self.btn_run.clicked.connect(lambda: self.button_click(win))

    def resize_event(self, win):
        win.resize(300, 410)
        win.setMinimumSize(QtCore.QSize(300, 410))
        win.setMaximumSize(QtCore.QSize(300, 410))

    def output(self):
        binary = self.create_binary_relation()
        hd = self.create_diagram(binary)

        # self.widget = PlotCanvas(hd, self.centralwidget)  # Полотно для рисования
        # self.widget.setGeometry(QtCore.QRect(300, 0, 400, 400))
        # self.widget.setObjectName("widget")

        if binary.is_reflexive():
            self.lbl_reflex.setText("   • Рефлексивно!")
        elif binary.is_irreflexive():
            self.lbl_reflex.setText("   • Иррефлексивно!")
        else:
            self.lbl_reflex.setText("   • Нерефлексивно!")

        self.lbl_symm.setText(
            "   • Симметрично!") if binary.is_symmetrical() else self.lbl_symm.setText(
            "   • Несимметрично!")
        self.lbl_trans.setText(
            "   • Транзитивно!") if binary.is_transitive() else self.lbl_trans.setText(
            "   • Нетранзитивно!")
        self.lbl_antisym.setText(
            "   • Антисимметрично!") if binary.is_antisymm() else self.lbl_antisym.setText(
            "   • Не антисимметрично!")

        if binary.is_order():
            self.lbl_bin_class.setStyleSheet("color: #008000;\n"
                                             "font-weight: bold;\n"
                                             "font-size: 12;\n"
                                             "font-family: Arial;")
            hd.draw()
        else:
            self.lbl_bin_class.setStyleSheet("color: rgb(184, 0, 0);\n"
                                             "font-weight: bold;\n"
                                             "font-size: 12;\n"
                                             "font-family: Arial;")

        bin_class = binary.class_of_relation()
        if bin_class == "unknown": self.lbl_bin_class.setText("Не входит ни в один класс")
        if bin_class == "tolerance": self.lbl_bin_class.setText("Эквивалентность")
        if bin_class == "equivalence": self.lbl_bin_class.setText("Толерантность")
        if bin_class == "partial order": self.lbl_bin_class.setText("Частичный порядок")
        if bin_class == "preorder": self.lbl_bin_class.setText("Предпорядок")
        if bin_class == "strict order": self.lbl_bin_class.setText("Строгий порядок")
        if bin_class == "strict preorder": self.lbl_bin_class.setText("Строгий предпорядок")

    def button_click(self, win):
        self.output()
        self.resize_event(win)
        # self.create_diagram(self.create_binary_relation())
        # PlotCanvas.plot(self.create_diagram(self.create_binary_relation()))

    def create_binary_relation(self) -> BinaryRelation:
        return BinaryRelation(self.input()[0], self.input()[1])

    def input(self) -> list:  # Ввод данных
        new_R = []
        A = set(map(str, re.findall(r'\w+', self.edt_setA.toPlainText())))  # Ввод числового множества
        R = re.findall(r'\([^)]*\)',
                       self.edt_setR.toPlainText())  # Ввод бинарного отношения перечислением пар TODO: сделать валидацию R ⊆ A^2
        for i in R:
            R_str = tuple(map(str, re.findall(r'\w+\.?\w*', i)))  # Преобразуем в пару строковых значений
            new_R.append(R_str)
        R = new_R
        return [A, R]

# class PlotCanvas(FigureCanvas):  # By inheriting the FigureCanvas class, this class is both a PyQt5 Qwidget and a Matplotlib FigureCanvas, which is the key to connecting pyqt5 and matplotlib
#     def __init__(self, hd, parent=None, width=500, height=500, dpi=100):
#         fig = Figure(figsize=(width, height), dpi=dpi)  # Create a Figure. Note: This Figure is a figure under matplotlib, not a figure under matplotlib.pyplot
#         self.axes = fig.add_subplot(111)  # Call the add_subplot method under figure, similar to the subplot method under matplotlib.pyplot
#         self.plot(hd)
#         FigureCanvas.__init__(self, fig)  # Initialize the parent class
#         self.setParent(parent)
#         FigureCanvas.setSizePolicy(self, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
#         FigureCanvas.updateGeometry(self)
#
#     def plot(self, hasse_diagram):
#         G = nx.Graph()
#         G.add_nodes_from(hasse_diagram.get_A())
#         G.add_edges_from(hasse_diagram.get_R())
#         pos = nx.spring_layout(G)
#         nx.draw_networkx_nodes(G, pos, node_size=500)
#         nx.draw_networkx_edges(G, pos, edgelist=G.edges(), edge_color='black')
#         nx.draw_networkx_labels(G, pos)
#         nx.draw(G, pos=nx.spring_layout(G), node_color='w', ax=self.axes, edge_color='b', with_labels=True, alpha=1, font_size=10, node_size=20, arrows=True)
#         plt.show()
#         hasse_diagram.draw()