import re
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

        self.add_functions(parent)  # Добавление сигналов

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()

    def add_functions(self, parent):
        self.btn_run.clicked.connect(self.button_click)  # TODO: btn_generate - генеировать рандомное бинарное отношение порядка
        self.btn_back.clicked.connect(lambda: self.return_to_mainmenu(parent))
        self.btn_help.clicked.connect(self.open_help)

    @staticmethod
    def create_diagram(self, bin_rel) -> HasseDiagram:
        print("Диаграмма хассе на множестве ", bin_rel.A)
        return HasseDiagram(bin_rel)

    def resize_event(self):
        self.resize(390, 410)
        self.setMinimumSize(QtCore.QSize(390, 410))
        self.setMaximumSize(QtCore.QSize(390, 410))

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
            if bin_class == "unknown": self.lbl_bin_class.setText("Не входит ни в один класс")
            if bin_class == "tolerance": self.lbl_bin_class.setText("Эквивалентность")
            if bin_class == "equivalence": self.lbl_bin_class.setText("Толерантность")
            if bin_class == "partial order": self.lbl_bin_class.setText("Частичный порядок")
            if bin_class == "preorder": self.lbl_bin_class.setText("Предпорядок")
            if bin_class == "strict order": self.lbl_bin_class.setText("Строгий порядок")
            if bin_class == "strict preorder": self.lbl_bin_class.setText("Строгий предпорядок")

            self.resize_event()

        except IOError as e:
            self.error_handle(e)

    def button_click(self):
        self.output()

    def create_binary_relation(self) -> BinaryRelation:
        return BinaryRelation(self.input()[0], self.input()[1])

    def input(self) -> list:  # Ввод данных
        new_R = []
        A = set(map(str, re.split(r' *, *', ',' + self.edt_setA.toPlainText() + ',')))  # Ввод числового множества
        A.discard('')
        R = re.findall(r'(\([^)]*\)), *',
                       self.edt_setR.toPlainText() + ", ")  # Ввод бинарного отношения перечислением пар TODO: сделать валидацию R ⊆ A^2
        for i in R:
            R_str = tuple(
                map(str, re.split(r' *, *', ',' + i[1:-1] + ',')))  # Преобразуем в пару строковых значений
            R_str = tuple(x for x in R_str if x != '')
            new_R.append(R_str)
        R = new_R

        if len(A) == 0 or len(R) == 0:
            raise IOError("Поля ввода не могут быть пустыми.")
        else:
            # Уникальные элементы в множестве пар, задающих бинарное отношение
            list_unique = []
            for i in R:
                i = list(i)
                list_unique.extend(i)
            list_unique = list(set(list_unique))

            if not set(list_unique).issubset(set(A)):
                raise IOError(
                    "Бинарное отношение R не является подмножеством декартова произведения множества A на себя. Пожалуйста, задайте R ⊆ A^2.")

            else:
                for x in R:
                    if len(x) != 2:
                        raise IOError(
                            "Неверное количество элементов в паре, задающей бинарное отношение.")
                else:
                    return [A, R]

    @staticmethod
    def error_handle(self, err_type):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText("Ошибка")
        msg.setInformativeText(str(err_type))
        msg.setWindowTitle("Ошибка")
        msg.exec()

    def return_to_mainmenu(self, menu):
        self.close()
        menu.setVisible(True)

    @staticmethod
    def open_help(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Справка по вводу данных")
        msg.setInformativeText(
            "Поле ввода множества A должно заполняться элементами множества через запятую. Например: 1, 2, 3.\n"
            "Поле ввода бинарного отношения R должно заполняться парами элементов, записанных в круглых скобках, через запятую. "
            "Сами пары должны быть разделены запятыми. Например: (1,2), (1,3), (2,3).")
        msg.setWindowTitle("Справка по вводу данных")
        msg.exec()