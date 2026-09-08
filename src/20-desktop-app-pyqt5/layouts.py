import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPalette, QColor

# The earlier examples (win-class.py, win-items.py) positioned every widget
# by hand with move()/resize() -- "absolute positioning". That's fragile:
# if the window is resized, or you add one more widget, you have to
# recalculate every coordinate yourself. PyQt5's LAYOUT classes solve this:
# you add widgets to a layout and just describe their relationship (e.g.
# "these three go side by side"), and the layout automatically computes
# positions and sizes for you -- including re-arranging everything if the
# window is resized. This file demonstrates QHBoxLayout (horizontal),
# QVBoxLayout (vertical), and (commented out) QGridLayout (rows/columns).

# QWidget is the base class almost every visible thing in Qt inherits from
# (QMainWindow, QLabel, QPushButton... all are QWidgets underneath). Here we
# subclass it directly to make a simple colored rectangle we can drop into a
# layout, just so the layouts below have something visible to arrange.
class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        # A widget doesn't paint its own background by default -- normally
        # you'd draw content in it explicitly. setAutoFillBackground(True)
        # tells Qt to automatically fill the widget's background using its
        # "palette" (the color scheme below), which is a quick way to get a
        # plain colored box without writing custom paint code.
        self.setAutoFillBackground(True)

        # Every widget has a QPalette: a set of colors it uses for different
        # roles (background, text, highlight, etc.). self.palette() fetches
        # this widget's current palette so we can tweak it, then
        # setPalette() applies the modified copy back to the widget.
        palette = self.palette()
        # QPalette.Window is the role used for a plain background fill.
        # QColor(color) builds a color object from a name string (e.g.
        # 'red', 'blue') -- Qt understands a wide range of standard color
        # names as well as '#rrggbb' hex codes.
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setGeometry(100,100,500,500)

        # QHBoxLayout arranges the widgets added to it in a horizontal row,
        # left to right, automatically dividing up the available space
        # between them (by default, roughly equally).
        hlayout1 = QtWidgets.QHBoxLayout()
        hlayout1.addWidget(Color('red'))
        hlayout1.addWidget(Color('blue'))
        hlayout1.addWidget(Color('green'))
        # hlayout1.setContentsMargins(30,20,0,30)
        # setSpacing() sets the gap, in pixels, left between neighboring
        # widgets inside the layout.
        hlayout1.setSpacing(50)

        hlayout2 = QtWidgets.QHBoxLayout()
        hlayout2.addWidget(Color('red'))
        hlayout2.addWidget(Color('green'))
        hlayout2.setSpacing(20)

        # QVBoxLayout arranges things vertically, top to bottom. Layouts can
        # be nested: addLayout() puts an entire other layout (with
        # everything inside it) into this one as if it were a single item.
        # So the final result is two horizontal rows (hlayout1 on top,
        # hlayout2 below it), stacked vertically.
        vlayout = QtWidgets.QVBoxLayout()
        vlayout.addLayout(hlayout1)
        vlayout.addLayout(hlayout2)

        # QGridLayout arranges widgets in a table of rows and columns.
        # addWidget(widget, row, column) places a widget at that grid cell
        # (rows/columns that are skipped, like column 1 and 2 below, are
        # simply left empty). This whole block is commented out and not
        # actually used in this example, but it's left here to show the
        # alternative to QHBoxLayout/QVBoxLayout for grid-shaped UIs (see
        # calculator.py's ui file / other _*Form.py files for real grid
        # layouts).
        # layout = QtWidgets.QGridLayout()

        # layout.addWidget(Color('red'),0,0)
        # layout.addWidget(Color('blue'),1,0)
        # layout.addWidget(Color('green'),0,2)
        # layout.addWidget(Color('yellow'),3,3)

        # A layout can't be applied straight onto a QMainWindow -- Qt
        # requires a QMainWindow's content to live inside one "central
        # widget". So the usual pattern is: build a plain QWidget, give IT
        # the layout via setLayout(), and then hand that widget to the
        # window with setCentralWidget(). Everything inside vlayout (both
        # rows of colored boxes) now appears inside the window.
        widget = QWidget()
        widget.setLayout(vlayout)

        self.setCentralWidget(widget)

def app():
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())

app()
