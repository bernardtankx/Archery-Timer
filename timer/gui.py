# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AutoTimer(object):
    def setupUi(self, AutoTimer):
        AutoTimer.setObjectName("AutoTimer")
        AutoTimer.resize(319, 296)
        self.fourMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.fourMinuteBtn.setGeometry(QtCore.QRect(210, 270, 93, 17))
        self.fourMinuteBtn.setObjectName("fourMinuteBtn")
        self.twoMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.twoMinuteBtn.setGeometry(QtCore.QRect(10, 270, 93, 17))
        self.twoMinuteBtn.setObjectName("twoMinuteBtn")
        self.stopBtn = QtWidgets.QPushButton(AutoTimer)
        self.stopBtn.setGeometry(QtCore.QRect(9, 237, 301, 23))
        self.stopBtn.setObjectName("stopBtn")
        self.lcdNumber = QtWidgets.QLCDNumber(AutoTimer)
        self.lcdNumber.setGeometry(QtCore.QRect(9, 9, 301, 191))
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 111.0)
        self.lcdNumber.setProperty("intValue", 111)
        self.lcdNumber.setObjectName("lcdNumber")
        self.threeMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.threeMinuteBtn.setGeometry(QtCore.QRect(110, 270, 93, 17))
        self.threeMinuteBtn.setObjectName("threeMinuteBtn")
        self.startBtn = QtWidgets.QPushButton(AutoTimer)
        self.startBtn.setGeometry(QtCore.QRect(9, 208, 301, 23))
        self.startBtn.setObjectName("startBtn")

        self.retranslateUi(AutoTimer)
        QtCore.QMetaObject.connectSlotsByName(AutoTimer)

    def retranslateUi(self, AutoTimer):
        _translate = QtCore.QCoreApplication.translate
        AutoTimer.setWindowTitle(_translate("AutoTimer", "Auto Timer"))
        self.fourMinuteBtn.setText(_translate("AutoTimer", "4 Minute Timer"))
        self.twoMinuteBtn.setText(_translate("AutoTimer", "2 Minute Timer"))
        self.stopBtn.setText(_translate("AutoTimer", "Stop"))
        self.threeMinuteBtn.setText(_translate("AutoTimer", "3 Minute Timer"))
        self.startBtn.setText(_translate("AutoTimer", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoTimer = QtWidgets.QDialog()
    ui = Ui_AutoTimer()
    ui.setupUi(AutoTimer)
    AutoTimer.show()
    sys.exit(app.exec_())

