# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1952, 1141)
        MainWindow.setStyleSheet("\n"
"background-color: #DCD6DC;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 401, 341))
        self.calendar.setStyleSheet("font: 12pt \"News Cycle\";\n"
"selection-background-color: #99AAD2;")
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
"background-color: #99AAD2;\n"
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
"background-color: #99AAD2;\n"
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
"background-color: #99AAD2;\n"
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
"background-color: #99AAD2;\n"
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
"background-color: #99AAD2;\n"
"}")
        self.finanBtn.setObjectName("finanBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 60, 1571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setGeometry(QtCore.QRect(450, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.addBtn.setFont(font)
        self.addBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.addBtn.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: #AAB1C1;\n"
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
"background-color: #AAB1C1;\n"
"border-radius: 20px;\n"
"}")
        self.searchTxt.setObjectName("searchTxt")
        self.delBtn = QtWidgets.QPushButton(self.centralwidget)
        self.delBtn.setGeometry(QtCore.QRect(750, 90, 241, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(18)
        self.delBtn.setFont(font)
        self.delBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.delBtn.setStyleSheet("QPushButton{\n"
"border-radius: 20px;\n"
"background-color: #AAB1C1;\n"
"}\n"
"")
        self.delBtn.setObjectName("delBtn")
        self.tableViewNote = QtWidgets.QTableView(self.centralwidget)
        self.tableViewNote.setGeometry(QtCore.QRect(460, 180, 1431, 841))
        self.tableViewNote.setStyleSheet("QTableView {\n"
"border-color: #B672EA\n"
"}")
        self.tableViewNote.setGridStyle(QtCore.Qt.CustomDashLine)
        self.tableViewNote.setObjectName("tableViewNote")
        self.period = QtWidgets.QComboBox(self.centralwidget)
        self.period.setGeometry(QtCore.QRect(1660, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.period.setFont(font)
        self.period.setObjectName("period")
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        self.labelDate.setGeometry(QtCore.QRect(460, 10, 221, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.labelDate.setFont(font)
        self.labelDate.setStyleSheet("color: #2E2E2E;\n"
"background-color: #99AAD2;\n"
"border-radius: 15px;\n"
"")
        self.labelDate.setText("")
        self.labelDate.setAlignment(QtCore.Qt.AlignCenter)
        self.labelDate.setObjectName("labelDate")
        self.hintBtn = QtWidgets.QToolButton(self.centralwidget)
        self.hintBtn.setGeometry(QtCore.QRect(1050, 90, 61, 61))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.hintBtn.setFont(font)
        self.hintBtn.setStyleSheet("QToolButton{\n"
"border-radius: 30px;\n"
"background-color: #AAB1C1;\n"
"}")
        self.hintBtn.setObjectName("hintBtn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.period.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.recordsBtn.setText(_translate("MainWindow", " Записи"))
        self.clienBtn.setText(_translate("MainWindow", "Клиенты"))
        self.consumBtn.setText(_translate("MainWindow", "Расходные материалы"))
        self.priceBtn.setText(_translate("MainWindow", "Прайс-лист"))
        self.finanBtn.setText(_translate("MainWindow", "Финансы"))
        self.addBtn.setText(_translate("MainWindow", "Добавить"))
        self.searchTxt.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'News Cycle\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.searchTxt.setPlaceholderText(_translate("MainWindow", "    Поиск..."))
        self.delBtn.setText(_translate("MainWindow", "Удалить"))
        self.hintBtn.setText(_translate("MainWindow", "?"))
