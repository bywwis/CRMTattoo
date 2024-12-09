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