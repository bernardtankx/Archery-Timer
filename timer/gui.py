# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AutoTimer(object):
    def setupUi(self, AutoTimer):
        AutoTimer.setObjectName("AutoTimer")
        AutoTimer.resize(480, 320)
        icon = QtGui.QIcon()
        icon_loc = resource_path(os.path.join('data', 'watch.ico'))
        icon.addPixmap(QtGui.QPixmap(icon_loc), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AutoTimer.setWindowIcon(icon)
        self.fourMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.fourMinuteBtn.setGeometry(QtCore.QRect(190, 220, 70, 90))
        self.fourMinuteBtn.setObjectName("fourMinuteBtn")
        self.twoMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.twoMinuteBtn.setGeometry(QtCore.QRect(10, 220, 70, 90))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twoMinuteBtn.sizePolicy().hasHeightForWidth())
        self.twoMinuteBtn.setSizePolicy(sizePolicy)
        self.twoMinuteBtn.setMinimumSize(QtCore.QSize(0, 0))
        self.twoMinuteBtn.setIconSize(QtCore.QSize(16, 16))
        self.twoMinuteBtn.setObjectName("twoMinuteBtn")
        self.stopBtn = QtWidgets.QPushButton(AutoTimer)
        self.stopBtn.setGeometry(QtCore.QRect(320, 110, 145, 95))
        self.stopBtn.setObjectName("stopBtn")
        self.lcdNumber = QtWidgets.QLCDNumber(AutoTimer)
        self.lcdNumber.setGeometry(QtCore.QRect(9, 9, 300, 200))
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setProperty("intValue", 0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.threeMinuteBtn = QtWidgets.QRadioButton(AutoTimer)
        self.threeMinuteBtn.setGeometry(QtCore.QRect(100, 220, 70, 90))
        self.threeMinuteBtn.setObjectName("threeMinuteBtn")
        self.startBtn = QtWidgets.QPushButton(AutoTimer)
        self.startBtn.setGeometry(QtCore.QRect(320, 10, 145, 95))
        self.startBtn.setObjectName("startBtn")
        self.spinBox_numEnds = QtWidgets.QSpinBox(AutoTimer)
        self.spinBox_numEnds.setGeometry(QtCore.QRect(320, 210, 145, 45))
        self.spinBox_numEnds.setObjectName("spinBox_numEnds")
        self.label_ends = QtWidgets.QLabel(AutoTimer)
        self.label_ends.setGeometry(QtCore.QRect(270, 220, 47, 21))
        self.label_ends.setTextFormat(QtCore.Qt.AutoText)
        self.label_ends.setScaledContents(False)
        self.label_ends.setObjectName("label_ends")
        self.spinBox_numArrows = QtWidgets.QSpinBox(AutoTimer)
        self.spinBox_numArrows.setGeometry(QtCore.QRect(320, 260, 145, 45))
        self.spinBox_numArrows.setObjectName("spinBox_numArrows")
        self.label_arrows = QtWidgets.QLabel(AutoTimer)
        self.label_arrows.setGeometry(QtCore.QRect(270, 270, 47, 21))
        self.label_arrows.setTextFormat(QtCore.Qt.AutoText)
        self.label_arrows.setScaledContents(False)
        self.label_arrows.setObjectName("label_arrows")

        self.retranslateUi(AutoTimer)
        QtCore.QMetaObject.connectSlotsByName(AutoTimer)

    def retranslateUi(self, AutoTimer):
        _translate = QtCore.QCoreApplication.translate
        AutoTimer.setWindowTitle(_translate("AutoTimer", "Auto Timer"))
        self.fourMinuteBtn.setText(_translate("AutoTimer", "4 Minute"))
        self.twoMinuteBtn.setText(_translate("AutoTimer", "2 Minute"))
        self.stopBtn.setText(_translate("AutoTimer", "Stop"))
        self.threeMinuteBtn.setText(_translate("AutoTimer", "3 Minute"))
        self.startBtn.setText(_translate("AutoTimer", "Start"))
        self.label_ends.setText(_translate("AutoTimer", "Ends"))
        self.label_arrows.setText(_translate("AutoTimer", "Arrows"))


def resource_path(relative):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative)
    return os.path.join(relative)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AutoTimer = QtWidgets.QDialog()
    ui = Ui_AutoTimer()
    ui.setupUi(AutoTimer)
    AutoTimer.show()
    sys.exit(app.exec_())
