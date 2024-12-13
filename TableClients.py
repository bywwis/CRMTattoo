from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime

class TableClients(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableClients, self).__init__()
        self.db = db
        self.data_list = []
        self.id_list = []
        self.headers = ["Фамилия", "Имя", "Отчество", "Номер телефона"]

        self.load_data()

    def load_data(self):
        self.beginResetModel()

        query = QSqlQuery("""
            SELECT Фамилия, 
                   Имя, 
                   Отчество,
                   Телефон,
                   ID 
            FROM Клиенты
        """, self.db)

        self.data_list.clear()
        self.id_list.clear()

        while query.next():
            display_row = []
            id_row = []

            for i in range(query.record().count()):
                if i < 4:
                    display_row.append(query.value(i))
                else:
                    id_row.append(query.value(i))

            self.data_list.append(display_row)
            self.id_list.append(id_row)
        self.endResetModel()

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
                    query.prepare("UPDATE Клиенты SET Фамилия=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                    if not query.exec_():
                        print(f"Ошибка выполнения запроса на обновление имени: {query.lastError().text()}")
                except Exception as e:
                    print(e)
            elif col == 1:
                try:
                    query.prepare("UPDATE Клиенты SET Имя=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                except Exception as e:
                    print(e)
            elif col == 2:
                try:
                    query.prepare("UPDATE Клиенты SET Отчество=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                except Exception as e:
                    print(e)
            elif col == 3:
                try:
                    query.prepare("UPDATE Клиенты SET Телефон=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                except Exception as e:
                    print(e)

            if not query.exec_():
                print(f"Ошибка выполнения запроса на обновление: {query.lastError().text()}")

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
        return self.id_list[row][0]

    def insert_row_clients(self):
        queries = [
            'INSERT INTO Клиенты (Фамилия, Имя, Отчество, Телефон) VALUES ("", "", "", "")',
        ]

        client_id = None

        query = QSqlQuery(self.db)

        if not query.exec_(queries[0]):
            print(f"Ошибка выполнения запроса на вставку клиента: {query.lastError().text()}")
            return
        client_id = query.lastInsertId()

        self.id_list.append([client_id])

    def delete_row_clients(self, row):
        id_row = self.get_client_id(row)
        query = QSqlQuery(self.db)
        query.prepare(
            f"""DELETE FROM Клиенты WHERE ID = {id_row}""")
        if not query.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку в таблице Клиенты.")
        self.load_data()

    def search_row_clients(self, search_text):
        try:
            if search_text == "":
                self.load_data()
            else:
                self.beginResetModel()

                query = QSqlQuery(self.db)
                query.prepare(""" 
                                SELECT  Фамилия, 
                                        Имя, 
                                        Отчество,
                                        Телефон,
                                        ID 
                                FROM Клиенты
                               WHERE Фамилия LIKE ? OR Имя LIKE ? OR Отчество LIKE ? OR Телефон LIKE ?
                              """)

                name = f"%{search_text}%"
                surname = f"%{search_text}%"
                patronymic = f"%{search_text}%"
                phone = f"%{search_text}%"
                query.addBindValue(name)
                query.addBindValue(surname)
                query.addBindValue(patronymic)
                query.addBindValue(phone)

                if not query.exec_():
                    print(f"Ошибка выполнения запроса: {query.lastError().text()}")
                else:
                    self.data_list.clear()
                    self.id_list.clear()

                while query.next():
                    display_row = []
                    id_row = []

                    for i in range(query.record().count()):
                        if i < 4:
                            display_row.append(query.value(i))
                        else:
                            id_row.append(query.value(i))

                    self.data_list.append(display_row)
                    self.id_list.append(id_row)

                self.endResetModel()

        except Exception as e:
            print("Ошибка поиска: ", e)

    def load_filtered_data_clients(self, period, start_date=None, end_date=None):
        try:
            self.beginResetModel()
            query = QSqlQuery(self.db)

            if period == "Месяц":
                month = start_date.split('.')[1]
                year = start_date.split('.')[2]
                query.prepare("""
                    SELECT  Клиенты.Фамилия, 
                            Клиенты.Имя, 
                            Клиенты.Отчество,
                            Клиенты.Телефон,
                            Клиенты.ID,
                            Запись.ID,
                            Запись.Дата 
                    FROM Клиенты
                    JOIN Запись ON Запись.IDклиента = Клиенты.ID
                    WHERE substr(Запись.Дата, 4, 2) = ? AND substr(Запись.Дата, 7, 4) = ?
                """)
                query.addBindValue(month)
                query.addBindValue(year)

            elif period == "Год":
                year = start_date.split('.')[2]
                query.prepare("""
                    SELECT  Клиенты.Фамилия, 
                            Клиенты.Имя, 
                            Клиенты.Отчество,
                            Клиенты.Телефон,
                            Клиенты.ID,
                            Запись.ID,
                            Запись.Дата 
                    FROM Клиенты
                    JOIN Запись ON Запись.IDклиента = Клиенты.ID
                    WHERE substr(Запись.Дата, 7, 4) = ?
                """)
                query.addBindValue(year)

            else:
                query.prepare("""
                   SELECT  Клиенты.Фамилия, 
                            Клиенты.Имя, 
                            Клиенты.Отчество,
                            Клиенты.Телефон,
                            Клиенты.ID,
                            Запись.ID,
                            Запись.Дата 
                    FROM Клиенты
                    JOIN Запись ON Запись.IDклиента = Клиенты.ID
                    WHERE Запись.Дата BETWEEN ? AND ?
                """)
                query.addBindValue(start_date)
                query.addBindValue(end_date)

            if not query.exec_():
                print("Ошибка выполнения запроса на фильтрацию данных:", query.lastError().text())

            self.data_list.clear()
            self.id_list.clear()

            while query.next():
                display_row = []
                id_row = []

                for i in range(query.record().count()):
                    if i < 4:
                        display_row.append(query.value(i))
                    else:
                        id_row.append(query.value(i))

                self.data_list.append(display_row)
                self.id_list.append(id_row)

            self.endResetModel()

        except Exception as e:
            print("Ошибка фильтрации данных в бд: ", e)

