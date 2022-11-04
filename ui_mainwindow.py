# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.

import re
import matplotlib.pyplot as plt
import warnings
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    plt.rcParams['toolbar'] = 'toolmanager'
from PyQt6 import QtCore, QtGui, QtWidgets
from binaryRelation import BinaryRelation
from hasseDiagram import HasseDiagram


class Ui_MainWindow(QtWidgets.QWidget):
    def setupUi(self, MainWindow, menu):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(390, 175)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(390, 175))
        MainWindow.setMaximumSize(QtCore.QSize(390, 200))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
        font.setPointSize(10)
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
"font-weight: bold")
        self.lbl_bin_class.setText("")
        self.lbl_bin_class.setObjectName("lbl_bin_class")
        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(300, 50, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_help.setFont(font)
        self.btn_help.setObjectName("btn_help")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(300, 20, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.btn_back.setFont(font)
        self.btn_back.setObjectName("btn_back")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Manual editing!
        self.add_functions(MainWindow, menu)  # Добавление сигналов

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Диаграмма Хассе"))
        self.edt_setR.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setR.setPlaceholderText(_translate("MainWindow", "Введите бинарное отношение R:"))
        self.lbl_props.setText(_translate("MainWindow", "Свойства бинарного отношения:"))
        self.edt_setA.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setA.setPlaceholderText(_translate("MainWindow", "Введите множество А:"))
        self.btn_run.setText(_translate("MainWindow", "Выполнить"))
        self.lbl_class.setText(_translate("MainWindow", "Класс бинарного отношения:"))
        self.btn_help.setText(_translate("MainWindow", "Справка"))
        self.btn_back.setText(_translate("MainWindow", "Вернуться"))

    def create_diagram(self, bin_rel) -> HasseDiagram:
        print("Диаграмма хассе на множестве ", bin_rel.A)
        return HasseDiagram(bin_rel)

    def add_functions(self, win, menu):
        self.btn_run.clicked.connect(
            lambda: self.button_click(win))  # TODO: btn_generate - генеировать рандомное бинарное отношение порядка
        self.btn_back.clicked.connect(lambda: self.return_to_mainmenu(win, menu))
        self.btn_help.clicked.connect(self.open_help)

    def resize_event(self, win):
        win.resize(390, 410)
        win.setMinimumSize(QtCore.QSize(390, 410))
        win.setMaximumSize(QtCore.QSize(390, 410))

    def output(self, win):
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
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Icon.Warning)
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

            self.resize_event(win)

        except IOError as e:
            self.error_handle(e)

    def button_click(self, win):
        self.output(win)

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

    def error_handle(self, err_type):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Critical)
        msg.setText("Ошибка")
        msg.setInformativeText(str(err_type))
        msg.setWindowTitle("Ошибка")
        msg.exec()

    def return_to_mainmenu(self, win, menu):
        win.close()
        menu.show()

    def open_help(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Icon.Information)
        msg.setText("Справка по вводу данных")
        msg.setInformativeText("Поле ввода множества A должно заполняться элементами множества через запятую. Например: 1, 2, 3.\n"
                               "Поле ввода бинарного отношения R должно заполняться парами элементов, записанных в круглых скобках, через запятую. "
                               "Сами пары должны быть разделены запятыми. Например: (1,2), (1,3), (2,3).")
        msg.setWindowTitle("Справка по вводу данных")
        msg.exec()