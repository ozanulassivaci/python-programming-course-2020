from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from _msgboxForm import Ui_MainWindow
import sys

# Demonstrates QMessageBox in more depth than _list.py's quick yes/no
# confirmation: here the popup offers three custom buttons (Ok / Cancel /
# Ignore) with one of them set as the default, and the commented-out code
# at the bottom shows the more flexible, longer way of building the same
# dialog by hand instead of using the QMessageBox.question() shortcut.
class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnExit.clicked.connect(self.showDialog)

    # Runs when "Exit" is clicked.
    def showDialog(self):

        # QMessageBox.question(parent, title, text, buttons, defaultButton)
        # is a convenience "static" method: it builds a whole dialog,
        # shows it, waits for the user, and returns which button was
        # pressed -- all in one call, without needing to construct a
        # QMessageBox object yourself. The buttons argument combines three
        # button flags with the bitwise-or operator `|` (same technique as
        # _list.py's Yes|No dialog) to show Ok, Cancel, and Ignore buttons
        # together. The final argument, QMessageBox.Cancel, marks Cancel as
        # the DEFAULT button -- the one that gets triggered if the user
        # just presses Enter without clicking anything.
        result = QMessageBox.question(self, 'Close Application', 'Are you sure ?', QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore, QMessageBox.Cancel)
        if result == QMessageBox.Ok:
            print('Yes clicked')
            # QtWidgets.qApp is a convenient global reference to the single
            # running QApplication instance (equivalent to calling
            # QApplication.instance()). .quit() tells the event loop
            # (app.exec_(), started in app() below) to stop, which ends the
            # program cleanly -- as opposed to _list.py's close(), which
            # used the more abrupt built-in quit() function.
            QtWidgets.qApp.quit()
        else:
            print('No clicked')

        # The block below is commented out, but it's left in as a worked
        # example of the alternative, more flexible way to show a message
        # box: instead of the one-call QMessageBox.question() shortcut
        # above, you construct a QMessageBox object directly and configure
        # it property by property (title, text, icon, buttons, default
        # button, and even extra "detailed text" hidden behind a
        # "Show Details" expander). This is useful when you need more
        # control than question()/information()/warning() provide -- for
        # example connecting buttonClicked to a custom slot (see
        # popup_button below) to react to exactly which button object was
        # pressed, rather than comparing against a fixed set of standard
        # result codes.
        # msg = QMessageBox()

        # msg.setWindowTitle('Close Application')
        # msg.setText('Are you sure ?')
        # msg.setIcon(QMessageBox.Warning)
        # msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel | QMessageBox.Ignore)
        # msg.setDefaultButton(QMessageBox.Cancel)
        # msg.setDetailedText('details....')
        # msg.buttonClicked.connect(self.popup_button)

        # x = msg.exec_()
        # print(x)

    # def popup_button(self, i):
    #     print(i.text())

    #     if i.text() == 'OK':
    #         print('OKEY...')
    #         QtWidgets.qApp.quit()
    #     elif i.text() == 'Cancel':
    #         print('Cancel...')
    #     else:
    #         print('Ignore...')
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())

app()


