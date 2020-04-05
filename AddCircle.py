# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addcircle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddCircle(QtWidgets.QMainWindow):

    signal = QtCore.pyqtSignal(int, int, int, int, int, int, int, str)

    def setupUi(self, AddCircle):
        AddCircle.setObjectName("AddCircle")
        AddCircle.resize(250, 320)
        self.centralwidget = QtWidgets.QWidget(AddCircle)
        self.centralwidget.setObjectName("centralwidget")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 2, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.lineCircleName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineCircleName.setGeometry(QtCore.QRect(110, 10, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineCircleName.setFont(font)
        self.lineCircleName.setObjectName("lineCircleName")

        self.spinXCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinXCircle.setGeometry(QtCore.QRect(50, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinXCircle.setFont(font)
        self.spinXCircle.setMinimum(0)
        self.spinXCircle.setMaximum(1280)
        self.spinXCircle.setObjectName("spinXCircle")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(12, 180, 221, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.spinRedCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinRedCircle.setGeometry(QtCore.QRect(10, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinRedCircle.setFont(font)
        self.spinRedCircle.setMinimum(0)
        self.spinRedCircle.setMaximum(255)
        self.spinRedCircle.setObjectName("spinRedCircle")

        self.spinGreenCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinGreenCircle.setGeometry(QtCore.QRect(80, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinGreenCircle.setFont(font)
        self.spinGreenCircle.setMinimum(0)
        self.spinGreenCircle.setMaximum(255)
        self.spinGreenCircle.setObjectName("spinGreenCircle")

        self.spinBlueCircle = QtWidgets.QSpinBox(self.groupBox)
        self.spinBlueCircle.setGeometry(QtCore.QRect(150, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBlueCircle.setFont(font)
        self.spinBlueCircle.setMinimum(0)
        self.spinBlueCircle.setMaximum(255)
        self.spinBlueCircle.setObjectName("spinBlueCircle")

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

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 30, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.spinRCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinRCircle.setGeometry(QtCore.QRect(170, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinRCircle.setFont(font)
        self.spinRCircle.setMinimum(0)
        self.spinRCircle.setMaximum(1000)
        self.spinRCircle.setObjectName("spinRCircle")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 70, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.spinYCircle = QtWidgets.QSpinBox(self.centralwidget)
        self.spinYCircle.setGeometry(QtCore.QRect(50, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinYCircle.setFont(font)
        self.spinYCircle.setMinimum(0)
        self.spinYCircle.setMaximum(720)
        self.spinYCircle.setObjectName("spinYCircle")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.btnOkCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkCircle.setGeometry(QtCore.QRect(70, 280, 93, 28))
        self.btnOkCircle.setObjectName("btnOkCircle")
        self.btnOkCircle.clicked.connect(self.btnOkCircleClicked)

        self.spinCircleThickness = QtWidgets.QSpinBox(self.centralwidget)
        self.spinCircleThickness.setGeometry(QtCore.QRect(160, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinCircleThickness.setFont(font)
        self.spinCircleThickness.setMinimum(1)
        self.spinCircleThickness.setMaximum(5)
        self.spinCircleThickness.setObjectName("spinCircleThickness")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        AddCircle.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddCircle)
        QtCore.QMetaObject.connectSlotsByName(AddCircle)

    def btnOkCircleClicked(self):
        self.signal.emit(self.spinXCircle.value(), self.spinYCircle.value(), self.spinRCircle.value(), self.spinCircleThickness.value(), self.spinRedCircle.value(), self.spinGreenCircle.value(), self.spinBlueCircle.value(), self.lineCircleName.text())

    def retranslateUi(self, AddCircle):
        _translate = QtCore.QCoreApplication.translate
        AddCircle.setWindowTitle(_translate("AddCircle", "Add Circle"))
        self.label_4.setText(_translate("AddCircle", "Name : "))
        self.spinXCircle.setToolTip(_translate("AddCircle", "Set X for circle\'s center (in pixels)"))
        self.groupBox.setTitle(_translate("AddCircle", "Color"))
        self.spinRedCircle.setToolTip(_translate("AddCircle", "Set X for circle\'s center (in pixels)"))
        self.spinGreenCircle.setToolTip(_translate("AddCircle", "Set X for circle\'s center (in pixels)"))
        self.spinBlueCircle.setToolTip(_translate("AddCircle", "Set X for circle\'s center (in pixels)"))
        self.label_6.setText(_translate("AddCircle", "Red"))
        self.label_7.setText(_translate("AddCircle", "Green"))
        self.label_10.setText(_translate("AddCircle", "Blue"))
        self.label.setText(_translate("AddCircle", "X : "))
        self.spinRCircle.setToolTip(_translate("AddCircle", "Set Radius for circle (in pixels)"))
        self.label_3.setText(_translate("AddCircle", "R : "))
        self.spinYCircle.setToolTip(_translate("AddCircle", "Set Y for circle\'s center (in pixels)"))
        self.label_2.setText(_translate("AddCircle", "Y : "))
        self.btnOkCircle.setText(_translate("AddCircle", "OK"))
        self.label_9.setText(_translate("AddCircle", "Thickness : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddCircle = QtWidgets.QMainWindow()
    ui = Ui_AddCircle()
    ui.setupUi(AddCircle)
    AddCircle.show()
    sys.exit(app.exec_())
