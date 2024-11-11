from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys

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

        self.ui.delBtn.clicked.connect(self.open_dialogDelNote)
        self.ui.hintBtn.setToolTip("Для того, чтобы отредактировать данные, кликните дважды по ячейке таблицы")
        self.ui.calendar.selectionChanged.connect(self.update_date_label)

        # self.ui.clienBtn.clicked.connect(self.clients_interface)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных")
            return

        self.modelNote = TableNote(self.db)
        self.ui.tableViewNote.setModel(self.modelNote)

        header = self.ui.tableViewNote.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        # self.ui.tableViewNote.setColumnHidden(0, True)


    # def clients_interface(self):
    #     self.db = QSqlDatabase.addDatabase('QSQLITE')
    #     self.db.setDatabaseName('database.db')
    #     if not self.db.open():
    #         QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных")
    #         return
    #
    #     self.model = QSqlTableModel(self, self.db)
    #     self.model.setTable("Клиенты")
    #     self.model.select()
    #
    #     self.ui.tableView.setModel(self.model)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def open_dialogAddNote(self):
        self.dialog = DialogAddNote()
        self.dialog.show()

    def open_dialogEditNote(self):
        self.dialog = DialogEditNote()
        self.dialog.show()

    def open_dialogDelNote(self):
        self.dialog = DialogDelNote()
        self.dialog.show()

    def open_dialogAddClients(self):
        pass

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

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
