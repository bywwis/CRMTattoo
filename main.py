from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime

class TableNote(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableNote, self).__init__()
        self.db = db
        self.data_list = []
        self.headers = ["Имя", "Номер телефона", "Название услуги", "Дата", "Время"]

        self.load_data()

    def load_data(self):
        query = QSqlQuery("""
            SELECT Клиенты.Имя, 
                   Клиенты.Телефон, 
                   Услуги.Наименование, 
                   Запись.Дата, 
                   Запись.Время 
            FROM Запись
            JOIN Клиенты ON Запись.IDклиента = Клиенты.ID
            JOIN Услуги ON Запись.IDуслуги = Услуги.ID
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(row_data)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

class TableClients(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableClients, self).__init__()
        self.db = db
        self.data_list = []
        self.headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

        self.load_data()

    def load_data(self):
        query = QSqlQuery("""
            SELECT Фамилия, 
                   Имя, 
                   Отчество,
                   Телефон 
            FROM Клиенты
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(row_data)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

class TableConsum(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableConsum, self).__init__()
        self.db = db
        self.data_list = []
        self.headers = ["Наименование", "Стоимость", "Количество в наличии", "Единицы измерения"]

        self.load_data()

    def load_data(self):
        query = QSqlQuery("""
            SELECT Наименование, 
                   СтоимостьШтуки, 
                   КоличествоВНаличии,
                   ЕдиницыИзмерения 
            FROM РасходныеМатериалы
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(row_data)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

class TablePrice(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TablePrice, self).__init__()
        self.db = db
        self.data_list = []
        self.headers = ["Название услуги", "Стоимость"]

        self.load_data()

    def load_data(self):
        query = QSqlQuery("""
            SELECT Наименование, 
                   Цена
            FROM Услуги
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(row_data)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

class TableExp(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableExp, self).__init__()
        self.db = db
        self.data_list = []
        self.headers = ["Название услуги", "Наименование материала", "Расход материала", "Единицы измерения"]

        self.load_data()

    def load_data(self):
        query = QSqlQuery("""
            SELECT Услуги.Наименование, 
                   РасходныеМатериалы.Наименование, 
                   УслугиРасходныеМатериалы.РасходМатериала,
                   УслугиРасходныеМатериалы.ЕдиницыИзмерения 
            FROM УслугиРасходныеМатериалы
            JOIN Услуги ON УслугиРасходныеМатериалы.IDУслуги = Услуги.ID
            JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(row_data)

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if index.isValid() and role == QtCore.Qt.EditRole:
            self.data_list[index.row()][index.column()] = value
            self.dataChanged.emit(index, index)
            return True
        return False

    def flags(self, index):
        if not index.isValid():
            return QtCore.Qt.ItemIsEnabled
        return QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEditable | QtCore.Qt.ItemIsEnabled

    def headerData(self, section, orientation, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.headers[section]

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
        self.model.data_list.append(["" for _ in range(self.model.columnCount())])
        self.model.layoutChanged.emit()




class DialogDelNote(QtWidgets.QDialog):
    def __init__(self):
        super(DialogDelNote, self).__init__()
        self.ui4 = Ui_DialogDelNote()
        self.ui4.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
