import sys
import time
import thread_pyqt_lcdnumber
import thread_timer
from PyQt5 import QtCore, QtWidgets
from gui import Ui_AutoTimer


class AutoTimer(Ui_AutoTimer):
    def __init__(self, dialog):
        Ui_AutoTimer.__init__(self)
        self.setupUi(dialog)

        self._fourMin = False
        self._threeMin = False
        self._twoMin = False

        self.t_stop = QtCore.QEvent(0)

        self.t4 = thread_timer.Timer(4, self.t_stop)
        self.t3 = thread_timer.Timer(3, self.t_stop)
        self.t2 = thread_timer.Timer(2, self.t_stop)
        self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t4, self.t_stop)

        # Connect button with a custom function
        self.fourMinuteBtn.clicked.connect(self.selectFourMin)
        self.threeMinuteBtn.clicked.connect(self.selectThreeMin)
        self.twoMinuteBtn.clicked.connect(self.selectTwoMin)
        self.startBtn.clicked.connect(self.start)
        self.stopBtn.clicked.connect(self.stop)

    def selectFourMin(self):
        self._fourMin = True
        self._threeMin = False
        self._twoMin = False

    def selectThreeMin(self):
        self._fourMin = False
        self._threeMin = True
        self._twoMin = False

    def selectTwoMin(self):
        self._fourMin = False
        self._threeMin = False
        self._twoMin = True

    def start(self):
        self.t_stop.accept()
        time.sleep(0.5)
        self.t_stop.ignore()
        if self._fourMin and not self.t4.isRunning() and not self.t3.isRunning() and not self.t2.isRunning():
            self.t4 = thread_timer.Timer(4, self.t_stop)
            self.t4.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t4, self.t_stop)
            self.t1.start()
        elif self._threeMin and not self.t4.isRunning() and not self.t3.isRunning() and not self.t2.isRunning():
            self.t3 = thread_timer.Timer(3, self.t_stop)
            self.t3.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t3, self.t_stop)
            self.t1.start()
        elif self._twoMin and not self.t4.isRunning() and not self.t3.isRunning() and not self.t2.isRunning():
            self.t2 = thread_timer.Timer(2, self.t_stop)
            self.t2.start()
            self.t1 = thread_pyqt_lcdnumber.LCDNumber(self.lcdNumber, self.t2, self.t_stop)
            self.t1.start()

    def stop(self):
        self.t_stop.accept()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = AutoTimer(dialog)

    dialog.show()

    sys.exit(app.exec_())
