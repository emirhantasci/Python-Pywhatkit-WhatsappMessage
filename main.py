# -*- coding: utf-8 -*-
"""


@author: emirh
"""
import sys
import time
import datetime
import pywhatkit as pwt
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QMainWindow, QMessageBox, QTableWidgetItem             
from PyQt5 import QtCore # timer için
from PyQt5.QtCore import QTime
from anasayfa import *


app1=QtWidgets.QApplication(sys.argv)
MainWindow1=QtWidgets.QMainWindow()
ui1= Ui_MainWindow() #Bu satır değişir
ui1.setupUi(MainWindow1)

x = datetime.datetime.now()
xa = str(x)
dtSaat = xa[11:13]
dtDakika= xa[14:16]
dtSaat2= int(dtSaat)
dtDakika2 = int(dtDakika)+1
ui1.timeEdit.setTime(QTime(dtSaat2, dtDakika2))
MainWindow1.show()


def gonder():
    ui1.statusbar.showMessage(" ")
    
    
    telno = ui1.lineEdit.text()
    message = ui1.textEdit.toPlainText()
    saat = ui1.timeEdit.text()
    saat1 = saat[0:2]
    saat2= saat[3:5]
    telefonNo = "+9" + telno
    pwt.sendwhatmsg(telefonNo, message, int(saat1), int(saat2))
    ui1.statusbar.showMessage(" Mesaj başarıyla gönderildi.")
    time.sleep(2)
    ui1.statusbar.showMessage(" ")


ui1.pushButton.clicked.connect(gonder)
sys.exit(app1.exec_())