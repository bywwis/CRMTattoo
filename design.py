from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1985, 942)
        MainWindow.setStyleSheet("background-color: rgb(213, 182, 237);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 401, 341))
        self.calendar.setStyleSheet("font: 12pt \"News Cycle\";\n"
"selection-background-color: rgb(182, 114, 234);")
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.recordsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.recordsBtn.setGeometry(QtCore.QRect(0, 350, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.recordsBtn.setFont(font)
        self.recordsBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.recordsBtn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #B672EA;\n"
"}\n"
"")
        self.recordsBtn.setObjectName("recordsBtn")
        self.clienBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clienBtn.setGeometry(QtCore.QRect(0, 420, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.clienBtn.setFont(font)
        self.clienBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clienBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #B672EA;\n"
"}")
        self.clienBtn.setObjectName("clienBtn")
        self.consumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.consumBtn.setGeometry(QtCore.QRect(0, 490, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.consumBtn.setFont(font)
        self.consumBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.consumBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #B672EA;\n"
"}")
        self.consumBtn.setObjectName("consumBtn")
        self.priceBtn = QtWidgets.QPushButton(self.centralwidget)
        self.priceBtn.setGeometry(QtCore.QRect(0, 560, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.priceBtn.setFont(font)
        self.priceBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.priceBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #B672EA;\n"
"}")
        self.priceBtn.setObjectName("priceBtn")
        self.finanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.finanBtn.setGeometry(QtCore.QRect(0, 630, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.finanBtn.setFont(font)
        self.finanBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.finanBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #B672EA;\n"
"}")
        self.finanBtn.setObjectName("finanBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 40, 1571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 10, 111, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(1770, 10, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(450, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.addBtn.setFont(font)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.addBtn.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: #B672EA;\n"
"}")
        self.addBtn.setObjectName("addBtn")
        self.searchTxt = QtWidgets.QTextEdit(self.centralwidget)
        self.searchTxt.setGeometry(QtCore.QRect(1550, 100, 321, 51))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.searchTxt.setFont(font)
        self.searchTxt.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.searchTxt.setStyleSheet("QTextEdit{\n"
"background-color: #B672EA;\n"
"border-radius: 15px;\n"
"}")
        self.searchTxt.setObjectName("searchTxt")
        self.editBtn = QtWidgets.QPushButton(self.centralwidget)
        self.editBtn.setGeometry(QtCore.QRect(720, 90, 251, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.editBtn.setFont(font)
        self.editBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.editBtn.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: #B672EA;\n"
"}")
        self.editBtn.setObjectName("editBtn")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(1000, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.delBtn.setFont(font)
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delBtn.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: #B672EA;\n"
"}\n"
"")
        self.delBtn.setObjectName("delBtn")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(440, 190, 1431, 761))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.recordsBtn.setText(_translate("MainWindow", " Записи"))
        self.clienBtn.setText(_translate("MainWindow", "Клиенты"))
        self.consumBtn.setText(_translate("MainWindow", "Расходные материалы"))
        self.priceBtn.setText(_translate("MainWindow", "Прайс-лист"))
        self.finanBtn.setText(_translate("MainWindow", "Финансы"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.addBtn.setText(_translate("MainWindow", "+ Добавить"))
        self.searchTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'News Cycle\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.searchTxt.setPlaceholderText(_translate("MainWindow", "🔍  Поиск..."))
        self.editBtn.setText(_translate("MainWindow", "✎ Редактировать"))
        self.delBtn.setText(_translate("MainWindow", "🗑 Удалить"))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(554, 314)
        self.saveBtn = QtWidgets.QPushButton(Dialog)
        self.saveBtn.setGeometry(QtCore.QRect(190, 250, 171, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.saveBtn.setFont(font)
        self.saveBtn.setObjectName("saveBtn")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 20, 401, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(220, 80, 113, 22))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(220, 120, 113, 22))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(220, 160, 113, 22))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_4.setGeometry(QtCore.QRect(220, 200, 113, 22))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.saveBtn.setText(_translate("Dialog", "Сохранить"))
        self.label.setText(_translate("Dialog", "Введите данные о новой записи "))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
