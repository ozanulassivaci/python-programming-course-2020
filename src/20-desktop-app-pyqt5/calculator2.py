from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # This is the version built from a .ui file loaded through pyuic
        # instead of laying out widgets by hand like in calculator.py.
        self.ui.btn_add.clicked.connect(self.calculate)
        self.ui.btn_subtract.clicked.connect(self.calculate)
        self.ui.btn_multiply.clicked.connect(self.calculate)
        self.ui.btn_divide.clicked.connect(self.calculate)

    def calculate(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Add':
            result = int(self.ui.txt_number1.text()) + int(self.ui.txt_number2.text())
        elif sender == 'Subtract':
            result = int(self.ui.txt_number1.text()) - int(self.ui.txt_number2.text())
        elif sender == 'Multiply':
            result = int(self.ui.txt_number1.text()) * int(self.ui.txt_number2.text())
        elif sender == 'Divide':
            result = int(self.ui.txt_number1.text()) / int(self.ui.txt_number2.text())

        self.ui.lbl_result.setText('Result: '+ str(result))


def app():
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet("QPushButton { color: red}")
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
