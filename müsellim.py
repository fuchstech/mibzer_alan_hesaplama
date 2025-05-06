# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'müsellim.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow():
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(443, 305)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 20, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 20, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 60, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(320, 220, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(100, 60, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(0, 130, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(220, 130, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 443, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.pushButton.clicked.connect(self.alan_sifirla)
        self.pushButton_2.clicked.connect(self.tur_sifirla)
        self.pushButton_3.clicked.connect(self.baslat)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def alan_sifirla(self):
        makina.alan = 0
    def tur_sifirla(self):
        makina.tur = 0
    def baslat(self):
        t1 = Thread()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MüsellimTech"))
        self.label.setText(_translate("MainWindow", "Toplam Alan:"))
        self.pushButton.setText(_translate("MainWindow", "Sıfırla"))
        self.label_2.setText(_translate("MainWindow", "Tur:"))
        self.pushButton_2.setText(_translate("MainWindow", "Sıfırla"))
        self.pushButton_3.setText(_translate("MainWindow", "Başlat"))
        self.label_3.setText(_translate("MainWindow", "400m"))
        self.label_4.setText(_translate("MainWindow", "19"))
        self.label_5.setText(_translate("MainWindow", "Ortalama Hız:"))
        self.label_6.setText(_translate("MainWindow", "14M/S"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())