import time
from PyQt5 import QtCore, QtGui, QtWidgets


class LCDNumber(QtCore.QThread):
    def __init__(self, lcdnumber):
        QtCore.QThread.__init__(self)
        self.lcdnumber = lcdnumber

    def run(self):
        count = 0
        while True:
            time.sleep(1)
            self.lcdnumber.setProperty("intValue", count)
            count += 1
