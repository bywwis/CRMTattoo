from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime

class TableExp(QtCore.QAbstractTableModel):
    def __init__(self, db):
        super(TableExp, self).__init__()
        self.db = db
        self.data_list = []
        self.id_list = []
        self.headers = ["Название услуги", "Наименование материала", "Расход материала", "Единицы измерения"]

        self.load_data()

    def load_data(self):
        self.beginResetModel()

        query = QSqlQuery("""
            SELECT Услуги.Наименование, 
                   РасходныеМатериалы.Наименование, 
                   УслугиРасходныеМатериалы.РасходМатериалаНаУслугу,
                   УслугиРасходныеМатериалы.ЕдиницыИзмерения,
                   Услуги.ID,
                   РасходныеМатериалы.ID,
                   УслугиРасходныеМатериалы.ID
            FROM УслугиРасходныеМатериалы
            JOIN Услуги ON УслугиРасходныеМатериалы.IDУслуги = Услуги.ID
            JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
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
                query.prepare("UPDATE УслугиРасходныеМатериалы SET IDУслуги = (SELECT ID FROM Услуги WHERE Наименование = ?) WHERE ID = ?")
                query.addBindValue(value)
                query.addBindValue(self.get_exp_id(row))
            elif col == 1:
                query.prepare("UPDATE УслугиРасходныеМатериалы SET IDМатериалов = (SELECT ID FROM РасходныеМатериалы WHERE Наименование = ?) WHERE ID = ?")
                query.addBindValue(value)
                query.addBindValue(self.get_exp_id(row))
            elif col == 2:
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
                        query.prepare("UPDATE УслугиРасходныеМатериалы SET РасходМатериалаНаУслугу=? WHERE ID=?")
                        query.addBindValue(value)
                        query.addBindValue(self.get_exp_id(row))
                        if not query.exec_():
                            print(f"Ошибка выполнения запроса на обновление: {query.lastError().text()}")
                except Exception as e:
                    print(e)
            elif col == 3:
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
                        query.prepare("UPDATE УслугиРасходныеМатериалы SET ЕдиницыИзмерения=? WHERE ID=?")
                        query.addBindValue(value)
                        query.addBindValue(self.get_exp_id(row))
                        if not query.exec_():
                            print(f"Ошибка выполнения запроса на обновление: {query.lastError().text()}")

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

    def get_service_id(self, row):
        return self.id_list[row][0]

    def get_consum_id(self, row):
        return self.id_list[row][1]

    def get_exp_id(self, row):
        return self.id_list[row][2]

    def insert_row_exp(self):
        query = QSqlQuery(self.db)

        query.prepare(
            'INSERT INTO УслугиРасходныеМатериалы (IDУслуги, IDМатериалов, РасходМатериалаНаУслугу, ЕдиницыИзмерения) VALUES (:id_услуги, :id_materiala, :расход, :единицы)')
        query.addBindValue(None)
        query.addBindValue(None)
        query.addBindValue("")
        query.addBindValue("")

        if not query.exec_():
            print(f"Ошибка выполнения запроса на вставку записи: {query.lastError().text()}")
            return

        exp_id = query.lastInsertId()
        self.id_list.append([None, None, exp_id])

    def delete_row_exp(self, row):
        id_row = self.get_exp_id(row)
        query = QSqlQuery(self.db)
        query.prepare(
            f"""DELETE FROM УслугиРасходныеМатериалы WHERE ID = {id_row}""")
        if not query.exec_():
            QMessageBox.warning(self, "Ошибка", "Не удалось удалить строку.")
        self.load_data()

    def search_row_exp(self, search_text):
        try:
            if search_text == "":
                self.load_data()
            else:
                self.beginResetModel()

                query = QSqlQuery(self.db)
                query.prepare("""
                    SELECT Услуги.Наименование, 
                        РасходныеМатериалы.Наименование, 
                        УслугиРасходныеМатериалы.РасходМатериалаНаУслугу,
                        УслугиРасходныеМатериалы.ЕдиницыИзмерения,
                        Услуги.ID,
                        РасходныеМатериалы.ID,
                        УслугиРасходныеМатериалы.ID
                    FROM УслугиРасходныеМатериалы
                    JOIN Услуги ON УслугиРасходныеМатериалы.IDУслуги = Услуги.ID
                    JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                    WHERE Услуги.Наименование LIKE ? OR РасходныеМатериалы.Наименование LIKE ?
                              """)

                name_service = f"%{search_text}%"
                name_consum = f"%{search_text}%"
                query.addBindValue(name_service)
                query.addBindValue(name_consum)


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
