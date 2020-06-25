# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'labgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(468, 330)
        MainWindow.setStyleSheet("background-color:rgb(187, 255, 209)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Button = QtWidgets.QPushButton(self.centralwidget)
        self.Button.setGeometry(QtCore.QRect(170, 240, 121, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Button.setFont(font)
        self.Button.setObjectName("Button")
        self.Input_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_1.setGeometry(QtCore.QRect(40, 30, 131, 41))
        self.Input_1.setStyleSheet("background-color:white")
        self.Input_1.setMaxLength(2)
        self.Input_1.setObjectName("Input_1")
        self.Input_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.Input_2.setGeometry(QtCore.QRect(270, 30, 131, 41))
        self.Input_2.setStyleSheet("background-color:white")
        self.Input_2.setMaxLength(2)
        self.Input_2.setObjectName("Input_2")
        self.int_2 = QtWidgets.QLabel(self.centralwidget)
        self.int_2.setGeometry(QtCore.QRect(80, 0, 41, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.int_2.setFont(font)
        self.int_2.setObjectName("int_2")
        self.int_3 = QtWidgets.QLabel(self.centralwidget)
        self.int_3.setGeometry(QtCore.QRect(290, 0, 111, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.int_3.setFont(font)
        self.int_3.setObjectName("int_3")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(170, 190, 121, 31))
        self.result.setText("")
        self.result.setObjectName("result")
        self.Num = QtWidgets.QLineEdit(self.centralwidget)
        self.Num.setGeometry(QtCore.QRect(170, 120, 121, 41))
        self.Num.setStyleSheet("background-color:white")
        self.Num.setMaxLength(10)
        self.Num.setObjectName("Num")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 468, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Lab4"))
        self.Button.setText(_translate("MainWindow", "Результат"))
        self.int_2.setText(_translate("MainWindow", "Из СС:"))
        self.int_3.setText(_translate("MainWindow", "Перевод в СС:"))
