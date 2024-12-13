from logging import disable
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel, QSqlQueryModel
from design import Ui_MainWindow
from dialogDelConsum import Ui_Dialog
import sys
import datetime

class DelConsum(QtWidgets.QDialog):
    def __init__(self):
        super(DelConsum, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.yesBtn.clicked.connect(self.accept)
        self.ui.noBtn.clicked.connect(self.reject)