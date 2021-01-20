# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test-ui-2.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtCore import Qt                             
import sys
from pathlib import Path
import os
from time import sleep
import custom_functions as cf

class Ui_Dialog(object):

    def setupUi(self, Dialog):
        cf.setObject(self)
        Dialog.setObjectName("Dialog")
        Dialog.resize(422, 295)
        Dialog.setFixedSize(422, 295)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(40, 30, 60, 16))
        self.label.setText("")
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 421, 301))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.lineEdit = QtWidgets.QLineEdit(self.tab)
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QtCore.QRect(20, 20, 231, 31))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setToolTipDuration(-1)
        self.lineEdit.setWhatsThis("")
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setPlaceholderText("eg - curl http://example.com")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(cf.updateCronJobButton)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 60, 16))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(10, 120, 113, 32))
        self.pushButton.clicked.connect(cf.onInputFileButtonClicked)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton.setMouseTracking(False)
        self.pushButton.setWhatsThis("")
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 41, 16))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(70, 60, 31, 16))
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(140, 60, 71, 16))
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(230, 60, 41, 16))
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(300, 60, 71, 16))
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 40, 51, 21))
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 40, 51, 21))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(140, 40, 51, 21))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(230, 40, 51, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.tab_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 40, 51, 21))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 110, 131, 32))
        self.pushButton_2.clicked.connect(cf.checkCronJob)
        font = QtGui.QFont()
        font.setFamily("IBM Plex Sans")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(100, 160, 251, 16))
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 190, 131, 32))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(cf.setPermission)
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_3.setText(_translate("Dialog", "OR"))
        self.pushButton.setText(_translate("Dialog", "Select file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Script"))
        self.label_2.setText(_translate("Dialog", "minute"))
        self.label_4.setText(_translate("Dialog", "hour"))
        self.label_5.setText(_translate("Dialog", "day(month)"))
        self.label_6.setText(_translate("Dialog", "month"))
        self.label_7.setText(_translate("Dialog", "day(week)"))
        self.lineEdit_2.setText("0")
        self.lineEdit_3.setText("*")
        self.lineEdit_4.setText("*")
        self.lineEdit_5.setText("*")
        self.lineEdit_6.setText("*")
        self.pushButton_2.setText(_translate("Dialog", "Check CronJob"))
        self.pushButton_3.setText(_translate("Dialog", "Set Permission"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Frequency"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())