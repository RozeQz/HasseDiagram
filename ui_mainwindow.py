# Form implementation generated from reading ui file 'ui_mainwindow.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(410, 175)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(410, 175))
        MainWindow.setMaximumSize(QtCore.QSize(410, 175))
        font = QtGui.QFont()
        font.setFamily("Arial")
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("background-color: #FEFFFE;")
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
        self.edt_setR.setStyleSheet("border-color: #3C66DC;\n"
                                    "border-width: 1px;\n"
                                    "border-style: solid;")
        self.edt_setR.setTabChangesFocus(True)
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
        self.edt_setA.setStyleSheet("border-color: #3C66DC;\n"
                                    "border-width: 1px;\n"
                                    "border-style: solid;")
        self.edt_setA.setTabChangesFocus(True)
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
        self.btn_run.setGeometry(QtCore.QRect(85, 130, 130, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_run.setFont(font)
        self.btn_run.setStyleSheet("border-color: #3C66DC;\n"
                                   "font: 90 12pt \"Arial\";\n"
                                   "font-weight: bold;\n"
                                   "color: #3C66DC;\n"
                                   "border-width: 2px;\n"
                                   "border-style: solid;\n"
                                   "background-color: rgb(255, 255, 255);")
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
        self.lbl_bin_class.setGeometry(QtCore.QRect(20, 370, 300, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lbl_bin_class.setFont(font)
        self.lbl_bin_class.setStyleSheet("color: rgb(184, 0, 0);\n"
                                         "font-weight: bold")
        self.lbl_bin_class.setText("")
        self.lbl_bin_class.setObjectName("lbl_bin_class")
        self.btn_help = QtWidgets.QPushButton(self.centralwidget)
        self.btn_help.setGeometry(QtCore.QRect(300, 50, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.btn_help.setFont(font)
        self.btn_help.setStyleSheet("border-color: black;\n"
                                    "font: 90 10pt \"Arial\";\n"
                                    "color: #black;\n"
                                    "border-width: 1px;\n"
                                    "border-style: solid;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.btn_help.setObjectName("btn_help")
        self.btn_back = QtWidgets.QPushButton(self.centralwidget)
        self.btn_back.setGeometry(QtCore.QRect(300, 20, 91, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("border-color: black;\n"
                                    "font: 90 10pt \"Arial\";\n"
                                    "color: #black;\n"
                                    "border-width: 1px;\n"
                                    "border-style: solid;\n"
                                    "background-color: rgb(255, 255, 255);")
        self.btn_back.setObjectName("btn_back")
        self.btn_gen = QtWidgets.QPushButton(self.centralwidget)
        self.btn_gen.setGeometry(QtCore.QRect(300, 80, 91, 61))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(11)
        self.btn_gen.setFont(font)
        self.btn_gen.setAutoFillBackground(False)
        self.btn_gen.setStyleSheet("white-space: normal;\n"
                                   "border-color: black;\n"
                                   "font: 90 10pt \"Arial\";\n"
                                   "color: #black;\n"
                                   "border-width: 1px;\n"
                                   "border-style: solid;\n"
                                   "background-color: rgb(255, 255, 255);")
        self.btn_gen.setAutoRepeat(False)
        self.btn_gen.setFlat(False)
        self.btn_gen.setObjectName("btn_gen")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Диаграмма Хассе"))
        self.edt_setR.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setR.setPlaceholderText(_translate("MainWindow", "Введите бинарное отношение R:"))
        self.lbl_props.setText(_translate("MainWindow", "Свойства бинарного отношения:"))
        self.edt_setA.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Arial\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'MS Shell Dlg 2\'; font-size:8.25pt;\"><br /></p></body></html>"))
        self.edt_setA.setPlaceholderText(_translate("MainWindow", "Введите множество А:"))
        self.btn_run.setText(_translate("MainWindow", "Выполнить"))
        self.lbl_class.setText(_translate("MainWindow", "Класс бинарного отношения:"))
        self.btn_help.setText(_translate("MainWindow", "Справка"))
        self.btn_back.setText(_translate("MainWindow", "Вернуться"))
        self.btn_gen.setText(_translate("MainWindow", "Генерировать\n"
                                                      "отношение\n"
                                                      "порядка"))
