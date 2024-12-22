from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5 import QtSql
from PyQt5.QtCore import QDate


class TableFinance(QtCore.QAbstractTableModel):
    def __init__(self, data=None, parent=None):
        super().__init__(parent)
        self._data = data or {
            'dates': [],
            'values': []
        }

    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self._data['dates'])

    def columnCount(self, parent=QtCore.QModelIndex()):
        return 2

    def data(self, index, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            row = index.row()
            col = index.column()
            if col == 0:
                return str(self._data['dates'][row])
            elif col == 1:
                return str(self._data['values'][row])
        return None

    def headerData(self, section, orientation, role=QtCore.Qt.ItemDataRole.DisplayRole):
        if role == QtCore.Qt.ItemDataRole.DisplayRole:
            if orientation == QtCore.Qt.Orientation.Horizontal:
                if section == 0:
                    return "Дата"
                elif section == 1:
                    return "Значение"
        return None

    def setData(self, data):
        self.beginResetModel()
        self._data = data
        self.endResetModel()