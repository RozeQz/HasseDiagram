# Form implementation generated from reading ui file 'ui_theorydialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_TheoryDialog(QtWidgets.QWidget):
    def setupUi(self, TheoryDialog):
        TheoryDialog.setObjectName("TheoryDialog")
        TheoryDialog.resize(347, 300)
        self.label = QtWidgets.QLabel(TheoryDialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 231, 16))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(TheoryDialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(TheoryDialog)
        QtCore.QMetaObject.connectSlotsByName(TheoryDialog)

        self.pushButton.clicked.connect(TheoryDialog.close)

    def retranslateUi(self, TheoryDialog):
        _translate = QtCore.QCoreApplication.translate
        TheoryDialog.setWindowTitle(_translate("TheoryDialog", "Теория"))
        self.label.setText(_translate("TheoryDialog", "Просто справочная теория"))
        self.pushButton.setText(_translate("TheoryDialog", "Вернуться"))