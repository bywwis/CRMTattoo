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

    def save_to_database_note(self):
        try:
            # Запрос для добавления клиента
            add_client_query = QSqlQuery(self.db)
            add_client_query.prepare("""
                INSERT INTO Клиенты (Фамилия, Имя, Отчество, Телефон)
                VALUES (:Фамилия, :Имя, :Отчество, :Телефон)
            """)

            # Запрос для добавления услуги
            add_service_query = QSqlQuery(self.db)
            add_service_query.prepare("""
                INSERT INTO Услуги (Наименование, Цена)
                VALUES (:Наименование, :Цена)
            """)

            # Запрос для поиска существующей записи
            find_record_query = QSqlQuery(self.db)
            find_record_query.prepare("""
                SELECT ID
                FROM Запись
                WHERE IDклиента = :IDклиента 
                  AND IDуслуги = :IDуслуги 
                  AND Дата = :Дата 
                  AND Время = :Время
            """)

            # Запрос для обновления записи
            update_record_query = QSqlQuery(self.db)
            update_record_query.prepare("""
                UPDATE Запись
                SET Дата = :Дата, Время = :Время
                WHERE ID = :ID
            """)

            # Запрос для добавления новой записи
            insert_record_query = QSqlQuery(self.db)
            insert_record_query.prepare("""
                INSERT INTO Запись (IDклиента, IDуслуги, Дата, Время)
                VALUES (:IDклиента, :IDуслуги, :Дата, :Время)
            """)

            for row in self.data_list:
                client_name = row[0]
                phone_number = row[1]
                service_name = row[2]
                record_date = row[3]
                record_time = row[4]

                # Получение или добавление клиента
                get_client_id_query = QSqlQuery(self.db)
                get_client_id_query.prepare("""
                    SELECT ID FROM Клиенты WHERE Имя = :Имя AND Телефон = :Телефон
                """)
                get_client_id_query.addBindValue(client_name)
                get_client_id_query.addBindValue(phone_number)

                if not get_client_id_query.exec_() or not get_client_id_query.first():
                    # Клиент не найден, добавляем нового
                    add_client_query.addBindValue(None)
                    add_client_query.addBindValue(client_name)
                    add_client_query.addBindValue(None)
                    add_client_query.addBindValue(phone_number)
                    if not add_client_query.exec_():
                        raise RuntimeError(f"Не удалось добавить клиента: {add_client_query.lastError().text()}")
                    client_id = add_client_query.lastInsertId()
                else:
                    # Получаем ID найденного клиента
                    client_id = get_client_id_query.value(0)

                # Получение или добавление услуги
                get_service_id_query = QSqlQuery(self.db)
                get_service_id_query.prepare("""
                    SELECT ID FROM Услуги WHERE Наименование = :Наименование
                """)
                get_service_id_query.addBindValue(service_name)

                if not get_service_id_query.exec_() or not get_service_id_query.first():
                    # Услуга не найдена, добавляем новую
                    add_service_query.addBindValue(service_name)
                    add_service_query.addBindValue(None)
                    if not add_service_query.exec_():
                        raise RuntimeError(f"Не удалось добавить услугу: {add_service_query.lastError().text()}")
                    service_id = add_service_query.lastInsertId()
                else:
                    # Получаем ID найденной услуги
                    service_id = get_service_id_query.value(0)

                # Проверка наличия записи
                find_record_query.addBindValue(client_id)
                find_record_query.addBindValue(service_id)
                find_record_query.addBindValue(record_date)
                find_record_query.addBindValue(record_time)

                if find_record_query.exec_() and find_record_query.first():
                    # Обновление существующей записи
                    record_id = find_record_query.value(0)
                    update_record_query.addBindValue(record_date)
                    update_record_query.addBindValue(record_time)
                    update_record_query.addBindValue(record_id)
                    if not update_record_query.exec_():
                        raise RuntimeError(f"Не удалось обновить запись ID={record_id}")
                else:
                    # Добавление новой записи
                    insert_record_query.addBindValue(client_id)
                    insert_record_query.addBindValue(service_id)
                    insert_record_query.addBindValue(record_date)
                    insert_record_query.addBindValue(record_time)
                    if not insert_record_query.exec_():
                        raise RuntimeError("Не удалось сохранить новую запись.")

        except Exception as e:
            print(e)
            QMessageBox.critical(self, "Ошибка", f"Ошибка сохранения: {e}")

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
            self.save_to_database_note()
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


