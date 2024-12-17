from logging import disable
from DelConsum import DelConsum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import QDate
from designeFinance import Ui_MainWindow
import sys
import datetime

class WindowFinance(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowFinance, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.period.addItem("День")
        self.ui.period.addItem("Неделя")
        self.ui.period.addItem("Месяц")
        self.ui.period.addItem("Год")

        self.ui.type.addItem("Выручка")
        self.ui.type.addItem("Прибыль")
        self.ui.type.addItem("Расходы")

        self.ui.displayType.addItem("График")
        self.ui.displayType.addItem("Диаграмма")
        self.ui.displayType.addItem("Гистограмма")

        self.ui.clientBtn.clicked.connect(self.show_clients)
        # self.ui.recordsBtn.clicked.connect(self.show_notes)
        # self.ui.consumBtn.clicked.connect(self.show_consum)
        # self.ui.priceBtn.clicked.connect(self.show_price)
        # self.ui.expBtn.clicked.connect(self.show_exp)
        # self.ui.finanBtn.clicked.connect(self.show_finance)

        self.ui.calendar.selectionChanged.connect(self.update_date_label)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных")
            return

        date_today = datetime.date.today()
        formatted_date = date_today.strftime("%d.%m.%Y")
        self.ui.labelDate.setText(f"{formatted_date}")

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

    def show_clients(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            # self.window.show_clients()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

