import re
import random
import matplotlib.pyplot as plt
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    plt.rcParams['toolbar'] = 'toolmanager'
from PyQt6 import QtCore, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from binaryRelation import BinaryRelation
from hasseDiagram import HasseDiagram
from ui_mainwindow import Ui_MainWindow


# Закрытие окна создания диаграммы Хассе
class MainWindow(QMainWindow, Ui_MainWindow):
    window_closed = QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.parent = parent
        self.error_msg = None
        self.help_msg = None

        self.btn_run.clicked.connect(self.button_click)  # TODO: генеировать рандомное бинарное отношение порядка
        self.btn_back.clicked.connect(lambda: self.return_to_mainmenu(parent))
        self.btn_help.clicked.connect(self.open_help)
        self.btn_gen.clicked.connect(self.input_random_order)

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()

    @staticmethod
    def create_diagram(bin_rel) -> HasseDiagram:
        print("Диаграмма хассе на множестве ", bin_rel.A)
        return HasseDiagram(bin_rel)

    def resize_event(self):
        self.resize(410, 410)
        self.setMinimumSize(QtCore.QSize(410, 410))
        self.setMaximumSize(QtCore.QSize(410, 410))

    def output(self):
        try:
            binary = self.create_binary_relation()

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
                hd = self.create_diagram(binary)
                self.lbl_bin_class.setStyleSheet("color: #008000;\n"
                                                 "font-weight: bold;\n"
                                                 "font-size: 12;\n"
                                                 "font-family: Arial;")

                # Удаляем ненужные кнопки на панели инструментов
                unwanted_buttons = ['pan', 'help', 'subplots']
                fig = plt.figure()
                for button in unwanted_buttons:
                    fig.canvas.manager.toolmanager.remove_tool(button)

                plt.show()
                hd.draw()

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Icon.Warning)
                msg.setText("Не является отношением порядка!")
                msg.setWindowTitle("Не является отношением порядка!")
                msg.exec()

                self.lbl_bin_class.setStyleSheet("color: rgb(184, 0, 0);\n"
                                                 "font-weight: bold;\n"
                                                 "font-size: 12;\n"
                                                 "font-family: Arial;")

            bin_class = binary.class_of_relation()
            if bin_class == "unknown":
                self.lbl_bin_class.setText("Не входит ни в один класс бинарных отношений")
            if bin_class == "tolerance":
                self.lbl_bin_class.setText("Толерантность")
            if bin_class == "equivalence":
                self.lbl_bin_class.setText("Эквивалентность")
            if bin_class == "partial order":
                self.lbl_bin_class.setText("Частичный порядок")
            if bin_class == "preorder":
                self.lbl_bin_class.setText("Предпорядок")
            if bin_class == "strict order":
                self.lbl_bin_class.setText("Строгий порядок")
            if bin_class == "strict preorder":
                self.lbl_bin_class.setText("Строгий предпорядок")

            self.resize_event()

        except IOError as e:
            self.error_handle(e)

    def button_click(self):
        self.output()

    def create_binary_relation(self) -> BinaryRelation:
        return BinaryRelation(self.input()[0], self.input()[1])

    def input(self) -> list:  # Ввод данных
        rubbish_text = re.sub(r'\([^()]*\)', '', self.edt_setR.toPlainText())
        alnum_outta_brackets = re.search(r'\w|\d', rubbish_text)
        if alnum_outta_brackets:
            raise IOError("Некорректный ввод бинарного отношения.")

        A = list(map(str, re.split(r' *, *', ',' + self.edt_setA.toPlainText() + ',')))  # Ввод числового множества
        A = list(x for x in A if x != '')
        R = []
        R_strings = re.findall(r'\( *([^\)]*) *\) *, *', self.edt_setR.toPlainText() + ",")  # Ввод бинарного отношения перечислением пар

        for elem in R_strings:
            R_str = tuple(map(str, re.split(r' *, *', elem)))  # Преобразуем в пару строковых значений
            R.append(R_str)

        if len(self.edt_setA.toPlainText()) == 0 or len(self.edt_setR.toPlainText()) == 0:
            raise IOError("Поля ввода не могут быть пустыми.")

        if not R:
            raise IOError("Некорректный ввод бинарного отношения.")

        # Уникальные элементы в множестве пар, задающих бинарное отношение
        list_unique = []
        for i in R:
            i = list(i)
            list_unique.extend(i)
        list_unique = list(set(list_unique))

        if not set(list_unique).issubset(set(A)):
            raise IOError(
                "Бинарное отношение R не является подмножеством декартова "
                "произведения множества A на себя. Пожалуйста, задайте R ⊆ A^2.")

        for x in R:
            if len(x) != 2:
                raise IOError(
                    "Неверное количество элементов в паре, задающей бинарное отношение.")

        return [A, R]

    def create_random_binary_relation(self) -> BinaryRelation:
        num_A = random.randrange(3, 7)
        A = list()
        R = list()
        for i in range(1, num_A + 1):
            A.append(i)

        num_R = random.randrange(3, 10)
        for i in range(num_R):
            first = random.choice(A)
            second = random.choice(A)
            R.append((first, second))

        return BinaryRelation(A, R)

    def input_random_order(self):
        bin_rel = self.create_random_binary_relation()
        bin_rel.make_order()
        self.edt_setA.setText(str(bin_rel.A)[1:-1])
        self.edt_setR.setText(str(bin_rel.R)[1:-1])

    def input_random_binary_relation(self):
        bin_rel = self.create_random_binary_relation()
        self.edt_setA.setText(str(bin_rel.A)[1:-1])
        self.edt_setR.setText(str(bin_rel.R)[1:-1])

    def error_handle(self, err_type):
        self.error_msg = QMessageBox()
        self.error_msg.setIcon(QMessageBox.Icon.Critical)
        self.error_msg.setText("Ошибка")
        self.error_msg.setInformativeText(str(err_type))
        self.error_msg.setWindowTitle("Ошибка")
        self.error_msg.exec()

    def return_to_mainmenu(self, menu):
        self.close()
        menu.setVisible(True)

    def open_help(self):
        if self.help_msg is None:
            self.help_msg = QMessageBox()
            self.help_msg.setIcon(QMessageBox.Icon.Information)
            self.help_msg.setText("Справка по вводу данных")
            self.help_msg.setInformativeText(
                "Поле ввода множества A должно заполняться элементами множества через запятую. Например: 1, 2, 3.\n"
                "Поле ввода бинарного отношения R должно заполняться парами элементов, "
                "записанных в круглых скобках, через запятую. "
                "Сами пары должны быть разделены запятыми. Например: (1,2), (1,3), (2,3).")
            self.help_msg.setWindowTitle("Справка по вводу данных")
        self.help_msg.exec()
