# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'smmtestui.ui'
#
# Created: Tue Jan 07 12:40:20 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 471, 511))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(200)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.initdatabu = QtGui.QPushButton(self.centralwidget)
        self.initdatabu.setGeometry(QtCore.QRect(640, 30, 81, 31))
        self.initdatabu.setObjectName(_fromUtf8("initdatabu"))
        self.predatabu = QtGui.QPushButton(self.centralwidget)
        self.predatabu.setGeometry(QtCore.QRect(510, 240, 91, 31))
        self.predatabu.setObjectName(_fromUtf8("predatabu"))
        self.prenextdatabu = QtGui.QPushButton(self.centralwidget)
        self.prenextdatabu.setGeometry(QtCore.QRect(510, 330, 91, 31))
        self.prenextdatabu.setObjectName(_fromUtf8("prenextdatabu"))
        self.prepredatabu = QtGui.QPushButton(self.centralwidget)
        self.prepredatabu.setGeometry(QtCore.QRect(510, 150, 91, 31))
        self.prepredatabu.setObjectName(_fromUtf8("prepredatabu"))
        self.selectdatabu = QtGui.QPushButton(self.centralwidget)
        self.selectdatabu.setGeometry(QtCore.QRect(510, 440, 91, 31))
        self.selectdatabu.setObjectName(_fromUtf8("selectdatabu"))

        self.selectcasetext = QtGui.QLabel(self.centralwidget)
        self.selectcasetext.setGeometry(QtCore.QRect(490, 410, 281, 31))
        self.selectcasetext.setObjectName(_fromUtf8("selecttext"))


        self.precasetext = QtGui.QLabel(self.centralwidget)
        self.precasetext.setGeometry(QtCore.QRect(490, 120, 301, 31))
        self.precasetext.setObjectName(_fromUtf8("precasetext"))
        self.casetext = QtGui.QLabel(self.centralwidget)
        self.casetext.setGeometry(QtCore.QRect(490, 190, 281, 41))
        self.casetext.setObjectName(_fromUtf8("casetext"))
        self.nextcasetext = QtGui.QLabel(self.centralwidget)
        self.nextcasetext.setGeometry(QtCore.QRect(490, 300, 301, 21))
        self.nextcasetext.setObjectName(_fromUtf8("nextcasetext"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))

        self.tableWidget.setColumnWidth(0,380)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "用例名称", None))
        self.initdatabu.setText(_translate("MainWindow", "初始化数据", None))
        self.predatabu.setText(_translate("MainWindow", "预置数据", None))
        self.prenextdatabu.setText(_translate("MainWindow", "预置下一用例", None))
        self.prepredatabu.setText(_translate("MainWindow", "预置上一用例", None))
        self.precasetext.setText(_translate("MainWindow", "上一个用例名", None))
        self.casetext.setText(_translate("MainWindow", "现用例名", None))
        self.nextcasetext.setText(_translate("MainWindow", "下一用例名", None))
        self.selectdatabu.setText(_translate("MainWindow", "预置选中用例", None))
