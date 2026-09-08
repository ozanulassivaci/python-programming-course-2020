from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QLineEdit, QMessageBox
from _listForm import Ui_MainWindow
import sys

# Demonstrates QListWidget: a simple "student list" editor with Add / Edit /
# Remove / move Up / move Down / Sort / Exit buttons. Also introduces two
# ready-made popup dialogs PyQt5 provides so you don't have to build your
# own small windows for common tasks: QInputDialog (a popup that asks the
# user to type a value) and QMessageBox (a popup that asks a yes/no/ok-style
# question or shows a message). Same generated-UI + app-class split as the
# other examples.
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # load Students
        self.loadStudents()

        # add New Student
        self.ui.btnAdd.clicked.connect(self.addStudent)

        # edit Student
        self.ui.btnEdit.clicked.connect(self.editStudent)

        # delete Student
        self.ui.btnRemove.clicked.connect(self.removeStudent)

        # Up
        self.ui.btnUp.clicked.connect(self.upStudent)

        # Down
        self.ui.btnDown.clicked.connect(self.downStudent)

        # sort
        self.ui.btnSort.clicked.connect(self.sortStudents)

        # close
        self.ui.btnExit.clicked.connect(self.close)

    # Called once, directly from __init__ (not a signal handler) to give
    # the list some starting content.
    def loadStudents(self):
        # Just some sample names to have something in the list to play with.
        # addItems() adds each string in the list as a new row (same method
        # name/behavior as QComboBox.addItems() in _combobox.py, since both
        # widgets share a similar "list of items" API).
        self.ui.listItems.addItems(['Kerem Deniz','Aykut','Öznur'])
        # setCurrentRow(1) selects (highlights) the row at index 1 (the
        # second item, since rows are 0-indexed) so something is selected
        # right from the start.
        self.ui.listItems.setCurrentRow(1)

    # Runs when "Add" is clicked.
    def addStudent(self):
        currentIndex = self.ui.listItems.currentRow()
        # QInputDialog.getText(parent, title, label) pops open a small
        # ready-made dialog with a text box, an OK button, and a Cancel
        # button, and BLOCKS (pauses this method) until the user closes it.
        # It returns a tuple: the text the user typed, and a boolean `ok`
        # that is True only if they pressed OK (False if they hit Cancel or
        # closed the dialog).
        text, ok = QInputDialog.getText(self, "New Student", "Student Name")
        if ok and text is not None:
            # insertItem(row, text) inserts a new row at that position,
            # shifting existing rows down -- unlike addItems(), which
            # always appends to the end.
            self.ui.listItems.insertItem(currentIndex ,text)

    # Runs when "Edit" is clicked.
    def editStudent(self):
        index = self.ui.listItems.currentRow()
        # item(index) returns the QListWidgetItem object at that row (or
        # None if the index is invalid/nothing is selected), which is what
        # lets us read/change that specific row's text below.
        item = self.ui.listItems.item(index)

        if item is not None:
            # Same QInputDialog.getText() as addStudent(), but this call
            # also pre-fills the text box with the item's current text
            # (item.text()) as a starting point to edit, using
            # QLineEdit.Normal to say "show it as plain visible text" (as
            # opposed to a password-style masked field).
            text, ok = QInputDialog.getText(self, "Edit Student", "Student Name", QLineEdit.Normal, item.text())
            if text and ok is not None:
                item.setText(text)

    # Runs when "Remove" is clicked.
    def removeStudent(self):
        index = self.ui.listItems.currentRow()
        item = self.ui.listItems.item(index)

        if item is None:
            return

        # QMessageBox.question(...) pops open a ready-made yes/no
        # confirmation dialog and blocks until the user picks one. The
        # button flags (QMessageBox.Yes | QMessageBox.No) are combined with
        # the bitwise-or operator `|` to tell Qt which buttons to show; the
        # return value tells you which one was actually clicked, which we
        # compare against QMessageBox.Yes below.
        q = QMessageBox.question(self, "Remove Student", "Do you want to remove student: " + item.text(), QMessageBox.Yes | QMessageBox.No)
        if q == QMessageBox.Yes:
            # takeItem(index) removes the row from the list widget AND
            # returns the QListWidgetItem object that used to be there
            # (unlike removing by index alone, this gives us a chance to
            # clean it up). `del item` then deletes that now-detached
            # Python object, since nothing needs it anymore.
            item = self.ui.listItems.takeItem(index)
            del item

    # Runs when "Up" is clicked: swaps the selected row with the one above
    # it, if it isn't already at the top.
    def upStudent(self):
        index = self.ui.listItems.currentRow()
        if index >= 1:
            # There's no direct "move row" method, so this is done manually:
            # take the item out (removing it from the list), reinsert it one
            # position earlier, then re-select it with setCurrentItem() so
            # the highlighted row moves along with it (otherwise the
            # selection would just stay on whatever row now sits at the old
            # index).
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index-1, item)
            self.ui.listItems.setCurrentItem(item)

    # Runs when "Down" is clicked: same idea as upStudent(), moving the
    # selected row one position later instead, as long as it isn't already
    # the last row (count()-1 is the index of the last item).
    def downStudent(self):
        index = self.ui.listItems.currentRow()
        if index < self.ui.listItems.count()-1:
            item = self.ui.listItems.takeItem(index)
            self.ui.listItems.insertItem(index+1, item)
            self.ui.listItems.setCurrentItem(item)

    # Runs when "Sort" is clicked. sortItems() reorders every row
    # alphabetically (ascending, by default).
    def sortStudents(self):
        self.ui.listItems.sortItems()

    # Runs when "Exit" is clicked. Note this overrides/shadows QMainWindow's
    # own built-in close() method (which would normally just close the
    # window) -- here it's redefined to call the built-in quit() function
    # instead, which ends the whole Python process immediately.
    def close(self):
        quit()

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()


