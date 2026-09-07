# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 343)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 60, 51, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 90, 51, 31))
        self.label_2.setObjectName("label_2")
        self.txt_number1 = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_number1.setGeometry(QtCore.QRect(110, 60, 200, 32))
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

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
