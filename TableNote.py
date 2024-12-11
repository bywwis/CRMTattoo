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
                   Запись.Время,
                   Запись.IDклиента,
                   Запись.IDуслуги,
                   Запись.ID
            FROM Запись
            JOIN Клиенты ON Запись.IDклиента = Клиенты.ID
            JOIN Услуги ON Запись.IDуслуги = Услуги.ID
        """, self.db)

        while query.next():
            row_data = []
            for i in range(query.record().count()):
                row_data.append(query.value(i))
            self.data_list.append(tuple(row_data))

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.data_list)

    def columnCount(self, parent=QtCore.QModelIndex()):
        return len(self.headers)

    def data(self, index, role=QtCore.Qt.DisplayRole):
        if role == QtCore.Qt.DisplayRole:
            return self.data_list[index.row()][index.column()]

    def setData(self, index, value, role=QtCore.Qt.EditRole):
        if role == QtCore.Qt.EditRole:
            row = index.row()
            col = index.column()

            self.data_list[row] = list(self.data_list[row])
            self.data_list[row][col] = value
            self.data_list[row] = tuple(self.data_list[row])

            query = QSqlQuery(self.db)
            if col == 0:
                try:
                    query.prepare("UPDATE Клиенты SET Имя=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                except Exception as e:
                    print(e)
            elif col == 1:
                try:
                    query.prepare("UPDATE Клиенты SET Телефон=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                except Exception as e:
                    print(e)
            elif col == 2:
                try:
                    query.prepare("UPDATE Услуги SET Наименование=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_service_id(row))
                except Exception as e:
                    print(e)
            elif col == 3:
                try:
                    query.prepare("UPDATE Запись SET Дата=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_record_id(row))
                except Exception as e:
                    print(e)
            elif col == 4:  # Время
                try:
                    query.prepare("UPDATE Запись SET Время=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_record_id(row))
                except Exception as e:
                    print(e)

            if not query.exec_():
                print(f"Ошибка выполнения запроса: {query.lastError().text()}")

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

    def get_client_id(self, row):
        return self.data_list[row][5]

    def get_service_id(self, row):
        return self.data_list[row][6]

    def get_record_id(self, row):
        return self.data_list[row][7]

    def insert_row_note(self):
        queries = [
            'INSERT INTO Клиенты (Имя, Телефон) VALUES ("", "")',
            'INSERT INTO Услуги (Наименование) VALUES ("")',
            'INSERT INTO Запись (IDклиента, IDуслуги, Дата, Время) ' \
            'VALUES ((SELECT MAX(ID) FROM Клиенты), ' \
                    '(SELECT MAX(ID) FROM Услуги), "", "")'
        ]

        for query_str in queries:
            query = QSqlQuery(self.db)
            if not query.exec_(query_str):
                print(f"Ошибка выполнения запроса: {query.lastError().text()}")
                break

    def delete_row_note(self, row):
        id_row = self.data_list[row][7]
        query = QSqlQuery(self.db)
        query.prepare(
            f"""DELETE FROM Запись WHERE ID = {id_row}""")
        if not query.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку.")
        else:
            self.load_data()