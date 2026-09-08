import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# A small calculator app: two number inputs and four operation buttons
# (Add/Subtract/Multiply/Divide). It builds on the same ideas as
# win-class.py (a QMainWindow subclass, widgets positioned with move(),
# signals connected to methods), but here all four buttons share a SINGLE
# handler method instead of each getting its own -- see calculate() below
# for how it tells them apart.
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
        # Notice all four .clicked signals are connected to the exact same
        # method, self.calculate -- unlike win-class.py where one button had
        # its own dedicated method. This avoids writing four nearly
        # identical methods that each do "read two numbers, do one
        # operation, show the result".
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

    # This is the shared signal handler for all four buttons: Qt calls it
    # every time ANY of Add/Subtract/Multiply/Divide is clicked. Since one
    # method now has to serve four different buttons, it needs a way to
    # know which button triggered it -- that's what self.sender() is for:
    # inside a slot, it returns the specific widget object that emitted the
    # signal currently being handled. Calling .text() on it gives that
    # button's label ('Add', 'Subtract', ...), which is then used to decide
    # which arithmetic operation to perform.
    def calculate(self):
        sender = self.sender().text()
        result = 0

        # QLineEdit.text() always returns a str, even if the user typed
        # digits, so int(...) converts each text box's contents to a whole
        # number before doing arithmetic on them. (This will crash with a
        # ValueError if the text isn't a valid integer -- there's no
        # input validation here, since the example is only meant to show
        # sender()-based dispatch.)
        if sender == 'Add':
            result = int(self.txt_number1.text()) + int(self.txt_number2.text())
        elif sender == 'Subtract':
            result = int(self.txt_number1.text()) - int(self.txt_number2.text())
        elif sender == 'Multiply':
            result = int(self.txt_number1.text()) * int(self.txt_number2.text())
        elif sender == 'Divide':
            # Note: '/' is true division in Python 3, so this can produce a
            # float (e.g. 7/2 == 3.5) even though the inputs are ints.
            result = int(self.txt_number1.text()) / int(self.txt_number2.text())

        self.lbl_result.setText('Result: '+ str(result))

def app():
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())

app()
