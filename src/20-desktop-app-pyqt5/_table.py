from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from _tableForm import Ui_MainWindow
import sys

# Demonstrates QTableWidget: a product list (name + price) shown in a
# spreadsheet-like grid, with a small form on the side to add new rows and
# double-click support to inspect a selected cell. Same generated-UI +
# app-class split as the other examples in this folder.
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.loadProducts()
        self.ui.btnSave.clicked.connect(self.saveProduct)
        # doubleClicked is a signal QTableWidget emits when the user
        # double-clicks a cell. It's connected here even though
        # doubleClick() below doesn't use any info from the click itself --
        # it just re-reads whatever is currently selected in the table.
        self.ui.tableProducts.doubleClicked.connect(self.doubleClick)

    # Runs whenever a cell in the table is double-clicked. selectedItems()
    # returns every QTableWidgetItem currently selected (normally just one,
    # from the double-click). Each item knows its own .row(), .column()
    # (both 0-based grid coordinates) and .text() (the cell's displayed
    # text), which are printed here just to demonstrate reading a cell's
    # position and content back out of the table.
    def doubleClick(self):
        for item in self.ui.tableProducts.selectedItems():
            print(item.row(), item.column(), item.text())


    # Runs when "Save" is clicked: reads the name/price text boxes and adds
    # them as a new row at the bottom of the table.
    def saveProduct(self):
        name = self.ui.txtName.text()
        price = self.ui.txtPrice.text()

        if name and price is not None:
            # rowCount() is the table's current number of rows, which
            # conveniently also equals the index the NEXT new row should go
            # at (rows are 0-indexed, so if there are already 4 rows, index
            # 4 is the next open slot).
            rowCount = self.ui.tableProducts.rowCount()
            print(rowCount)
            # insertRow(index) adds a new, empty row at that position,
            # growing the table's row count by one.
            self.ui.tableProducts.insertRow(rowCount)
            # A QTableWidget cell doesn't hold plain text directly -- each
            # cell needs a QTableWidgetItem object wrapping the text (and
            # optionally other properties like icons, fonts, or flags).
            # setItem(row, column, item) places that item into a specific
            # cell.
            self.ui.tableProducts.setItem(rowCount,0, QTableWidgetItem(name))
            self.ui.tableProducts.setItem(rowCount,1, QTableWidgetItem(price))

    # Called once from __init__ (not a signal handler) to populate the
    # table with sample data when the window first opens.
    def loadProducts(self):

        products = [
            {'name': 'Samsung S5', 'price': 2000},
            {'name': 'Samsung S6', 'price': 3000},
            {'name': 'Samsung S7', 'price': 4000},
            {'name': 'Samsung S8', 'price': 5000}
        ]

        # A QTableWidget needs to be told how many rows and columns it has
        # before you can start filling in cells -- setRowCount()/
        # setColumnCount() allocate the grid.
        self.ui.tableProducts.setRowCount(len(products))
        self.ui.tableProducts.setColumnCount(2)
        # setHorizontalHeaderLabels() sets the column header text shown
        # along the top of the table (here, "Name" and "Price"), given as a
        # tuple in column order.
        self.ui.tableProducts.setHorizontalHeaderLabels(('Name','Price'))
        # setColumnWidth(column, pixels) sets a fixed pixel width for a
        # specific column, so the Name column gets more horizontal room
        # than the Price column.
        self.ui.tableProducts.setColumnWidth(0,200)
        self.ui.tableProducts.setColumnWidth(1,100)

        rowIndex = 0
        for product in products:
            # str(product['price']) is needed because QTableWidgetItem
            # expects a string, but product['price'] is a plain Python int
            # (e.g. 2000) in the products list above.
            self.ui.tableProducts.setItem(rowIndex,0, QTableWidgetItem(product['name']))
            self.ui.tableProducts.setItem(rowIndex,1, QTableWidgetItem(str(product['price'])))

            rowIndex+=1

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()


