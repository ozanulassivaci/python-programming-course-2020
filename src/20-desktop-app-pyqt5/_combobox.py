from PyQt5 import QtWidgets
import sys
from _comboboxForm import Ui_MainWindow

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        combo = self.ui.combo_cities

        # combo.addItem('Ankara')
        # combo.addItem('Istanbul')
        # combo.addItem('Kocaeli')
        # combo.addItems(['Adana','Izmir','Rize'])

        self.ui.btnLoadItems.clicked.connect(self.load_items)
        self.ui.btnGetItem.clicked.connect(self.get_item)
        self.ui.btnClear.clicked.connect(self.clear_items)

        self.ui.combo_cities.currentIndexChanged.connect(self.selected_index_changed)
        self.ui.combo_cities.currentIndexChanged[str].connect(self.selected_text_changed)

    def clear_items(self):
        self.ui.combo_cities.clear()

    def load_items(self):
        cities = ['Adana','Izmir','Rize']

        self.ui.combo_cities.addItems(cities)

    def get_item(self):
        print(self.ui.combo_cities.currentText())
        print(self.ui.combo_cities.currentIndex())

        count = self.ui.combo_cities.count()
        for index in range(count):
            print(self.ui.combo_cities.itemText(index))

    def selected_index_changed(self, index):
        print(index)

    def selected_text_changed(self, text):
        print(text)

app = QtWidgets.QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
