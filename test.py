# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addellipse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEllipse(QtWidgets.QMainWindow):

    signal = QtCore.pyqtSignal(int, int, int, int, int, int, int, str)

    def setupUi(self, AddEllipse):
        AddEllipse.setObjectName("AddEllipse")
        AddEllipse.resize(220, 335)
        self.centralwidget = QtWidgets.QWidget(AddEllipse)
        self.centralwidget.setObjectName("centralwidget")

        self.btnOkellipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkellipse.setGeometry(QtCore.QRect(60, 300, 93, 28))
        self.btnOkellipse.setObjectName("btnOkellipse")
        self.btnOkellipse.clicked.connect(self.btnOkellipseClicked)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.spinYellipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinYellipse.setGeometry(QtCore.QRect(90, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinYellipse.setFont(font)
        self.spinYellipse.setMinimum(0)
        self.spinYellipse.setMaximum(720)
        self.spinYellipse.setObjectName("spinYellipse")

        self.spinXellipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinXellipse.setGeometry(QtCore.QRect(90, 40, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinXellipse.setFont(font)
        self.spinXellipse.setMinimum(0)
        self.spinXellipse.setMaximum(1280)
        self.spinXellipse.setObjectName("spinXellipse")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 40, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 160, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.spinAellipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinAellipse.setGeometry(QtCore.QRect(90, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinAellipse.setFont(font)
        self.spinAellipse.setMinimum(0)
        self.spinAellipse.setMaximum(1000)
        self.spinAellipse.setObjectName("spinAellipse")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 120, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.spinBellipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBellipse.setGeometry(QtCore.QRect(90, 160, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBellipse.setFont(font)
        self.spinBellipse.setMinimum(0)
        self.spinBellipse.setMaximum(1000)
        self.spinBellipse.setObjectName("spinBellipse")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 2, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEllipseName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEllipseName.setGeometry(QtCore.QRect(90, 10, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEllipseName.setFont(font)
        self.lineEllipseName.setObjectName("lineEllipseName")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 200, 200, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.spinRedEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinRedEllipse.setGeometry(QtCore.QRect(10, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinRedEllipse.setFont(font)
        self.spinRedEllipse.setMinimum(0)
        self.spinRedEllipse.setMaximum(255)
        self.spinRedEllipse.setObjectName("spinRedEllipse")

        self.spinGreenEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinGreenEllipse.setGeometry(QtCore.QRect(70, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinGreenEllipse.setFont(font)
        self.spinGreenEllipse.setMinimum(0)
        self.spinGreenEllipse.setMaximum(255)
        self.spinGreenEllipse.setObjectName("spinGreenEllipse")

        self.spinBlueEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinBlueEllipse.setGeometry(QtCore.QRect(130, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBlueEllipse.setFont(font)
        self.spinBlueEllipse.setMinimum(0)
        self.spinBlueEllipse.setMaximum(255)
        self.spinBlueEllipse.setObjectName("spinBlueEllipse")

        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(72, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(140, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")

        self.btnOkellipse.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.spinXellipse.raise_()
        self.spinYellipse.raise_()
        self.label_3.raise_()
        self.spinAellipse.raise_()
        self.label_4.raise_()
        self.spinBellipse.raise_()
        self.label_5.raise_()
        self.lineEllipseName.raise_()
        self.groupBox.raise_()
        AddEllipse.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEllipse)
        QtCore.QMetaObject.connectSlotsByName(AddEllipse)

    def btnOkellipseClicked(self):
        self.signal.emit(self.spinXellipse.value(), self.spinYellipse.value(), self.spinAellipse.value(), self.spinBellipse.value(), self.spinRedEllipse.value(), self.spinGreenEllipse.value(), self.spinBlueEllipse.value(), self.lineEllipseName.text())

    def retranslateUi(self, AddEllipse):
        _translate = QtCore.QCoreApplication.translate
        AddEllipse.setWindowTitle(_translate("AddEllipse", "Add Ellipse"))
        self.btnOkellipse.setText(_translate("AddEllipse", "OK"))
        self.label_2.setText(_translate("AddEllipse", "Y : "))
        self.spinYellipse.setToolTip(_translate("AddEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinXellipse.setToolTip(_translate("AddEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.label.setText(_translate("AddEllipse", "X : "))
        self.label_3.setText(_translate("AddEllipse", "B : "))
        self.spinAellipse.setToolTip(_translate("AddEllipse", "Set radius A for ellipse (in pixels)"))
        self.label_4.setText(_translate("AddEllipse", "A : "))
        self.spinBellipse.setToolTip(_translate("AddEllipse", "Set radius B for ellipse (in pixels)"))
        self.label_5.setText(_translate("AddEllipse", "Name : "))
        self.groupBox.setTitle(_translate("AddEllipse", "Color"))
        self.spinRedEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.spinGreenEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.spinBlueEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.label_6.setText(_translate("AddEllipse", "Red:"))
        self.label_7.setText(_translate("AddEllipse", "Green:"))
        self.label_8.setText(_translate("AddEllipse", "Blue:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEllipse = QtWidgets.QMainWindow()
    ui = Ui_AddEllipse()
    ui.setupUi(AddEllipse)
    AddEllipse.show()
    sys.exit(app.exec_())
