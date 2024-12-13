from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelNote import Ui_DialogDelNote
import sys
import datetime
from dialogDelExp import Ui_Dialog

class DelExp(QtWidgets.QDialog):
    def __init__(self):
        super(DelExp, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.yesBtn.clicked.connect(self.accept)
        self.ui.noBtn.clicked.connect(self.reject)