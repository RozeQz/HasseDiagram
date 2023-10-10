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


class MainWindow(QMainWindow, Ui_MainWindow):
    window_closed = QtCore.pyqtSignal()
    number_of_diagrams = 0

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.error_msg = None
        self.help_msg = None

        self.btn_run.clicked.connect(self.button_click)
        self.btn_back.clicked.connect(lambda: self.return_to_mainmenu(parent))
        self.btn_help.clicked.connect(self.open_help)
        self.btn_gen.clicked.connect(self.input_random_order)

    def closeEvent(self, event):
        self.window_closed.emit()
        event.accept()

    @staticmethod
    def create_diagram(bin_rel) -> HasseDiagram:
        '''
        Создает диаграмму Хассе по заданному бинарному отношению (отношению порядка).

        Args:
            bin_rel: Отношение порядка, по которому содается диаграмма Хассе.

        Returns:
            Диаграмма Хассе HasseDiagram(bin_rel), где bin_rel - отношение порядка.
        '''
        print("Диаграмма хассе на множестве ", bin_rel.A)
        return HasseDiagram(bin_rel)

    def resize_event(self):
        '''
        Меняет размер окна.
        '''
        self.resize(410, 410)
        self.setMinimumSize(QtCore.QSize(410, 410))
        self.setMaximumSize(QtCore.QSize(410, 410))

    def output(self):
        '''
        Выводит на экран свойства заданного бинарного отношения.
        Выводит диаграмму Хассе, если бинарное отношение является отношением порядка.
        '''
        try:
            binary = self.create_binary_relation()

            if binary.is_reflexive():
                reflex_text = "Рефлексивно"
            elif binary.is_irreflexive():
                reflex_text = "Иррефлексивно"
            else:
                reflex_text = "Нерефлексивно"
            self.lbl_reflex.setText(f"   • {reflex_text}!")

            symm_text = "Симметрично" if binary.is_symmetrical() else "Несимметрично"
            self.lbl_symm.setText(f"   • {symm_text}!")

            trans_text = "Транзитивно" if binary.is_transitive() else "Нетранзитивно"
            self.lbl_trans.setText(f"   • {trans_text}!")

            antisymm_text = "Антисимметрично" if binary.is_antisymm() else "Не антисимметрично"
            self.lbl_antisym.setText(f"   • {antisymm_text}!")

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

                # Задаем название диаграмме
                self.number_of_diagrams += 1
                name_of_diagram = "Диаграмма " + str(self.number_of_diagrams)
                fig.canvas.manager.set_window_title(name_of_diagram)

                plt.show()
                hd.draw()

                # Сохраняем параметры диаграммы в соответствующем файле
                with open(name_of_diagram + ".txt", "w") as file:
                    params = "A: " + str(hd.get_bin_rel().A) + "\nR: " + str(hd.get_bin_rel().R) + "\n"
                    file.write(params)

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
        '''
        Обработчик нажатия на кнопку "Выполнить".
        '''
        self.output()

    def create_binary_relation(self) -> BinaryRelation:
        '''
        Создает бинарное отношение на тех данных, что были записаны в поля для ввода.

        Returns:
            BinaryRelation(A, R), где A, R - записаны в поля для ввода.
        '''
        return BinaryRelation(*self.input())

    def input(self) -> list:
        '''
        Валидатор и парсер ввода данных.

        Returns:
            Список [A, R], где A - само множество, R - список пар, задающих бинарное отношение на этом множестве.

        Raises:
            IOError: Если был некорректный ввод данных.
        '''
        rubbish_text = re.sub(r'\([^()]*\)', '', self.edt_setR.toPlainText())
        alnum_outta_brackets = re.search(r'\w|\d', rubbish_text)

        A = list(map(str, re.split(r' *, *', ',' + self.edt_setA.toPlainText() + ',')))  # Ввод числового множества
        A = list(x for x in A if x != '')
        R = []
        R_strings = re.findall(r'\( *([^\)]*) *\) *, *', self.edt_setR.toPlainText() + ",")  # Ввод бинарного отношения перечислением пар

        for elem in R_strings:
            R_str = tuple(map(str, re.split(r' *, *', elem)))  # Преобразуем в пару строковых значений
            R.append(R_str)

        if len(self.edt_setA.toPlainText()) == 0 or len(self.edt_setR.toPlainText()) == 0:
            raise IOError("Поля ввода не могут быть пустыми.")

        if re.findall(r'\) *\(', self.edt_setR.toPlainText()):
            raise IOError("Некорректный ввод бинарного отношения. Пары должны вводиться через запятую.")

        if alnum_outta_brackets or not R:
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

        if len(set(A)) > 40:
            raise IOError("Слишком большое количество элементов множества.")

        if len(set(R)) > 300:
            raise IOError("Слишком большое количество пар, задающих бинарное отношение.")

        return [A, R]

    def create_random_binary_relation(self) -> BinaryRelation:
        '''
            Создает случайное бинарное отношение на множестве A,
            заданное перечислением пар R.
        '''
        num_A = random.randrange(3, 7)
        A = list()
        R = list()
        for i in range(1, num_A + 1):
            A.append(i)

        num_R = random.randrange(7, 12)
        for i in range(num_R):
            first = random.choice(A)
            second = random.choice(A)
            R.append((first, second))

        return BinaryRelation(A, R)

    def bin_rel_to_valid_input(self, bin_rel):
        '''
        Конвертация и ввод бинарного отношения
        BinaryRelation(A, R) в поля для ввода.

        Args:
            bin_rel: Бинарное отношение, которое нужно распарсить и вывести.
        '''
        self.edt_setA.setText(", ".join(map(str, bin_rel.A)))
        self.edt_setR.setText(", ".join(map(str, bin_rel.R)))

    def input_random_order(self):
        '''
        Ввод в поля для ввода случайного бинарного отношения на множестве A,
        заданное перечислением пар R, образующих отношение порядка.
        '''
        bin_rel = self.create_random_binary_relation()
        bin_rel.make_order()
        self.bin_rel_to_valid_input(bin_rel)

    def input_random_binary_relation(self):
        '''
        Ввод в поля для ввода случайного бинарного отношения на множестве A,
        заданное перечислением пар R.
        '''
        bin_rel = self.create_random_binary_relation()
        self.bin_rel_to_valid_input(bin_rel)

    def error_handle(self, err_text):
        '''
        Окно ошибки.

        Args:
            err_text: Сообщение ошибки для отображения пользователю.
        '''
        self.error_msg = QMessageBox()
        self.error_msg.setIcon(QMessageBox.Icon.Critical)
        self.error_msg.setText("Ошибка")
        self.error_msg.setInformativeText(str(err_text))
        self.error_msg.setWindowTitle("Ошибка")
        self.error_msg.exec()

    def return_to_mainmenu(self, menu):
        '''
        Возврат к начальному окну приложения.

        Args:
            menu: Объект начального окна приложения.
        '''
        self.close()
        menu.setVisible(True)

    def open_help(self):
        '''
        Окно справки по вводу данных.
        '''
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
