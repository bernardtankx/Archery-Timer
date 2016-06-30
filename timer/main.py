#!/usr/bin/env python

import sys
import thread_pyqt_lcdnumber
import thread_timer
import threading
from datetime import datetime
from PyQt5 import QtWidgets
from gui import Ui_AutoTimer


class AutoTimer(Ui_AutoTimer):
    def __init__(self, dialog):
        Ui_AutoTimer.__init__(self)
        self.setupUi(dialog)

        self.t_stop = threading.Event()

        self.t4 = thread_timer.Timer(4, self.t_stop)
        self.t3 = thread_timer.Timer(3, self.t_stop)
        self.t2 = thread_timer.Timer(2, self.t_stop)
        self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t4, self.t_stop)

        self.fourMinuteBtn.setChecked(True)

        self.numEnds = 0
        self.spinBox_numEnds.setMinimum(0)
        self.spinBox_numEnds.setSingleStep(1)

        # Connect button with a custom function
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)
        self.spinBox_numEnds.valueChanged.connect(self.getNumEnds)

    def start(self):
        self.numEnds += 1
        self.spinBox_numEnds.setValue(self.numEnds)

        self.t_stop.set()
        if self.t4.is_alive():
            self.t4.join()
        if self.t3.is_alive():
            self.t3.join()
        if self.t2.is_alive():
            self.t2.join()
        self.t_stop.clear()

        if self.fourMinuteBtn.isChecked() and not self.t4.is_alive() and not self.t3.is_alive() and not self.t2.is_alive():
            self.t4 = thread_timer.Timer(4, self.t_stop)
            self.t4.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t4, self.t_stop)
            self.t1.start()
        elif self.threeMinuteBtn.isChecked() and not self.t4.is_alive() and not self.t3.is_alive() and not self.t2.is_alive():
            self.t3 = thread_timer.Timer(3, self.t_stop)
            self.t3.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t3, self.t_stop)
            self.t1.start()
        elif self.twoMinuteBtn.isChecked() and not self.t4.is_alive() and not self.t3.is_alive() and not self.t2.is_alive():
            self.t2 = thread_timer.Timer(2, self.t_stop)
            self.t2.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t2, self.t_stop)
            self.t1.start()

    def stop(self):
        self.t_stop.set()

    def getNumEnds(self):
        self.numEnds = self.spinBox_numEnds.value()

    def writeText(self):
        with open("Training Log.txt", "a") as text_file:
            print("Date: " + "{:%B %d, %Y}".format(datetime.now()) + "    Number of Ends: " + str(self.numEnds) + "    Number of Arrows per End: ", file=text_file)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = AutoTimer(dialog)

    dialog.show()

    sys.exit(app.exec_())
