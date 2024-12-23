from logging import disable
from DelConsum import DelConsum
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from PyQt5 import QtSql
from PyQt5.QtCore import QDate
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
from dialogDelClients import Ui_Dialog
from dialogDelConsum import Ui_Dialog
from dialogDelPrice import Ui_Dialog
from dialogDelExp import Ui_Dialog
import sys
import datetime
from TableNote import TableNote
from TableClients import TableClients
from TableConsum import TableConsum
from TablePrice import TablePrice
from TableExp import TableExp
from TableFinance import TableFinance
from DelNote import DelNote
from DelClients import DelClients
from DelConsum import DelConsum
from DelPrice import DelPrice
from DelExp import DelExp
from designeFinance import Ui_Finance
import pyqtgraph as pg
import numpy as np
from pyqtgraph.exporters import Exporter
import csv


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
        self.ui.finanBtn.clicked.connect(self.show_finance)

        self.ui.addBtn.clicked.connect(self.add_row)
        self.ui.delBtn.clicked.connect(self.open_dialog)
        self.ui.hintBtn.setToolTip("Для того, чтобы отредактировать данные, кликните дважды по ячейке таблицы")

        self.ui.calendar.selectionChanged.connect(self.update_date_label)
        self.ui.period.currentIndexChanged.connect(self.on_period_changed)

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


        self.ui.tableView.setItemDelegateForColumn(2, ServiceDelegate(self.ui.tableView))

        date_today = datetime.date.today()
        formatted_date = date_today.strftime("%d.%m.%Y")
        self.ui.labelDate.setText(f"{formatted_date}")

        self.ui.searchTxt.textChanged.connect(lambda: self.search_text(self.ui.searchTxt.toPlainText()))

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableView.setItemDelegateForColumn(2, None)
        self.ui.tableView.setItemDelegateForColumn(0, None)
        self.ui.tableView.setItemDelegateForColumn(1, None)

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableView.setItemDelegateForColumn(2, ServiceDelegate(self.ui.tableView))
        self.ui.tableView.setItemDelegateForColumn(0, None)
        self.ui.tableView.setItemDelegateForColumn(1, None)

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableView.setItemDelegateForColumn(2, None)
        self.ui.tableView.setItemDelegateForColumn(0, None)
        self.ui.tableView.setItemDelegateForColumn(1, None)

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableView.setItemDelegateForColumn(2, None)
        self.ui.tableView.setItemDelegateForColumn(0, None)
        self.ui.tableView.setItemDelegateForColumn(1, None)

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
        self.ui.tableView.verticalHeader().setVisible(False)

        header = self.ui.tableView.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)

        self.ui.tableView.setItemDelegateForColumn(0, ServiceDelegate(self.ui.tableView))
        self.ui.tableView.setItemDelegateForColumn(1, MaterialDelegate(self.ui.tableView))

        self.ui.tableView.setItemDelegateForColumn(2, None)

    def show_finance(self):
        try:
            self.windowFinance = WindowFinance()
            self.windowFinance.showFullScreen()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def open_dialog(self):
        try:
            index = self.ui.tableView.currentIndex()
            if index.isValid():
                if isinstance(self.model, TableNote):
                    self.dialog = DelNote()
                elif isinstance(self.model, TableClients):
                    self.dialog = DelClients()
                elif isinstance(self.model, TableConsum):
                    self.dialog = DelConsum()
                elif isinstance(self.model, TableExp):
                    self.dialog = DelExp()
                elif isinstance(self.model, TablePrice):
                    self.dialog = DelPrice()
                result = self.dialog.exec_()
                if result == QtWidgets.QDialog.Accepted:
                    row = index.row()
                    if isinstance(self.model, TableNote):
                        self.model.delete_row_note(row)
                    elif isinstance(self.model, TableClients):
                        self.model.delete_row_clients(row)
                    elif isinstance(self.model, TableConsum):
                        self.model.delete_row_consum(row)
                    elif isinstance(self.model, TableExp):
                        self.model.delete_row_exp(row)
                    elif isinstance(self.model, TablePrice):
                        self.model.delete_row_price(row)
            else:
                QMessageBox.warning(self, "Предупреждение", "Сначала выберите строку для удаления.")
        except Exception as e:
            print('Ошибка удаления: ', e)

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

        self.on_period_changed(self.ui.period.currentIndex())

    def on_period_changed(self, index):
        try:
            period = self.ui.period.itemText(index)
            current_date = QDate.fromString(self.ui.labelDate.text(), "dd.MM.yyyy")

            if period == "День":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = start_date
            elif period == "Неделя":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addDays(7).toString("dd.MM.yyyy")
            elif period == "Месяц":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addMonths(1).toString("dd.MM.yyyy")
            elif period == "Год":
                start_date = current_date.toString("dd.MM.yyyy")
                end_date = current_date.addYears(1).toString("dd.MM.yyyy")

            self.filter_table(start_date, end_date)

        except Exception as e:
            print("Ошибка смены периода:", e)

    def filter_table(self, start_date, end_date):
        if isinstance(self.model, TableNote):
            self.model.load_filtered_data_note(period=self.ui.period.currentText(),
                                               start_date=start_date,
                                               end_date=end_date)
        elif isinstance(self.model, TableClients):
            self.model.load_filtered_data_clients(period=self.ui.period.currentText(),
                                               start_date=start_date,
                                               end_date=end_date)

    def add_row(self):
        try:
            self.model.beginInsertRows(QtCore.QModelIndex(), self.model.rowCount(), self.model.rowCount())
            self.model.data_list.append(["" for _ in range(self.model.columnCount())])
            self.model.endInsertRows()
            if isinstance(self.model, TableNote):
                self.model.insert_row_note()
            elif isinstance(self.model, TableClients):
                self.model.insert_row_clients()
            elif isinstance(self.model, TableConsum):
                self.model.insert_row_consum()
            elif isinstance(self.model, TableExp):
                self.model.insert_row_exp()
            elif isinstance(self.model, TablePrice):
                self.model.insert_row_price()
        except Exception as e:
            print(f"Ошибка при добавлении строки: {e}")

    def search_text(self, search_text):
        try:
            if isinstance(self.model, TableNote):
                self.model.search_row_note(search_text)
            elif isinstance(self.model, TableClients):
                self.model.search_row_clients(search_text)
            elif isinstance(self.model, TableConsum):
                self.model.search_row_consum(search_text)
            elif isinstance(self.model, TableExp):
                self.model.search_row_exp(search_text)
            elif isinstance(self.model, TablePrice):
                self.model.search_row_price(search_text)
        except Exception as e:
            print("Ошибка ввода в строку для поиска: ", e)


class ServiceDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        query = QtSql.QSqlQuery("SELECT Наименование FROM Услуги", self.parent().model().db)
        while query.next():
            editor.addItem(query.value(0))
        return editor

    def setEditorData(self, editor, index):
        text = index.model().data(index, QtCore.Qt.DisplayRole)
        editor.setCurrentText(text)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)


class MaterialDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        query = QtSql.QSqlQuery("SELECT Наименование FROM РасходныеМатериалы", self.parent().model().db)
        while query.next():
            editor.addItem(query.value(0))
        return editor

    def setEditorData(self, editor, index):
        text = index.model().data(index, QtCore.Qt.DisplayRole)
        editor.setCurrentText(text)

    def setModelData(self, editor, model, index):
        model.setData(index, editor.currentText(), QtCore.Qt.EditRole)


class WindowFinance(QtWidgets.QMainWindow):
    def __init__(self):
        super(WindowFinance, self).__init__()
        self.ui = Ui_Finance()
        self.ui.setupUi(self)

        self.ui.period.addItem("День")
        self.ui.period.addItem("Неделя")
        self.ui.period.addItem("Месяц")
        self.ui.period.addItem("Год")
        self.ui.period.currentIndexChanged.connect(self.update_graph)

        self.ui.type.addItem("Выручка")
        self.ui.type.addItem("Прибыль")
        self.ui.type.addItem("Расходы")
        self.ui.type.currentIndexChanged.connect(self.update_graph)

        self.ui.displayType.addItem("График")
        self.ui.displayType.addItem("Диаграмма")
        self.ui.displayType.addItem("Гистограмма")
        self.ui.displayType.currentIndexChanged.connect(self.update_graph)

        self.ui.clientBtn.clicked.connect(self.show_clients)
        self.ui.recordsBtn.clicked.connect(self.show_notes)
        self.ui.consumBtn.clicked.connect(self.show_consum)
        self.ui.priceBtn.clicked.connect(self.show_price)
        self.ui.expBtn.clicked.connect(self.show_exp)
        self.ui.finanBtn.clicked.connect(self.show_finance)

        self.ui.calendar.selectionChanged.connect(self.update_date_label)

        self.ui.reportBtn.clicked.connect(self.save_plot)

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('database.db')
        if not self.db.open():
            QMessageBox.critical(self, "Ошибка", "Не удалось подключиться к базе данных")
            return

        date_today = datetime.date.today()
        formatted_date = date_today.strftime("%d.%m.%Y")
        self.ui.labelDate.setText(f"{formatted_date}")

        self.graph_widget = pg.PlotWidget(background="#dcd6dc")
        self.ui.gridLayout.addWidget(self.graph_widget)

        self.update_graph()

    def save_plot(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить график", "график", "PNG (*.png);;PDF (*.pdf)")
        if file_name:
            exporter = pg.exporters.ImageExporter(self.graph_widget.plotItem)
            exporter.parameters()['width'] = 1020
            exporter.parameters()['height'] = 1080
            exporter.export(file_name)
            QMessageBox.information(self, "Сохранение", "Данные графика успешно сохранены в файл " + file_name)
            self.save_table()

    def save_table(self):
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Сохранить таблицу",
            "таблица",
            "CSV (*.csv)"
        )
        if file_name:
            model = self.ui.tableViewFinance.model()

            row_count = model.rowCount()
            column_count = model.columnCount()

            with open(file_name, 'w', newline='') as file:
                writer = csv.writer(file, delimiter=';')

                headers = ["Дата", "Значение"]
                writer.writerow(headers)

                for row in range(row_count):
                    data_row = []
                    for col in range(column_count):
                        index = model.index(row, col)
                        value = index.data(QtCore.Qt.DisplayRole)
                        data_row.append(str(value))

                    writer.writerow(data_row)

            QMessageBox.information(self, "Сохранение", f"Таблица успешно сохранена в файл {file_name}")

    def update_graph(self):
        self.graph_widget.clear()
        period = self.ui.period.currentText()
        type_ = self.ui.type.currentText()
        display_type = self.ui.displayType.currentText()

        current_date = QDate.fromString(self.ui.labelDate.text(), "dd.MM.yyyy")

        if period == "День":
            start_date = current_date.toString("dd.MM.yyyy")
            end_date = start_date
        elif period == "Неделя":
            start_date = current_date.toString("dd.MM.yyyy")
            end_date = current_date.addDays(7).toString("dd.MM.yyyy")
        elif period == "Месяц":
            start_date = current_date.toString("dd.MM.yyyy")
            end_date = current_date.addMonths(1).toString("dd.MM.yyyy")
        elif period == "Год":
            start_date = current_date.toString("dd.MM.yyyy")
            end_date = current_date.addYears(1).toString("dd.MM.yyyy")

        data = self.get_data(type_, start_date, end_date, period)

        if display_type == "График":
            self.plot_line_graph(data)
        elif display_type == "Диаграмма":
            self.plot_bar_chart(data)
        elif display_type == "Гистограмма":
            self.plot_histogram(data)

        self.model = TableFinance()
        self.ui.tableViewFinance.setModel(self.model)
        self.model.setData(data)

        header = self.ui.tableViewFinance.horizontalHeader()
        header.setStretchLastSection(True)
        header.setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableViewFinance.verticalHeader().setVisible(False)

    def get_data(self, type_, start_date, end_date, period):
        try:
            query = QSqlQuery(self.db)

            if type_ == "Выручка":
                if period == "День" or period == "Неделя":
                    query.prepare("""
                                SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                                FROM (
                                    SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                                    FROM Запись
                                    WHERE Дата BETWEEN ? AND ?
                                    GROUP BY IDуслуги, Дата) AS ЗаписиПоУслугам
                    JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                    GROUP BY Дата
                """)

                    query.addBindValue(start_date)
                    query.addBindValue(end_date)

                elif period == "Месяц":
                    month = start_date.split('.')[1]
                    year = start_date.split('.')[2]
                    query.prepare("""
                        SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                        FROM (
                            SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                            FROM Запись
                            WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                            GROUP BY IDуслуги, Дата)
                        AS ЗаписиПоУслугам
                        JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                        GROUP BY Дата
                    """)

                    query.addBindValue(month)
                    query.addBindValue(year)

                elif period == "Год":
                    year = start_date.split('.')[2]
                    query.prepare("""
                        SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                        FROM (
                            SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                            FROM Запись
                            WHERE substr(Дата, 7, 4) = ?
                            GROUP BY IDуслуги, Дата)
                        AS ЗаписиПоУслугам
                        JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                        GROUP BY Дата
                    """)

                    query.addBindValue(year)

            elif type_ == "Расходы":
                if period == "День" or period == "Неделя":
                    query.prepare("""
                        SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                        FROM Запись 
                        JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                        JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                        WHERE Дата BETWEEN ? AND ?
                        GROUP BY Дата
                    """)

                    query.addBindValue(start_date)
                    query.addBindValue(end_date)

                elif period == "Месяц":
                    month = start_date.split('.')[1]
                    year = start_date.split('.')[2]

                    query.prepare("""
                        SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                        FROM Запись 
                        JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                        JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                        WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                        GROUP BY Дата
                    """)

                    query.addBindValue(month)
                    query.addBindValue(year)

                elif period == "Год":
                    year = start_date.split('.')[2]
                    query.prepare("""
                        SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                        FROM Запись 
                        JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                        JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                        WHERE substr(Дата, 7, 4) = ?
                        GROUP BY Дата
                    """)

                    query.addBindValue(year)

            elif type_ == "Прибыль":
                if period == "День" or period == "Неделя":
                    query.prepare("""
                        WITH Выручка AS (
                            SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                            FROM (
                                SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                                FROM Запись
                                WHERE Дата BETWEEN ? AND ?
                                GROUP BY IDуслуги, Дата)
                                AS ЗаписиПоУслугам
                            JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                            GROUP BY Дата
                        ), Расход AS (
                            SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                            FROM Запись 
                            JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                            JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                            WHERE Дата BETWEEN ? AND ?
                            GROUP BY Дата
                        )
                        SELECT Выручка.Дата,  IFNULL(Выручка.Выручка, 0) - IFNULL(Расход.Расход, 0) AS Прибыль
                        FROM Выручка LEFT JOIN Расход ON Выручка.Дата = Расход.Дата
                    """)

                    query.addBindValue(start_date)
                    query.addBindValue(end_date)
                    query.addBindValue(start_date)
                    query.addBindValue(end_date)

                elif period == "Месяц":
                    month = start_date.split('.')[1]
                    year = start_date.split('.')[2]
                    query.prepare("""
                        WITH Выручка AS (
                            SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                            FROM (
                                SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                                FROM Запись
                                WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                                GROUP BY IDуслуги, Дата)
                            AS ЗаписиПоУслугам
                            JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                            GROUP BY Дата
                        ), Расход AS (
                                SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                                FROM Запись 
                                JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                                JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                                WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                                GROUP BY Дата
                        )
                        SELECT Выручка.Дата, IFNULL(Выручка.Выручка, 0) - IFNULL(Расход.Расход, 0) AS Прибыль
                        FROM Выручка LEFT JOIN Расход ON Выручка.Дата = Расход.Дата
                    """)

                    query.addBindValue(month)
                    query.addBindValue(year)

                    query.addBindValue(month)
                    query.addBindValue(year)

                elif period == "Год":
                    year = start_date.split('.')[2]
                    query.prepare("""
                        WITH Выручка AS (
                            SELECT Дата, SUM(Услуги.Цена * КоличествоЗаписей) AS Выручка
                            FROM (
                                SELECT IDуслуги, COUNT(ID) AS КоличествоЗаписей, Дата
                                FROM Запись
                                WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                                GROUP BY IDуслуги, Дата)
                            AS ЗаписиПоУслугам
                            JOIN Услуги ON ЗаписиПоУслугам.IDуслуги = Услуги.ID
                            GROUP BY Дата
                        ), Расход AS (
                                SELECT Дата, SUM(РасходныеМатериалы.СтоимостьШтуки * УслугиРасходныеМатериалы.РасходМатериалаНаУслугу) AS Расход
                                FROM Запись 
                                JOIN УслугиРасходныеМатериалы ON Запись.IDуслуги = УслугиРасходныеМатериалы.IDУслуги
                                JOIN РасходныеМатериалы ON УслугиРасходныеМатериалы.IDМатериалов = РасходныеМатериалы.ID
                                WHERE substr(Дата, 4, 2) = ? AND substr(Дата, 7, 4) = ?
                                GROUP BY Дата
                        )
                        SELECT Выручка.Дата, IFNULL(Выручка.Выручка, 0) - IFNULL(Расход.Расход, 0) AS Прибыль
                        FROM Выручка LEFT JOIN Расход ON Выручка.Дата = Расход.Дата
                    """)
                    query.addBindValue(year)
                    query.addBindValue(year)
                    query.addBindValue(year)
                    query.addBindValue(year)

            if not query.exec_():
                print("Ошибка выполнения запроса на получение данных:", query.lastError().text())
                return []

            dates = []
            values = []
            while query.next():
                dates.append(query.value(0))
                values.append(query.value(1))

            return {"dates": dates, "values": values}

        except Exception as e:
            print("Ошибка получения данных для графиков: ", e)

    def plot_line_graph(self, data):
        self.graph_widget.clear()
        x = np.arange(len(data["dates"]))
        y = data["values"]
        self.graph_widget.plot(x, y, symbol='o', pen=pg.mkPen(color=(153, 170, 210), width=3))
        self.graph_widget.setLabel('left', 'Значение', units='')
        self.graph_widget.setLabel('bottom', 'Дата', units='')
        self.graph_widget.setTitle('График изменения значений')

    def plot_bar_chart(self, data):
        self.graph_widget.clear()
        x = np.arange(len(data["dates"]))
        y = data["values"]
        bar_graph_item = pg.BarGraphItem(x=x, height=y, width=0.8, brush=(153, 170, 210))
        self.graph_widget.addItem(bar_graph_item)
        self.graph_widget.setLabel('left', 'Значение', units='')
        self.graph_widget.setLabel('bottom', 'Дата', units='')
        self.graph_widget.setTitle('Диаграмма изменения значений')

    def plot_histogram(self, data):
        self.graph_widget.clear()
        y = data["values"]
        hist, bin_edges = np.histogram(y, bins='auto')
        x = bin_edges[:-1]
        bar_graph_item = pg.BarGraphItem(x=x, height=hist, width=0.8, brush=(153, 170, 210))
        self.graph_widget.addItem(bar_graph_item)
        self.graph_widget.setLabel('left', 'Частота', units='')
        self.graph_widget.setLabel('bottom', 'Значения', units='')
        self.graph_widget.setTitle('Гистограмма распределения значений')

    def update_date_label(self):
        selected_date = self.ui.calendar.selectedDate()
        formatted_date = selected_date.toString("dd.MM.yyyy")
        self.ui.labelDate.setText(f"{formatted_date}")

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def show_clients(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_clients()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def show_notes(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_notes()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def show_consum(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_consum()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def show_price(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_price()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def show_exp(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_exp()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)

    def show_finance(self):
        try:
            self.window = MyWindow()
            self.window.showFullScreen()

            self.window.show_finance()

            QtCore.QTimer.singleShot(1000, self.close)
        except Exception as e:
            print(e)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showFullScreen()
    sys.exit(app.exec_())