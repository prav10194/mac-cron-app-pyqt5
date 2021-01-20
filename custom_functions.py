from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QTextEdit,
                             QAction, QFileDialog, QApplication)
from PyQt5.QtCore import Qt
import os

def checkCronJob(self):
    try:
        if 'filename' not in globals():
            ui_object.pushButton_2.setText("Add CronJob")
            ui_object.pushButton_2.clicked.connect(addCronJob)
        else:
            cmdOutput = os.popen('ls -la "' + filename[0] + '"').read()
            permissions = cmdOutput.split(" ")[0][0:4]
            if "x" != permissions[-1]:
                ui_object.label_8.setStyleSheet("color: red")
                ui_object.label_8.setText("You need to have executable permissions")
                ui_object.pushButton_3.setEnabled(True)
            else:
                ui_object.label_8.setStyleSheet("color: green") 
                ui_object.label_8.setText("You have executable permissions")
                ui_object.pushButton_2.setText("Add CronJob")
                ui_object.pushButton_2.clicked.connect(addCronJob)
    except Exception as e:
        print(e)
        ui_object.pushButton_2.setText("Add CronJob")
        ui_object.pushButton_2.clicked.connect(addCronJob)

def setObject(ui_object_1):
    global ui_object
    ui_object = ui_object_1

def updateCronJobButton(self):
    ui_object.pushButton_2.setText("Check CronJob")
    ui_object.pushButton_2.clicked.connect(checkCronJob)
    ui_object.label_8.setText("")

def onInputFileButtonClicked(self):
    global filename
    filename = QFileDialog.getOpenFileName(None, "Select script", "", "")
    ui_object.lineEdit.setText("sh " + filename[0])
    ui_object.pushButton_2.setText("Check CronJob")
    ui_object.pushButton_2.clicked.connect(checkCronJob)
    ui_object.label_8.setText("")
    print(filename)

def setPermission(self):
    os.popen('chmod u+x "' + filename[0] + '"')
    ui_object.label_8.setStyleSheet("color: green") 
    ui_object.label_8.setText("Executable permissions granted")
    ui_object.pushButton_2.setText("Add CronJob")
    ui_object.pushButton_2.clicked.connect(addCronJob)

def addCronJob(self):
    os.system('crontab -l > cronfile')
    cronShell = ui_object.lineEdit_2.text() + " " + ui_object.lineEdit_3.text() + " " + ui_object.lineEdit_4.text() + " " + ui_object.lineEdit_5.text() + " " + ui_object.lineEdit_6.text() + " " + ui_object.lineEdit.text()
    os.system('echo "' + cronShell + '" >> cronfile && crontab < cronfile')
    ui_object.label_8.setStyleSheet("color: green") 
    ui_object.label_8.setText("Job added. ")
    ui_object.pushButton_2.clicked.disconnect()