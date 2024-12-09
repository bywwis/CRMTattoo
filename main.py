from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime
from TableNote import TableNote
from TableClients import TableClients
from TableConsum import TableConsum
from TablePrice import TablePrice
from TableExp import TableExp
from DelNote import DelNote


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.period.addItem("День")
        self.ui.period.addItem("Неделя")
        self.ui.period.addItem("Месяц")
        self.ui.period.addItem("Год")

        self.ui.clientBtn.clicked.connect(self.show_clients)
        self.ui.recordsBtn.clicked.connect(self.show_notes)
        self.ui.consumBtn.clicked.connect(self.show_consum)
        self.ui.priceBtn.clicked.connect(self.show_price)
        self.ui.expBtn.clicked.connect(self.show_exp)

        self.ui.addBtn.clicked.connect(self.add_row)
        self.ui.delBtn.clicked.connect(self.open_dialogDelNote)
        self.ui.hintBtn.setToolTip("Для того, чтобы отредактировать данные, кликните дважды по ячейке таблицы")
        self.ui.calendar.selectionChanged.connect(self.update_date_label)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных")
            return

        self.model = TableNote(self.db)
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        date_today = datetime.date.today()
        formatted_date = date_today.strftime("%d.%m.%Y")
        self.ui.labelDate.setText(f"{formatted_date}")

    def show_clients(self):
        self.ui.clientBtn.setStyleSheet("border: none; border-radius: 25px; background-color: #99AAD2;")
        self.ui.recordsBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.consumBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.priceBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.expBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.finanBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")

        self.ui.labelDate.show()
        self.ui.line.show()
        self.ui.period.show()

        self.model = TableClients(self.db)
        self.ui.tableView.setModel(self.model)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def show_notes(self):
        self.ui.recordsBtn.setStyleSheet("border: none; border-radius: 25px; background-color: #99AAD2;")
        self.ui.clientBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.consumBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.priceBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.expBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.finanBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")

        self.ui.labelDate.show()
        self.ui.line.show()
        self.ui.period.show()

        self.model = TableNote(self.db)
        self.ui.tableView.setModel(self.model)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def show_consum(self):
        self.ui.consumBtn.setStyleSheet("border: none; border-radius: 25px; background-color: #99AAD2;")
        self.ui.clientBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.recordsBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.priceBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.expBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.finanBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")

        self.ui.labelDate.hide()
        self.ui.line.hide()
        self.ui.period.hide()

        self.model = TableConsum(self.db)
        self.ui.tableView.setModel(self.model)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def show_price(self):
        self.ui.priceBtn.setStyleSheet("border: none; border-radius: 25px; background-color: #99AAD2;")
        self.ui.clientBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.recordsBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.consumBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.expBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.finanBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")

        self.ui.labelDate.hide()
        self.ui.line.hide()
        self.ui.period.hide()

        self.model = TablePrice(self.db)
        self.ui.tableView.setModel(self.model)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def show_exp(self):
        self.ui.expBtn.setStyleSheet("border: none; border-radius: 25px; background-color: #99AAD2;")
        self.ui.clientBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.recordsBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.consumBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.priceBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")
        self.ui.finanBtn.setStyleSheet(
            "QPushButton:hover {border: none; border-radius: 25px; background-color: #99AAD2;}")

        self.ui.labelDate.hide()
        self.ui.line.hide()
        self.ui.period.hide()

        self.model = TableExp(self.db)
        self.ui.tableView.setModel(self.model)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def open_dialogDelNote(self):
        self.dialog = DialogDelNote()
        self.dialog.show()

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

    def add_row(self):
        try:
            self.model.beginInsertRows(QtCore.QModelIndex(), self.model.rowCount(), self.model.rowCount())
            self.model.data_list.append(["" for _ in range(self.model.columnCount())])
            self.model.endInsertRows()
        except Exception as e:
            QMessageBox.critical(self, "Ошибка", f"Ошибка при добавлении строки: {e}")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
