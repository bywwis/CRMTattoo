from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Finance(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1952, 1081)
        MainWindow.setStyleSheet("\n"
"background-color: #DCD6DC;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(0, 0, 401, 341))
        self.calendar.setStyleSheet(" font: 12pt \"News Cycle\";\n"
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
        self.recordsBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #99AAD2;\n"
"}")
        self.recordsBtn.setObjectName("recordsBtn")
        self.clientBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clientBtn.setGeometry(QtCore.QRect(0, 420, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.clientBtn.setFont(font)
        self.clientBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.clientBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #99AAD2;\n"
"}")
        self.clientBtn.setObjectName("clientBtn")
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
        self.finanBtn.setGeometry(QtCore.QRect(0, 700, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.finanBtn.setFont(font)
        self.finanBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.finanBtn.setStyleSheet("QPushButton{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #99AAD2;\n"
"}\n"
"\n"
"")
        self.finanBtn.setObjectName("finanBtn")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(410, 110, 1571, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.reportBtn = QtWidgets.QPushButton(self.centralwidget)
        self.reportBtn.setGeometry(QtCore.QRect(1590, 40, 241, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(16)
        self.reportBtn.setFont(font)
        self.reportBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.reportBtn.setStyleSheet("QPushButton{\n"
"border-radius: 15px;\n"
"background-color: #AAB1C1;\n"
"}")
        self.reportBtn.setObjectName("reportBtn")
        self.period = QtWidgets.QComboBox(self.centralwidget)
        self.period.setGeometry(QtCore.QRect(700, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.period.setFont(font)
        self.period.setObjectName("period")
        self.labelDate = QtWidgets.QLabel(self.centralwidget)
        self.labelDate.setGeometry(QtCore.QRect(430, 40, 221, 41))
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
        self.expBtn = QtWidgets.QPushButton(self.centralwidget)
        self.expBtn.setGeometry(QtCore.QRect(0, 630, 401, 71))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(24)
        self.expBtn.setFont(font)
        self.expBtn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.expBtn.setStyleSheet("QPushButton:hover{\n"
"border: none;\n"
"border-radius: 25px;\n"
"background-color: #99AAD2;\n"
"}")
        self.expBtn.setObjectName("expBtn")
        self.type = QtWidgets.QComboBox(self.centralwidget)
        self.type.setGeometry(QtCore.QRect(990, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.type.setFont(font)
        self.type.setObjectName("type")
        self.displayType = QtWidgets.QComboBox(self.centralwidget)
        self.displayType.setGeometry(QtCore.QRect(1280, 40, 231, 41))
        font = QtGui.QFont()
        font.setFamily("News Cycle")
        font.setPointSize(14)
        self.displayType.setFont(font)
        self.displayType.setObjectName("displayType")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(460, 160, 981, 851))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableViewFinance = QtWidgets.QTableView(self.centralwidget)
        self.tableViewFinance.setGeometry(QtCore.QRect(1470, 160, 391, 851))
        self.tableViewFinance.setStyleSheet("QTableView {\n"
"  border:none;\n"
"  border-top:2px solid #99AAD2; \n"
"  border-radius: 5px;\n"
"  gridline-color: #99AAD2; \n"
"  border-left: 2px solid #99AAD2; \n"
"  border-right: 2px solid #99AAD2; \n"
"  border-bottom:2px solid #99AAD2; \n"
"  color: rgb(0, 0, 0);  \n"
"  font: 12pt \"News Cycle\";\n"
"  }\n"
"\n"
"QTableView::item {\n"
"    border-bottom:1px solid #99AAD2; \n"
"    border-left: 0.5px solid #99AAD2; \n"
"}\n"
" \n"
"QTableView::item:selected {\n"
"  background-color: #AAB1C1;\n"
" }\n"
"\n"
"QHeaderView::section {\n"
"  border: none;\n"
"  border-bottom: 2px solid #99AAD2; \n"
"  background-color: #bcc7e0; \n"
"  border-left: 0.5px solid #99AAD2; \n"
"  border-right: 0.5px solid #99AAD2;\n"
"  color: rgb(0, 0, 0);\n"
"  font: 14pt \"News Cycle\";\n"
"  padding: 3px;\n"
"}\n"
"\n"
"QHeaderView::down-arrow {\n"
"  width: 26px; \n"
"  height:18px; \n"
"  subcontrol-position: bottom right; \n"
"}")
        self.tableViewFinance.setObjectName("tableViewFinance")
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
        self.clientBtn.setText(_translate("MainWindow", "Клиенты"))
        self.consumBtn.setText(_translate("MainWindow", "Расходные материалы"))
        self.priceBtn.setText(_translate("MainWindow", "Прайс-лист"))
        self.finanBtn.setText(_translate("MainWindow", "Финансы"))
        self.reportBtn.setText(_translate("MainWindow", "Сохранить отчёт"))
        self.expBtn.setText(_translate("MainWindow", "Расход материалов"))
