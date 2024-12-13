from logging import disable

from DelConsum import DelConsum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5.QtCore import QDate
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
from dialogDelClients import Ui_Dialog
from dialogDelConsum import Ui_Dialog
from dialogDelPrice import Ui_Dialog
from dialogDelExp import Ui_Dialog
import sys
import datetime
from TableNote import TableNote
from TableClients import TableClients
from TableConsum import TableConsum
from TablePrice import TablePrice
from TableExp import TableExp
from DelNote import DelNote
from DelClients import DelClients
from DelConsum import DelConsum
from DelPrice import DelPrice
from DelExp import DelExp


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
        self.ui.delBtn.clicked.connect(self.open_dialog)
        self.ui.hintBtn.setToolTip("Для того, чтобы отредактировать данные, кликните дважды по ячейке таблицы")

        self.ui.calendar.selectionChanged.connect(self.update_date_label)
        self.ui.period.currentIndexChanged.connect(self.on_period_changed)

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

        self.ui.searchTxt.textChanged.connect(lambda: self.search_text(self.ui.searchTxt.toPlainText()))

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
        self.ui.tableView.verticalHeader().setVisible(False)

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
        self.ui.tableView.verticalHeader().setVisible(False)

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
        self.ui.tableView.verticalHeader().setVisible(False)

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
        self.ui.tableView.verticalHeader().setVisible(False)

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def open_dialog(self):
        try:
            index = self.ui.tableView.currentIndex()
            if index.isValid():
                if isinstance(self.model, TableNote):
                    self.dialog = DelNote()
                elif isinstance(self.model, TableClients):
                    self.dialog = DelClients()
                elif isinstance(self.model, TableConsum):
                    self.dialog = DelConsum()
                elif isinstance(self.model, TableExp):
                    self.dialog = DelExp()
                elif isinstance(self.model, TablePrice):
                    self.dialog = DelPrice()
                result = self.dialog.exec_()
                if result == QtWidgets.QDialog.Accepted:
                    row = index.row()
                    if isinstance(self.model, TableNote):
                        self.model.delete_row_note(row)
                    elif isinstance(self.model, TableClients):
                        self.model.delete_row_clients(row)
                    elif isinstance(self.model, TableConsum):
                        self.model.delete_row_consum(row)
                    elif isinstance(self.model, TableExp):
                        self.model.delete_row_exp(row)
                    elif isinstance(self.model, TablePrice):
                        self.model.delete_row_price(row)
            else:
                QMessageBox.warning(self, "Предупреждение", "Сначала выберите строку для удаления.")
        except Exception as e:
            print('Ошибка удаления: ', e)

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

        self.on_period_changed(self.ui.period.currentIndex())

    def on_period_changed(self, index):
        try:
            period = self.ui.period.itemText(index)
            current_date = QDate.fromString(self.ui.labelDate.text(), "dd.MM.yyyy")

            if period == "День":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = start_date
            elif period == "Неделя":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addDays(7).toString("dd.MM.yyyy")
            elif period == "Месяц":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addMonths(1).toString("dd.MM.yyyy")
            elif period == "Год":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addYears(1).toString("dd.MM.yyyy")

            self.filter_table(start_date, end_date)

        except Exception as e:
            print("Ошибка смены периода:", e)

    def filter_table(self, start_date, end_date):
        if isinstance(self.model, TableNote):
            self.model.load_filtered_data_note(period=self.ui.period.currentText(),
                                               start_date=start_date,
                                               end_date=end_date)
        elif isinstance(self.model, TableClients):
            self.model.load_filtered_data_clients(period=self.ui.period.currentText(),
                                               start_date=start_date,
                                               end_date=end_date)

    def add_row(self):
        try:
            self.model.beginInsertRows(QtCore.QModelIndex(), self.model.rowCount(), self.model.rowCount())
            self.model.data_list.append(["" for _ in range(self.model.columnCount())])
            self.model.endInsertRows()
            if isinstance(self.model, TableNote):
                self.model.insert_row_note()
            elif isinstance(self.model, TableClients):
                self.model.insert_row_clients()
            elif isinstance(self.model, TableConsum):
                self.model.insert_row_consum()
            elif isinstance(self.model, TableExp):
                self.model.insert_row_exp()
            elif isinstance(self.model, TablePrice):
                self.model.insert_row_price()
        except Exception as e:
            print(f"Ошибка при добавлении строки: {e}")

    def search_text(self, search_text):
        try:
            if isinstance(self.model, TableNote):
                self.model.search_row_note(search_text)
            elif isinstance(self.model, TableClients):
                self.model.search_row_clients(search_text)
            elif isinstance(self.model, TableConsum):
                self.model.search_row_consum(search_text)
            elif isinstance(self.model, TableExp):
                self.model.search_row_exp(search_text)
            elif isinstance(self.model, TablePrice):
                self.model.search_row_price(search_text)
        except Exception as e:
            print("Ошибка ввода в строку для поиска: ", e)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showFullScreen()
    sys.exit(app.exec_())