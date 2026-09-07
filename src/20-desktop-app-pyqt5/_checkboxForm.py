# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_checkbox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(498, 368)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_get_hobbies = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_hobbies.setGeometry(QtCore.QRect(80, 190, 111, 41))
        self.btn_get_hobbies.setObjectName("btnHobilerSecilenleriAl")
        self.lbl_result_hobbies = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_hobbies.setGeometry(QtCore.QRect(80, 240, 111, 101))
        self.lbl_result_hobbies.setText("")
        self.lbl_result_hobbies.setObjectName("lblResultHobiler")
        self.group_hobbies = QtWidgets.QGroupBox(self.centralwidget)
        self.group_hobbies.setGeometry(QtCore.QRect(60, 10, 181, 181))
        self.group_hobbies.setObjectName("groupHobiler")
        self.widget = QtWidgets.QWidget(self.group_hobbies)
        self.widget.setGeometry(QtCore.QRect(30, 30, 111, 111))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.cb_cinema = QtWidgets.QCheckBox(self.widget)
        self.cb_cinema.setObjectName("cbSinema")
        self.verticalLayout.addWidget(self.cb_cinema)
        self.cb_reading = QtWidgets.QCheckBox(self.widget)
        self.cb_reading.setObjectName("cbKitapOkumak")
        self.verticalLayout.addWidget(self.cb_reading)
        self.cb_sports = QtWidgets.QCheckBox(self.widget)
        self.cb_sports.setObjectName("cbSpor")
        self.verticalLayout.addWidget(self.cb_sports)
        self.group_subjects = QtWidgets.QGroupBox(self.centralwidget)
        self.group_subjects.setGeometry(QtCore.QRect(270, 10, 181, 181))
        self.group_subjects.setObjectName("groupDersler")
        self.layoutWidget = QtWidgets.QWidget(self.group_subjects)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 111, 111))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cb_web_design = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_web_design.setObjectName("cbWebTasarim")
        self.verticalLayout_2.addWidget(self.cb_web_design)
        self.cb_programming = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_programming.setObjectName("cbProgramlama")
        self.verticalLayout_2.addWidget(self.cb_programming)
        self.cb_math = QtWidgets.QCheckBox(self.layoutWidget)
        self.cb_math.setObjectName("cbMatematik")
        self.verticalLayout_2.addWidget(self.cb_math)
        self.btn_get_subjects = QtWidgets.QPushButton(self.centralwidget)
        self.btn_get_subjects.setGeometry(QtCore.QRect(270, 190, 111, 41))
        self.btn_get_subjects.setObjectName("btnDerslerSecilenleriAl")
        self.lbl_result_subjects = QtWidgets.QLabel(self.centralwidget)
        self.lbl_result_subjects.setGeometry(QtCore.QRect(270, 240, 111, 101))
        self.lbl_result_subjects.setText("")
        self.lbl_result_subjects.setObjectName("lblResultDersler")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 498, 18))
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
        self.btn_get_hobbies.setText(_translate("MainWindow", "Get Selected"))
        self.group_hobbies.setTitle(_translate("MainWindow", "GroupBox"))
        self.cb_cinema.setText(_translate("MainWindow", "Cinema"))
        self.cb_reading.setText(_translate("MainWindow", "Reading"))
        self.cb_sports.setText(_translate("MainWindow", "Sports"))
        self.group_subjects.setTitle(_translate("MainWindow", "GroupBox"))
        self.cb_web_design.setText(_translate("MainWindow", "Web Design"))
        self.cb_programming.setText(_translate("MainWindow", "Programming"))
        self.cb_math.setText(_translate("MainWindow", "Math"))
        self.btn_get_subjects.setText(_translate("MainWindow", "Get Selected"))
