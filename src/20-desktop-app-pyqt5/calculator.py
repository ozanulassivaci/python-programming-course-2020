import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class MainForm(QMainWindow):
    def __init__(self):
        super(MainForm, self).__init__()

        self.setWindowTitle('Calculator')
        self.setGeometry(200,200,500,500)
        self.initUI()

    def initUI(self):
        self.lbl_number1 = QtWidgets.QLabel(self)
        self.lbl_number1.setText('Number 1: ')
        self.lbl_number1.move(50,30)

        self.txt_number1 = QtWidgets.QLineEdit(self)
        self.txt_number1.move(150,30)
        self.txt_number1.resize(200,32)

        self.lbl_number2 = QtWidgets.QLabel(self)
        self.lbl_number2.setText('Number 2: ')
        self.lbl_number2.move(50,80)

        self.txt_number2 = QtWidgets.QLineEdit(self)
        self.txt_number2.move(150,80)
        self.txt_number2.resize(200,32)

        # First time wiring up multiple buttons to the same handler and
        # telling them apart by checking self.sender().text() below.
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_add.setText('Add')
        self.btn_add.move(150,130)
        self.btn_add.clicked.connect(self.calculate)

        self.btn_subtract = QtWidgets.QPushButton(self)
        self.btn_subtract.setText('Subtract')
        self.btn_subtract.move(150,170)
        self.btn_subtract.clicked.connect(self.calculate)

        self.btn_multiply = QtWidgets.QPushButton(self)
        self.btn_multiply.setText('Multiply')
        self.btn_multiply.move(150,210)
        self.btn_multiply.clicked.connect(self.calculate)

        self.btn_divide = QtWidgets.QPushButton(self)
        self.btn_divide.setText('Divide')
        self.btn_divide.move(150,250)
        self.btn_divide.clicked.connect(self.calculate)

        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.setText('Result: ')
        self.lbl_result.move(150,290)

    def calculate(self):
        sender = self.sender().text()
        result = 0

        if sender == 'Add':
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
        elif sender == 'Subtract':
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
        elif sender == 'Multiply':
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
        elif sender == 'Divide':
            result = int(self.txt_number1.text()) / int(self.txt_number2.text())

        self.lbl_result.setText('Result: '+ str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()
