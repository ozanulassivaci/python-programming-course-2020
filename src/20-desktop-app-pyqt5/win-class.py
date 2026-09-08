import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

# This is the same idea as creating-app.py (a QApplication + a QMainWindow),
# but now the window is written as its own class instead of a bare function.
# This is the standard, recommended way to build PyQt5 apps: subclassing
# QMainWindow lets the window keep its own widgets as attributes (self.xxx)
# and its own methods to react to user actions, instead of everything living
# in loose local variables inside one function.
class MyWindow(QMainWindow):
    def __init__(self):
        # __init__ is the constructor: it runs automatically once, the
        # moment MyWindow() is called (see window() below). super(MyWindow,
        # self).__init__() calls QMainWindow's own constructor first, so all
        # the normal window machinery (event handling, painting, etc.) gets
        # set up properly before we start customizing it. Always do this
        # before touching `self` in a widget subclass's __init__.
        super(MyWindow, self).__init__()

        # Same widget-configuration calls as before, but now called on
        # `self` (this window instance) instead of on a local `win`
        # variable, since `self` *is* the window.
        self.setWindowTitle('First Application')
        self.setGeometry(200,200,700,700)
        self.setWindowIcon(QIcon('icon.png'))
        self.setToolTip('my tooltip')

        # It's a common PyQt5 pattern to keep __init__ short and move all the
        # "build the child widgets" code into a separate method (often
        # called initUI). It's just a naming convention, not something Qt
        # requires -- but it makes classes easier to read once there are a
        # lot of widgets to create.
        self.initUI()

    def initUI(self):
        # QLabel is a widget that displays a short piece of read-only text
        # (or an image). Passing `self` as the argument to the constructor
        # -- QtWidgets.QLabel(self) -- makes this label a CHILD of the
        # window: it will be drawn inside the window and destroyed
        # automatically when the window is destroyed. Every widget you add
        # to a window needs a parent like this (directly or indirectly)
        # or it won't show up inside it.
        self.lbl_name = QtWidgets.QLabel(self)
        # setText() changes the text the label displays.
        self.lbl_name.setText('Your Name: ')
        # move(x, y) places the widget at pixel coordinates x,y *relative to
        # its parent's top-left corner* (not the screen). There's no
        # automatic layout being used in this file, so every widget's
        # position has to be set by hand with move() -- this is called
        # "absolute positioning". (Compare with layouts.py, where
        # QVBoxLayout/QHBoxLayout arrange widgets for you automatically.)
        self.lbl_name.move(50,30)

        self.lbl_surname = QtWidgets.QLabel(self)
        self.lbl_surname.setText('Your Surname: ')
        self.lbl_surname.move(50,70)

        # This label starts out with no text (it will be filled in later,
        # once the Save button is clicked). resize(width, height) sets the
        # widget's size in pixels, independent of move()'s position.
        self.lbl_result = QtWidgets.QLabel(self)
        self.lbl_result.resize(300,50)
        self.lbl_result.move(150,150)

        # QLineEdit is a single-line editable text box -- the widget users
        # type into.
        self.txt_name = QtWidgets.QLineEdit(self)
        self.txt_name.move(150, 30)
        self.txt_name.resize(200,32)

        self.txt_surname = QtWidgets.QLineEdit(self)
        self.txt_surname.move(150, 70)
        self.txt_surname.resize(200,32)

        # QPushButton is a clickable button.
        self.btn_save = QtWidgets.QPushButton(self)
        self.btn_save.setText('Save')
        self.btn_save.move(150,110)
        # This is PyQt5's "signals and slots" mechanism, the core way
        # widgets communicate with your code. Every widget can emit
        # "signals" when something happens to it -- a button's `clicked`
        # signal fires whenever it's pressed and released. `.connect(...)`
        # attaches a Python function (called a "slot" in Qt terminology,
        # though in PyQt5 it can be any callable) to that signal: from now
        # on, whenever the button is clicked, Qt will automatically call
        # self.clicked() for us. We never call self.clicked() ourselves --
        # the event loop (app.exec_(), see window() below) is what notices
        # the click and makes the call happen.
        self.btn_save.clicked.connect(self.clicked)

    # This method is a "signal handler" (a slot): it does not run when the
    # class is created, and nothing in this file calls it directly. It only
    # runs later, each time the user clicks the Save button, because it was
    # wired up above with `.connect(self.clicked)`. When it runs, it reads
    # whatever text is currently in the two QLineEdit boxes with .text()
    # and displays a combined message in the result label.
    def clicked(self):
        self.lbl_result.setText('name: '+ self.txt_name.text()+ ' surname: '+ self.txt_surname.text())

def window():
    app = QApplication(sys.argv)
    # Creating MyWindow() runs its __init__ above, which builds every child
    # widget before this line finishes.
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


# A quick reference of other common PyQt5 widgets you'll meet in this
# folder's later examples, beyond the QLabel/QLineEdit/QPushButton used
# here:
# QComboBox       - a dropdown selection list
# QCheckBox       - a box that can be independently ticked on/off
# QRadioButton    - one option chosen from a mutually-exclusive group
# QPushButton
# QTableWidget    - a spreadsheet-like grid of rows/columns
# QLineEdit
# QSlider         - a draggable handle for picking a numeric value
# QProgressBar    - a bar showing how far a long task has progressed
