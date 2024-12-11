from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime

class DelNote(QtWidgets.QDialog):
    def __init__(self):
        super(DelNote, self).__init__()
        self.ui = Ui_DialogDelNote()
        self.ui.setupUi(self)