from PyQt5 import QtWidgets
import sys
from _radiobuttonForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.radio_turkey.setChecked(True)
        self.ui.radio_high_school.setChecked(True)

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

    def on_country_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            print('selected country: '+ rb.text())

    def on_education_clicked(self):
        rb = self.sender()
        if rb.isChecked():
            print('selected education: '+ rb.text())

    def get_selected_country(self):
        items = self.ui.group_box_country.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_country.setText('selected country: '+ rb.text())

    def get_selected_education(self):
        items = self.ui.group_box_education.findChildren(QtWidgets.QRadioButton)
        for rb in items:
            if rb.isChecked():
                self.ui.lbl_education.setText('selected education: '+ rb.text())

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
