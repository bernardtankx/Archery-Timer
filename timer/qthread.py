from PyQt5 import QtCore, QtGui, QtWidgets


class LCDNumber(QtCore.QThread):
    def __init__(self, lcdnumber, thread, stop):
        QtCore.QThread.__init__(self)
        self.lcdnumber = lcdnumber
        self.thread = thread
        self.stop = stop

    def run(self):
        while not self.stop.is_set():
            self.lcdnumber.setProperty("intValue", self.thread.seconds)
