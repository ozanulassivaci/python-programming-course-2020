from PyQt5 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow

# Demonstrates QRadioButton: two independent groups (country, education
# level) where only one option can be selected per group. Same generated-UI
# + app-class split as the other examples in this folder.
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # setChecked(True) pre-selects one radio button in each group as
        # the initial default, so the form doesn't start with nothing
        # selected. Because radio buttons in the same QGroupBox are
        # mutually exclusive (see _radiobuttonForm.py), checking one of
        # them here doesn't need to explicitly uncheck the others -- Qt
        # does that automatically.
        self.ui.radio_turkey.setChecked(True)
        self.ui.radio_high_school.setChecked(True)

        # QRadioButton's `toggled` signal fires whenever the button's
        # checked state changes -- both when it BECOMES checked and when it
        # becomes UNCHECKED (e.g. because a sibling radio button was
        # selected instead, which automatically unchecks this one). That's
        # why on_country_clicked() below checks rb.isChecked() before
        # printing anything: without that check, selecting Germany would
        # also trigger this same handler once for Turkey turning OFF (which
        # we want to ignore) and once for Germany turning ON (which we want
        # to report).
        self.ui.radio_turkey.toggled.connect(self.on_country_clicked)
        self.ui.radio_azerbaijan.toggled.connect(self.on_country_clicked)
        self.ui.radio_germany.toggled.connect(self.on_country_clicked)
        self.ui.radio_greece.toggled.connect(self.on_country_clicked)

        self.ui.radio_elementary.toggled.connect(self.on_education_clicked)
        self.ui.radio_high_school.toggled.connect(self.on_education_clicked)
        self.ui.radio_university.toggled.connect(self.on_education_clicked)
        self.ui.radio_masters.toggled.connect(self.on_education_clicked)

        self.ui.btn_country.clicked.connect(self.get_selected_country)
        self.ui.btn_education.clicked.connect(self.get_selected_education)

    # Runs automatically whenever ANY country radio button's checked state
    # changes (see the toggled signal explanation above). self.sender()
    # identifies which specific radio button just changed; the isChecked()
    # guard means we only print when a button was just turned ON, not when
    # it was turned off by a sibling selection.
    def on_country_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            print('selected country: '+ rb.text())

    # Same idea as on_country_clicked(), for the education group.
    def on_education_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            print('selected education: '+ rb.text())

    # Runs when "Select Country" is clicked. findChildren(QRadioButton) (see
    # _checkbox.py for the same pattern with QCheckBox) collects every radio
    # button inside the country group box, and we loop through to find
    # whichever one is currently checked.
    def get_selected_country(self):
        items = self.ui.group_box_country.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_country.setText('selected country: '+ rb.text())

    # Runs when "Select Education" is clicked -- same idea, scoped to the
    # education group box instead.
    def get_selected_education(self):
        items = self.ui.group_box_education.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_education.setText('selected education: '+ rb.text())

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
