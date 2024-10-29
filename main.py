from PyQt5 import QtWidgets, QtGui, QtCore
from design import Ui_MainWindow
from dialog import Ui_Dialog
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.addBtn.clicked.connect(self.open_dialog)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()

    def open_dialog(self):
        self.dialog = Dialog()
        self.dialog.show()

class Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.ui2 = Ui_Dialog()
        self.ui2.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.showFullScreen()
    sys.exit(app.exec_())
