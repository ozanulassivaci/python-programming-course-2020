import sys
from PyQt5 import QtWidgets
from _dateForm import Ui_MainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime

# Demonstrates QDate: picking two dates with QDateEdit widgets (see
# _dateForm.py) and doing simple date arithmetic on them. Same generated-UI
# + app-class split as the other examples in this folder.
class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnCalculate.clicked.connect(self.calculate)

    # Runs when "PushButton" (Calculate) is clicked.
    def calculate(self):
        # QDate has some handy built-in helpers for date math, no need
        # to compute day differences by hand.
        # .date() reads the QDateEdit widget's currently selected value as a
        # QDate object (a value representing just a calendar date, with no
        # time-of-day component).
        start = self.ui.dateStart.date()
        end = self.ui.dateEnd.date()
        print(start, end)

        # daysInMonth()/daysInYear() report how many days are in the month
        # / year that `start` falls in (e.g. daysInMonth() would be 28, 29,
        # 30, or 31 depending on the month, and correctly accounts for leap
        # years for daysInYear()).
        print('Days in month: {0}'.format(start.daysInMonth()))
        print('Days in year: {0}'.format(start.daysInYear()))

        # daysTo(other) returns the number of days between this date and
        # another QDate, as a plain integer (negative if `other` is earlier
        # than `start`). This one line replaces what would otherwise be
        # fiddly manual calendar math (accounting for different month
        # lengths, leap years, etc.).
        print('total days: {0}'.format(start.daysTo(end)))

        # QDate.currentDate() is a "static" method -- called on the class
        # itself (QDate), not on an existing QDate instance -- that returns
        # today's date according to the system clock.
        now = QDate.currentDate()

        print('total days from now: {0}'.format(start.daysTo(now)))


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = MyApp()
    win.show()
    sys.exit(app.exec_())

app()
