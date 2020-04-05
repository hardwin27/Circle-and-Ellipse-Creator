# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editcircle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditCircle(QtWidgets.QMainWindow):

    signalComboCircleNameIndexChanged = QtCore.pyqtSignal(int)
    signalBtnOkEditCircleClicked = QtCore.pyqtSignal(int, int, int, int, int, int, int, int)

    def setupUi(self, EditCircle):
        EditCircle.setObjectName("EditCircle")
        EditCircle.resize(250, 350)
        self.centralwidget = QtWidgets.QWidget(EditCircle)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 100, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.spinEditXCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditXCircle.setGeometry(QtCore.QRect(50, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditXCircle.setFont(font)
        self.spinEditXCircle.setMinimum(0)
        self.spinEditXCircle.setMaximum(1280)
        self.spinEditXCircle.setObjectName("spinEditXCircle")

        self.spinEditYCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditYCircle.setGeometry(QtCore.QRect(50, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditYCircle.setFont(font)
        self.spinEditYCircle.setMinimum(0)
        self.spinEditYCircle.setMaximum(720)
        self.spinEditYCircle.setObjectName("spinEditYCircle")

        self.spinEditRCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditRCircle.setGeometry(QtCore.QRect(170, 100, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditRCircle.setFont(font)
        self.spinEditRCircle.setMinimum(0)
        self.spinEditRCircle.setMaximum(1000)
        self.spinEditRCircle.setObjectName("spinEditRCircle")

        self.btnOkEditCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkEditCircle.setGeometry(QtCore.QRect(70, 310, 93, 28))
        self.btnOkEditCircle.setObjectName("btnOkEditCircle")
        self.btnOkEditCircle.clicked.connect(self.btnOkEditCircleClicked)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        self.comboCircleName = QtWidgets.QComboBox(self.centralwidget)
        self.comboCircleName.setGeometry(QtCore.QRect(70, 30, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboCircleName.setFont(font)
        self.comboCircleName.setObjectName("comboCircleName")
        self.comboCircleName.currentIndexChanged.connect(self.comboCircleNameIndexChanged)

        self.spinEditCircleThickness = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditCircleThickness.setGeometry(QtCore.QRect(160, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditCircleThickness.setFont(font)
        self.spinEditCircleThickness.setMinimum(1)
        self.spinEditCircleThickness.setMaximum(5)
        self.spinEditCircleThickness.setObjectName("spinEditCircleThickness")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(12, 210, 221, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.spinEditRedCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditRedCircle.setGeometry(QtCore.QRect(10, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditRedCircle.setFont(font)
        self.spinEditRedCircle.setMinimum(0)
        self.spinEditRedCircle.setMaximum(255)
        self.spinEditRedCircle.setObjectName("spinEditRedCircle")

        self.spinEditGreenCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditGreenCircle.setGeometry(QtCore.QRect(80, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditGreenCircle.setFont(font)
        self.spinEditGreenCircle.setMinimum(0)
        self.spinEditGreenCircle.setMaximum(255)
        self.spinEditGreenCircle.setObjectName("spinEditGreenCircle")

        self.spinEditBlueCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditBlueCircle.setGeometry(QtCore.QRect(150, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditBlueCircle.setFont(font)
        self.spinEditBlueCircle.setMinimum(0)
        self.spinEditBlueCircle.setMaximum(255)
        self.spinEditBlueCircle.setObjectName("spinEditBlueCircle")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(80, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(150, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")

        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.btnOkEditCircle.raise_()
        self.spinEditXCircle.raise_()
        self.spinEditYCircle.raise_()
        self.spinEditRCircle.raise_()
        self.label_8.raise_()
        self.comboCircleName.raise_()
        self.spinEditCircleThickness.raise_()
        self.label_9.raise_()
        self.groupBox.raise_()
        
        EditCircle.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditCircle)
        QtCore.QMetaObject.connectSlotsByName(EditCircle)

    def comboCircleNameIndexChanged(self):
        self.signalComboCircleNameIndexChanged.emit(int(self.comboCircleName.currentIndex()))

    def btnOkEditCircleClicked(self):
        self.signalBtnOkEditCircleClicked.emit(self.comboCircleName.currentIndex(), self.spinEditXCircle.value(), self.spinEditYCircle.value(), self.spinEditRCircle.value(), self.spinEditCircleThickness.value(), self.spinEditRedCircle.value(), self.spinEditGreenCircle.value(), self.spinEditBlueCircle.value())

    def retranslateUi(self, EditCircle):
        _translate = QtCore.QCoreApplication.translate
        EditCircle.setWindowTitle(_translate("EditCircle", "Edit Circle"))
        self.label.setText(_translate("EditCircle", "X : "))
        self.label_2.setText(_translate("EditCircle", "Y : "))
        self.label_3.setText(_translate("EditCircle", "R : "))
        self.spinEditXCircle.setToolTip(_translate("EditCircle", "Set X for circle\'s center (in pixels)"))
        self.spinEditYCircle.setToolTip(_translate("EditCircle", "Set Y for circle\'s center (in pixels)"))
        self.spinEditRCircle.setToolTip(_translate("EditCircle", "Set Radius for circle (in pixels)"))
        self.btnOkEditCircle.setText(_translate("EditCircle", "OK"))
        self.label_8.setText(_translate("EditCircle", "Select Circle"))
        self.label_9.setText(_translate("EditCircle", "Thickness :"))
        self.groupBox.setTitle(_translate("EditCircle", "Color"))
        self.spinEditRedCircle.setToolTip(_translate("EditCircle", "Set X for circle\'s center (in pixels)"))
        self.spinEditGreenCircle.setToolTip(_translate("EditCircle", "Set X for circle\'s center (in pixels)"))
        self.spinEditBlueCircle.setToolTip(_translate("EditCircle", "Set X for circle\'s center (in pixels)"))
        self.label_6.setText(_translate("EditCircle", "Red"))
        self.label_7.setText(_translate("EditCircle", "Green"))
        self.label_10.setText(_translate("EditCircle", "Blue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditCircle = QtWidgets.QMainWindow()
    ui = Ui_EditCircle()
    ui.setupUi(EditCircle)
    EditCircle.show()
    sys.exit(app.exec_())
