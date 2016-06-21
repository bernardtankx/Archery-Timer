import sys
import timer
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_AutoTimer


class AutoTimer(Ui_AutoTimer):
    def __init__(self, dialog):
        Ui_AutoTimer.__init__(self)
        self.setupUi(dialog)

        self._fourMin = False
        self._threeMin = False
        self._twoMin = False

        # Connect button with a custom function
        self.fourMinuteBtn.clicked.connect(self.selectFourMin)
        self.threeMinuteBtn.clicked.connect(self.selectThreeMin)
        self.twoMinuteBtn.clicked.connect(self.selectTwoMin)
        self.startBtn.clicked.connect(self.start)
        #self.stopBtn.clicked.connect(self.stop)

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
        if self._fourMin:
            timer.fourmin()
        if self._threeMin:
            timer.threemin()
        if self._twoMin:
            timer.twomin()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()

    prog = AutoTimer(dialog)

    dialog.show()
    sys.exit(app.exec_())
