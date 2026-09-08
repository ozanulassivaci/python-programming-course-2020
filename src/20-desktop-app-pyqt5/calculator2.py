from PyQt5 import QtWidgets
import sys
from MainWindow import Ui_MainWindow

# This is calculator.py's exact same feature (add/subtract/multiply/divide
# two numbers), rebuilt on top of the generated MainWindow.py instead of
# positioning every widget by hand. This "generated UI class + a separate
# app class" split is the standard way real PyQt5 projects are structured:
# Ui_MainWindow (from MainWindow.py) only knows how to build the widgets;
# MyApp (below) owns the actual behavior (what happens on a click). Keeping
# them separate means the visual design can be edited in Qt Designer and
# regenerated at any time without touching or losing this behavior code.
class MyApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyApp, self).__init__()
        # Rather than MyApp inheriting from Ui_MainWindow, it creates one as
        # a separate object and stores it as self.ui. This is called
        # "composition" (has-a) instead of "inheritance" (is-a), and it's
        # the pattern pyuic5-generated code is designed around: self.ui
        # will hold every widget from the form as attributes, e.g.
        # self.ui.btn_add, self.ui.txt_number1, etc.
        self.ui = Ui_MainWindow()
        # setupUi(self) builds all those widgets and places them onto this
        # window (`self`, the MyApp/QMainWindow instance being constructed
        # right now).
        self.ui.setupUi(self)
        # This is the version built from a .ui file loaded through pyuic
        # instead of laying out widgets by hand like in calculator.py.
        # Same signal/slot idea as calculator.py: all four buttons share one
        # handler, self.calculate, and it uses self.sender() to tell them
        # apart. The only difference from calculator.py is that the widgets
        # are reached through self.ui.btn_add instead of self.btn_add,
        # because they live on the self.ui object now.
        self.ui.btn_add.clicked.connect(self.calculate)
        self.ui.btn_subtract.clicked.connect(self.calculate)
        self.ui.btn_multiply.clicked.connect(self.calculate)
        self.ui.btn_divide.clicked.connect(self.calculate)

    # Shared click handler for all four operation buttons -- see
    # calculator.py's calculate() for the full explanation of how
    # self.sender().text() is used to figure out which button was pressed.
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
    # setStyleSheet() applies CSS-like styling rules across the whole
    # application. Qt's style sheet syntax deliberately looks like web CSS:
    # "QPushButton { color: red}" selects every QPushButton widget in the
    # app and sets its text color to red. This is a quick way to restyle
    # widgets without subclassing or touching paint code.
    app.setStyleSheet("QPushButton { color: red}")
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
