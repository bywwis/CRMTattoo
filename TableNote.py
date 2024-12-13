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
        self.id_list = []
        self.headers = ["Имя", "Номер телефона", "Название услуги", "Дата", "Время"]

        self.load_data()

    def load_data(self):
        self.beginResetModel()

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

        self.data_list.clear()
        self.id_list.clear()

        while query.next():
            display_row = []
            id_row = []

            for i in range(query.record().count()):
                if i < 5:
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
            field_name = self.headers[col]

            if col == 0:
                try:
                    query.prepare("UPDATE Клиенты SET Имя=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_client_id(row))
                    if not query.exec_():
                        print(f"Ошибка выполнения запроса на обновление имени: {query.lastError().text()}")
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

    def get_service_id(self, row):
        return self.id_list[row][1]

    def get_record_id(self, row):
        return self.id_list[row][2]

    def insert_row_note(self):
        queries = [
            'INSERT INTO Клиенты (Имя, Телефон) VALUES ("", "")',
            'INSERT INTO Услуги (Наименование) VALUES ("")',
            'INSERT INTO Запись (IDклиента, IDуслуги, Дата, Время) '
            'VALUES ((SELECT MAX(ID) FROM Клиенты), '
            '(SELECT MAX(ID) FROM Услуги), "", "")'
        ]

        client_id = None
        service_id = None
        record_id = None

        query = QSqlQuery(self.db)

        if not query.exec_(queries[0]):
            print(f"Ошибка выполнения запроса на вставку клиента: {query.lastError().text()}")
            return
        client_id = query.lastInsertId()
        if not query.exec_(queries[1]):
            print(f"Ошибка выполнения запроса на вставку услуги: {query.lastError().text()}")
            return
        service_id = query.lastInsertId()
        if not query.exec_(queries[2]):
            print(f"Ошибка выполнения запроса на вставку записи: {query.lastError().text()}")
            return
        record_id = query.lastInsertId()

        self.id_list.append([client_id, service_id, record_id])

    def delete_row_note(self, row):
        id_row = self.id_list[row][2]
        query = QSqlQuery(self.db)
        query.prepare(
            f"""DELETE FROM Запись WHERE ID = {id_row}""")
        if not query.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку.")

    def search_row_note(self, search_text):
        try:
            if search_text == "":
                self.load_data()
            else:
                self.beginResetModel()

                query = QSqlQuery(self.db)
                query.prepare("""
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
                               WHERE Клиенты.Имя LIKE ? OR Клиенты.Телефон LIKE ? OR Услуги.Наименование LIKE ?
                              """)

                name = f"%{search_text}%"
                phone = f"%{search_text}%"
                service = f"%{search_text}%"
                record_date = f"%{search_text}%"
                record_time = f"%{search_text}%"
                query.addBindValue(name)
                query.addBindValue(phone)
                query.addBindValue(service)

                if not query.exec_():
                    print(f"Ошибка выполнения запроса: {query.lastError().text()}")
                else:
                    self.data_list.clear()
                    self.id_list.clear()

                while query.next():
                    display_row = []
                    id_row = []

                    for i in range(query.record().count()):
                        if i < 5:
                            display_row.append(query.value(i))
                        else:
                            id_row.append(query.value(i))

                    self.data_list.append(display_row)
                    self.id_list.append(id_row)

                self.endResetModel()

        except Exception as e:
            print("Ошибка поиска: ", e)

    def load_filtered_data(self, period, start_date=None, end_date=None):
        try:
            self.beginResetModel()
            query = QSqlQuery(self.db)

            if period == "Месяц":
                month = start_date.split('.')[1]
                year = start_date.split('.')[2]
                query.prepare("""
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
                    WHERE substr(Запись.Дата, 4, 2) = ? AND substr(Запись.Дата, 7, 4) = ?
                """)
                query.addBindValue(month)
                query.addBindValue(year)

            elif period == "Год":
                year = start_date.split('.')[2]
                query.prepare("""
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
                    WHERE substr(Запись.Дата, 7, 4) = ?
                """)
                query.addBindValue(year)

            else:
                query.prepare("""
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
                    if i < 5:
                        display_row.append(query.value(i))
                    else:
                        id_row.append(query.value(i))

                self.data_list.append(display_row)
                self.id_list.append(id_row)

            self.endResetModel()

        except Exception as e:
            print("Ошибка фильтрации данных в бд: ", e)

