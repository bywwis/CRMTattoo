from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogDelNote(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Подтвердите удаление")
        Dialog.resize(569, 199)
        Dialog.setStyleSheet("background-color: #DCD6DC;\n"
"")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 10, 491, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.yesBtn = QtWidgets.QPushButton(Dialog)
        self.yesBtn.setGeometry(QtCore.QRect(70, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.yesBtn.setFont(font)
        self.yesBtn.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: #99AAD2;\n"
"}")
        self.yesBtn.setObjectName("yesBtn")
        self.noBtn = QtWidgets.QPushButton(Dialog)
        self.noBtn.setGeometry(QtCore.QRect(340, 110, 181, 51))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.noBtn.setFont(font)
        self.noBtn.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: #99AAD2;\n"
"}")
        self.noBtn.setObjectName("noBtn")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Вы уверены, что хотите удалить запись?"))
        self.yesBtn.setText(_translate("Dialog", "Да"))
        self.noBtn.setText(_translate("Dialog", "Нет"))
