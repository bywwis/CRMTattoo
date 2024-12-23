from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime

class TablePrice(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TablePrice, self).__init__()
        self.db = db
        self.data_list = []
        self.id_list = []
        self.headers = ["Название услуги", "Стоимость"]

        self.load_data()

    def load_data(self):
        self.beginResetModel()
        query = QSqlQuery("""
            SELECT Наименование, 
                   Цена,
                   ID
            FROM Услуги
        """, self.db)

        self.data_list.clear()
        self.id_list.clear()

        while query.next():
            display_row = []
            id_row = []

            for i in range(query.record().count()):
                if i < 2:
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
                    query.prepare("UPDATE Услуги SET Наименование=? WHERE ID=?")
                    query.addBindValue(value)
                    query.addBindValue(self.get_price_id(row))
                    if not query.exec_():
                        print(f"Ошибка выполнения запроса на обновление услуги: {query.lastError().text()}")
                except Exception as e:
                    print(e)
            elif col == 1:
                try:
                    if len(value) > 10:
                        print("Введено слишком много символов! Пожалуйста, введите менее 10.")
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle('Предупреждение')
                        msg_box.setText('Введено слишком много символов!')
                        msg_box.setInformativeText('Пожалуйста, введите менее 10.')
                        msg_box.setIcon(QMessageBox.Icon.Warning)
                        msg_box.exec()

                        value = ''
                        self.load_data()
                    else:
                        query.prepare("UPDATE Услуги SET Цена=? WHERE ID=?")
                        query.addBindValue(value)
                        query.addBindValue(self.get_price_id(row))
                        if not query.exec_():
                            print(f"Ошибка выполнения запроса на обновление цены: {query.lastError().text()}")
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

    def get_price_id(self, row):
        return self.id_list[row][0]

    def insert_row_price(self):
        queries = [
            'INSERT INTO Услуги (Наименование, Цена) '
            'VALUES ("", 0)',
        ]

        price_id = None

        query = QSqlQuery(self.db)

        if not query.exec_(queries[0]):
            print(f"Ошибка выполнения запроса на вставку материала: {query.lastError().text()}")
            return
        price_id = query.lastInsertId()

        self.id_list.append(price_id)

    def delete_row_price(self, row):
        id_row = self.get_price_id(row)
        query = QSqlQuery(self.db)
        query.prepare(
            f"""DELETE FROM Услуги WHERE ID = {id_row}""")
        if not query.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку в таблице услуги.")
        self.load_data()


    def search_row_price(self, search_text):
        try:
            if search_text == "":
                self.load_data()
            else:
                self.beginResetModel()

                query = QSqlQuery(self.db)
                query.prepare(""" 
                    SELECT  Наименование, 
                            Цена,
                            ID
                    FROM Услуги
                    WHERE Наименование LIKE ? OR Цена LIKE ? 
                    """)

                name = f"%{search_text}%"
                cost = f"%{search_text}%"
                query.addBindValue(name)
                query.addBindValue(cost)

                if not query.exec_():
                    print(f"Ошибка выполнения запроса: {query.lastError().text()}")
                else:
                    self.data_list.clear()
                    self.id_list.clear()

                while query.next():
                    display_row = []
                    id_row = []

                    for i in range(query.record().count()):
                        if i < 2:
                            display_row.append(query.value(i))
                        else:
                            id_row.append(query.value(i))

                    self.data_list.append(display_row)
                    self.id_list.append(id_row)

                self.endResetModel()

        except Exception as e:
            print("Ошибка поиска: ", e)