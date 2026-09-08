import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

# Same little "name + surname" form as win-class.py, but written WITHOUT a
# class: every widget is just a local variable inside the window() function,
# and the parent widget passed to each constructor is `win` directly instead
# of `self`. This works fine for a tiny one-off script, but it doesn't scale:
# there's no natural place to store shared state or add more methods, which
# is exactly why win-class.py's class-based style is the pattern used
# everywhere else in this folder.
def window():
    app = QApplication(sys.argv)
    win = QMainWindow()

    win.setWindowTitle('First Application')
    win.setGeometry(200,200,700,700)
    win.setWindowIcon(QIcon('icon.png'))
    win.setToolTip('my tooltip')

    # QLabel(win) makes `win` the parent, so the label is drawn inside the
    # window. move(x, y) positions it relative to the window's top-left
    # corner (no automatic layout is being used, so every position is set
    # by hand).
    lbl_name = QtWidgets.QLabel(win)
    lbl_name.setText('Your Name: ')
    lbl_name.move(50,30)

    lbl_surname = QtWidgets.QLabel(win)
    lbl_surname.setText('Your Surname: ')
    lbl_surname.move(50,70)

    txt_name = QtWidgets.QLineEdit(win)
    txt_name.move(150, 30)

    txt_surname = QtWidgets.QLineEdit(win)
    txt_surname.move(150, 70)

    # This is the version without a class - all widgets are just
    # created directly on the window in one function.
    #
    # Because there's no class/self here, the click handler is just a plain
    # nested function defined inside window(). Thanks to Python's "closures",
    # this inner function can still see and use txt_name/txt_surname from
    # the enclosing function, even though they aren't passed in as
    # arguments. Note its parameter is named `self` out of habit from the
    # class-based style, but it isn't a real `self` here -- it's just
    # whatever argument the clicked signal happens to pass in (QPushButton's
    # clicked signal can optionally send a boolean "checked" value, which
    # ends up bound to this parameter; the function just ignores it).
    def clicked(self):
        print('button clicked - name: '+ txt_name.text()+ ' surname: '+ txt_surname.text())

    btn_save = QtWidgets.QPushButton(win)
    btn_save.setText('Save')
    btn_save.move(150,110)
    # Same signal/slot idea as win-class.py: connect the button's `clicked`
    # signal to our function, so Qt calls clicked() automatically every time
    # the button is pressed, once the event loop below is running.
    btn_save.clicked.connect(clicked)

    win.show()
    sys.exit(app.exec_())

window()


# A quick reference of other common PyQt5 widgets (see win-class.py for a
# one-line description of each):
# QComboBox
# QCheckBox
# QRadioButton
# QPushButton
# QTableWidget
# QLineEdit
# QSlider
# QProgressBar
