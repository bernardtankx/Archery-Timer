import sys
import timer
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_AutoTimer


class AutoTimer(Ui_AutoTimer):
    def __init__(self, dialog):
        Ui_AutoTimer.__init__(self)
        self.setupUi(dialog)

        self._fourMin = False
        self._threeMin = False
        self._twoMin = False

        self.t_stop = threading.Event()

        self.t4 = timer.Timer(4, self.t_stop)
        self.t3 = timer.Timer(3, self.t_stop)
        self.t2 = timer.Timer(2, self.t_stop)

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
        self.t_stop.clear()
        if self._fourMin:
            self.t4 = timer.Timer(4, self.t_stop)
            self.t4.start()
        elif self._threeMin:
            self.t3 = timer.Timer(3, self.t_stop)
            self.t3.start()
        elif self._twoMin:
            self.t2 = timer.Timer(2, self.t_stop)
            self.t2.start()

    def stop(self):
        self.t_stop.set()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = AutoTimer(dialog)

    dialog.show()

    sys.exit(app.exec_())
