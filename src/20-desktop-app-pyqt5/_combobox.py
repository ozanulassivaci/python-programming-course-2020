from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

# Demonstrates QComboBox (the dropdown widget): loading items into it,
# reading back the current selection, clearing it, and reacting when the
# selection changes. Same generated-UI + app-class split as calculator2.py.
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.combo_cities

        # addItem() would add a single entry to the dropdown; addItems()
        # (used for real in load_items() below) adds a whole list at once.
        # Left commented out here just to show the two ways of populating a
        # QComboBox -- one item at a time, or in bulk from a list.
        # combo.addItem('Ankara')
        # combo.addItem('Istanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','Izmir','Rize'])

        self.ui.btnLoadItems.clicked.connect(self.load_items)
        self.ui.btnGetItem.clicked.connect(self.get_item)
        self.ui.btnClear.clicked.connect(self.clear_items)

        # currentIndexChanged is QComboBox's signal for "the selected item
        # changed" -- it fires whenever the user (or code) picks a
        # different entry. This is an "overloaded" signal: Qt actually
        # offers two versions of it, one that sends the new selection's
        # integer index, and one that sends the new selection's text.
        # Plain `.connect(...)` (as used on the line below) picks the
        # default (index) version. To explicitly choose the text version
        # instead, PyQt5 lets you index the signal by the type you want --
        # `.currentIndexChanged[str]` -- as done on the second line, which
        # is why selected_text_changed() below receives a string instead of
        # a number. Both connections fire together on every single
        # selection change; they're just two different slots listening to
        # the same event.
        self.ui.combo_cities.currentIndexChanged.connect(self.selected_index_changed)
        self.ui.combo_cities.currentIndexChanged[str].connect(self.selected_text_changed)

    # Runs when "Clear Items" is clicked. clear() removes every item from
    # the combo box, leaving it empty again.
    def clear_items(self):
        self.ui.combo_cities.clear()

    # Runs when "Load Items" is clicked. addItems() takes a Python list of
    # strings and appends each one as a new selectable entry in the combo
    # box, in order.
    def load_items(self):
        cities = ['Adana','Izmir','Rize']

        self.ui.combo_cities.addItems(cities)

    # Runs when "Get Item" is clicked. currentText() returns the label of
    # whichever item is currently selected; currentIndex() returns its
    # position (0-based) in the list instead. count() returns how many
    # items are in the combo box in total, and itemText(index) looks up the
    # label at a specific position -- together they let us print every
    # entry the combo box currently holds, not just the selected one.
    def get_item(self):
        print(self.ui.combo_cities.currentText())
        print(self.ui.combo_cities.currentIndex())

        count = self.ui.combo_cities.count()
        for index in range(count):
            print(self.ui.combo_cities.itemText(index))

    # Slot for the index-based currentIndexChanged signal: runs automatically
    # every time the selected item changes, receiving the new item's
    # integer position.
    def selected_index_changed(self, index):
        print(index)

    # Slot for the text-based currentIndexChanged[str] signal: runs
    # automatically every time the selected item changes, receiving the new
    # item's text instead of its index.
    def selected_text_changed(self, text):
        print(text)

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
