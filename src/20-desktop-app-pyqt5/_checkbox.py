import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

# Demonstrates QCheckBox: two groups of checkboxes (hobbies and school
# subjects), each with a button that reports which ones are currently
# checked. Same "generated UI + separate app class" split as calculator2.py:
# Ui_MainWindow (from _checkboxForm.py) builds the widgets, MyApp below
# wires up the behavior.
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # QCheckBox emits a `stateChanged` signal whenever it's ticked or
        # unticked. Unlike QPushButton's `clicked` (which carries no useful
        # data), stateChanged passes an integer value describing the new
        # state to the connected slot -- that's why show_state() below is
        # defined with an extra `value` parameter. All three checkboxes are
        # wired to the very same show_state method; like calculate() in
        # calculator.py, self.sender() is used inside it to find out which
        # checkbox actually changed.
        self.ui.cb_cinema.stateChanged.connect(self.show_state)
        self.ui.cb_reading.stateChanged.connect(self.show_state)
        self.ui.cb_sports.stateChanged.connect(self.show_state)

        # findChildren by widget type turned out to be an easy way to
        # loop over every checkbox in a group without naming them one by one.
        self.ui.btn_get_hobbies.clicked.connect(self.get_all_hobbies)
        self.ui.btn_get_subjects.clicked.connect(self.get_all_subjects)

    # Runs when "Get Selected" (hobbies) is clicked. findChildren(QCheckBox)
    # searches self.ui.group_hobbies (the QGroupBox from _checkboxForm.py)
    # and returns every QCheckBox widget nested inside it, no matter how
    # deep -- so we don't have to list self.ui.cb_cinema, cb_reading,
    # cb_sports by name here. isChecked() reports each box's current
    # on/off state as a plain Python bool.
    def get_all_hobbies(self):
        result = ''
        items = self.ui.group_hobbies.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lbl_result_hobbies.setText(result)

    # Same idea as get_all_hobbies(), but scoped to the "subjects" group box
    # instead, run when the second "Get Selected" button is clicked.
    def get_all_subjects(self):
        result = ''
        items = self.ui.group_subjects.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lbl_result_subjects.setText(result)

    # Runs automatically every time ANY of the three checkboxes changes
    # state (checked or unchecked) -- not on a button click, but directly
    # as a result of the user clicking the checkbox itself. `value` is the
    # integer Qt passes along with the stateChanged signal (0 = unchecked,
    # 2 = checked; QCheckBox can also have a partially-checked state, which
    # this example doesn't use). self.sender() again identifies exactly
    # which checkbox fired, so we can print its label and current state.
    def show_state(self, value):
        cb = self.sender()

        print(value)
        print(cb.text())
        print(cb.isChecked())


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
