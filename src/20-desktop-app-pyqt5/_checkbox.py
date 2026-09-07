import sys
from PyQt5 import QtWidgets
from _checkboxForm import Ui_MainWindow

class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.cb_cinema.stateChanged.connect(self.show_state)
        self.ui.cb_reading.stateChanged.connect(self.show_state)
        self.ui.cb_sports.stateChanged.connect(self.show_state)

        # findChildren by widget type turned out to be an easy way to
        # loop over every checkbox in a group without naming them one by one.
        self.ui.btn_get_hobbies.clicked.connect(self.get_all_hobbies)
        self.ui.btn_get_subjects.clicked.connect(self.get_all_subjects)

    def get_all_hobbies(self):
        result = ''
        items = self.ui.group_hobbies.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lbl_result_hobbies.setText(result)

    def get_all_subjects(self):
        result = ''
        items = self.ui.group_subjects.findChildren(QtWidgets.QCheckBox)
        for cb in items:
            if cb.isChecked():
                result += cb.text() + '\n'

        self.ui.lbl_result_subjects.setText(result)

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
