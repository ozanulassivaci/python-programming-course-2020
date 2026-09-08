# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

# --- What this file is and why it looks like this ---
# So far every window in this folder was built by writing Python code by
# hand (QLabel(self), .move(x, y), etc.). PyQt5 also ships a visual editor
# called "Qt Designer" where you drag and drop widgets onto a form and save
# the result as an XML ".ui" file (here, MainWindow.ui, sitting next to this
# file). This MainWindow.py file was NOT typed by a human -- it was produced
# automatically by a command-line tool called "pyuic5" (part of PyQt5) that
# reads MainWindow.ui and translates every widget in it into the equivalent
# Python widget-creation code, following the exact same patterns you've
# already seen (QtWidgets.QLabel(...), setGeometry(...), etc.).
#
# The big warning comment above is important: if you re-run pyuic5 on the
# .ui file (e.g. after editing the form in Qt Designer again), this whole
# file gets overwritten from scratch. So you never hand-edit generated files
# like this one -- instead you edit the .ui file (usually visually in Qt
# Designer) and regenerate. The actual app logic (what happens when a
# button is clicked) is written separately, in a normal class that USES this
# generated class -- see calculator2.py, which imports Ui_MainWindow from
# this file.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    # setupUi() is the method the generator always produces: given an empty
    # QMainWindow instance (passed in as the `MainWindow` parameter), it
    # creates and configures every widget that was placed on the form in Qt
    # Designer. It's meant to be called once, right after creating the
    # window, from whatever class actually uses this UI (see calculator2.py:
    # self.ui.setupUi(self)).
    def setupUi(self, MainWindow):
        # setObjectName() gives a widget an internal name Qt can refer to
        # (used for things like style sheets and Designer's own bookkeeping)
        # -- it doesn't affect what's visible on screen.
        MainWindow.setObjectName("MainWindow")
        # resize(width, height) sets the window's initial size in pixels.
        MainWindow.resize(494, 343)
        # A QMainWindow needs one "central widget" to hold its contents (see
        # the same idea explained in layouts.py). Here it's a plain QWidget
        # with no layout manager -- every child widget below gets its exact
        # position and size set individually via setGeometry(), just like
        # the hand-written examples used move()/resize().
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        # setGeometry(QRect(x, y, width, height)) is the generator's way of
        # combining move() + resize() into one call: QtCore.QRect describes
        # a rectangle (position + size) as a single object. This is
        # equivalent to calling .move(x, y) and .resize(width, height)
        # separately.
        self.label.setGeometry(QtCore.QRect(60, 60, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.txt_number1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_number1.setGeometry(QtCore.QRect(110, 60, 200, 32))
        # Note: this internal object name ("txt_sayi1") still has the
        # original Turkish name from the .ui file, even though the Python
        # attribute it's assigned to (self.txt_number1) was renamed to
        # English. Object names are just internal Qt bookkeeping labels
        # (see setObjectName above) -- they don't need to match the Python
        # variable name, and changing this generated file's object name
        # strings has no effect on behavior, so they were left as-is.
        self.txt_number1.setObjectName("txt_sayi1")
        self.txt_number2 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_number2.setGeometry(QtCore.QRect(110, 100, 200, 32))
        self.txt_number2.setObjectName("txt_sayi2")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(110, 150, 71, 31))
        self.btn_add.setObjectName("btn_toplama")
        self.btn_subtract = QtWidgets.QPushButton(self.centralwidget)
        self.btn_subtract.setGeometry(QtCore.QRect(190, 150, 71, 31))
        self.btn_subtract.setObjectName("btn_cikarma")
        self.btn_divide = QtWidgets.QPushButton(self.centralwidget)
        self.btn_divide.setGeometry(QtCore.QRect(270, 150, 71, 31))
        self.btn_divide.setObjectName("btn_bolme")
        self.btn_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.btn_multiply.setGeometry(QtCore.QRect(350, 180, 71, 31))
        self.btn_multiply.setObjectName("btn_carpma")
        self.lbl_result = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result.setGeometry(QtCore.QRect(110, 200, 121, 21))
        self.lbl_result.setObjectName("lbl_sonuc")
        # Hands the widget we just built to the window as its central
        # widget (see the same call explained in layouts.py).
        MainWindow.setCentralWidget(self.centralwidget)
        # QMenuBar is the horizontal bar at the top of a window that would
        # hold menus like File/Edit/Help (Qt Designer adds an empty one by
        # default even if you never add any menu items, which is the case
        # here).
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        # QStatusBar is the thin bar at the bottom of a window, typically
        # used to show short status messages. Also added empty by default.
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # retranslateUi() (defined below) sets all the visible text labels;
        # it's kept separate from widget creation so that switching the
        # app's language later only requires calling this one method again.
        self.retranslateUi(MainWindow)
        # connectSlotsByName() is Qt's "auto-connect" feature: if you name a
        # method on the window exactly `on_<objectName>_<signalName>` (e.g.
        # on_btn_add_clicked), Qt will connect it to that widget's signal
        # automatically, with no explicit .connect() call needed. Nothing in
        # this project actually uses that naming convention -- calculator2.py
        # wires up its buttons explicitly instead -- but pyuic5 always emits
        # this call just in case.
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # retranslateUi() sets every widget's visible text. QtCore.QCoreApplication.translate
    # is Qt's internationalization (i18n) helper: in an app that supports
    # multiple languages, it would look up the translated version of each
    # string; here, with no translation files installed, it just returns
    # the English text unchanged.
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Number 1:"))
        self.label_2.setText(_translate("MainWindow", "Number 2:"))
        self.btn_add.setText(_translate("MainWindow", "Add"))
        self.btn_subtract.setText(_translate("MainWindow", "Subtract"))
        self.btn_divide.setText(_translate("MainWindow", "Divide"))
        self.btn_multiply.setText(_translate("MainWindow", "Multiply"))
        self.lbl_result.setText(_translate("MainWindow", "Result:"))
