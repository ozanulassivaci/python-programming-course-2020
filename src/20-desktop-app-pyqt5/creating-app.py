import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QToolTip
from PyQt5.QtGui import QIcon

# This is the very first, smallest possible PyQt5 desktop app: it just opens
# an empty window. PyQt5 is a set of Python bindings for the Qt framework, a
# C++ toolkit for building graphical (windowed) desktop applications. "GUI"
# stands for Graphical User Interface -- windows, buttons, text boxes, etc.,
# as opposed to a console/terminal program that only prints text.
#
# A GUI app is built from a tree of "widgets": every visible piece (the
# window itself, buttons, labels, text fields...) is a widget. Widgets are
# combined into a hierarchy, with one top-level window at the root.

def window():
    # QApplication manages the whole application: command-line arguments,
    # application-wide settings, and -- most importantly -- the "event
    # loop" (explained below). Every PyQt5 program needs exactly one
    # QApplication instance, created before any widgets. sys.argv is the
    # list of command-line arguments Python received when it was started;
    # PyQt5 can use it for its own options (like window styling flags), so
    # we hand it over here even though this program doesn't use any.
    app = QApplication(sys.argv)

    # QMainWindow is a ready-made top-level window: a widget that comes with
    # optional built-in areas for a menu bar, toolbars, and a status bar
    # (none of which we're using yet). For a simple standalone window you
    # could also use QWidget, but QMainWindow is the standard base class
    # when you might want to add menus/toolbars/status bars later.
    win = QMainWindow()

    # setWindowTitle() sets the text shown in the window's title bar.
    win.setWindowTitle('First Application')

    # setGeometry(x, y, width, height) positions AND sizes the window in one
    # call: x/y are the pixel coordinates of the window's top-left corner on
    # the screen, and width/height are the window's size in pixels. So this
    # places the window 200px from the left, 200px from the top, and makes
    # it 700x700 pixels.
    win.setGeometry(200,200,700,700)

    # setWindowIcon() sets the small icon shown in the title bar / taskbar.
    # QIcon('icon.png') loads an image file from disk (relative to wherever
    # the script is run from) and wraps it as an icon PyQt5 can display.
    win.setWindowIcon(QIcon('icon.png'))

    # setToolTip() sets the little popup text that appears when the mouse
    # hovers over the widget for a moment. Here it's set on the window
    # itself, so hovering anywhere over the window background shows it.
    win.setToolTip('my tooltip')

    # Widgets are created invisible by default. show() makes the window (and
    # everything inside it) actually appear on screen.
    win.show()

    # app.exec_() starts the Qt "event loop" -- an internal infinite loop
    # that waits for things to happen (mouse clicks, key presses, window
    # resizes, timers...) and dispatches each one to the right widget. Your
    # own Python code doesn't run again until an event occurs; the loop is
    # what keeps the window responsive and on screen instead of the script
    # just ending immediately after show(). exec_() only returns once the
    # user closes the app (or something calls quit()), and it returns an
    # exit status code. sys.exit(...) passes that code back to the
    # operating system as the process's exit code -- this is the standard
    # way every PyQt5 script ends.
    sys.exit(app.exec_())

# Since window() is only defined above, we have to actually call it here for
# anything to happen -- Python doesn't run a function just because it exists.
window()
