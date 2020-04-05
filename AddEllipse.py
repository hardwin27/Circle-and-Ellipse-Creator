# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addellipse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddEllipse(QtWidgets.QMainWindow):

    signal = QtCore.pyqtSignal(int, int, int, int, int, int, int, int, str)
    
    def setupUi(self, AddEllipse):
        AddEllipse.setObjectName("AddEllipse")
        AddEllipse.resize(250, 320)
        self.centralwidget = QtWidgets.QWidget(AddEllipse)
        self.centralwidget.setObjectName("centralwidget")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.lineEllipseName = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEllipseName.setGeometry(QtCore.QRect(110, 8, 113, 22))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEllipseName.setFont(font)
        self.lineEllipseName.setObjectName("lineEllipseName")

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.spinBEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBEllipse.setGeometry(QtCore.QRect(170, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBEllipse.setFont(font)
        self.spinBEllipse.setMinimum(0)
        self.spinBEllipse.setMaximum(1000)
        self.spinBEllipse.setObjectName("spinBEllipse")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 50, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.spinYEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinYEllipse.setGeometry(QtCore.QRect(50, 90, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinYEllipse.setFont(font)
        self.spinYEllipse.setMinimum(0)
        self.spinYEllipse.setMaximum(720)
        self.spinYEllipse.setObjectName("spinYEllipse")

        self.spinXEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinXEllipse.setGeometry(QtCore.QRect(50, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinXEllipse.setFont(font)
        self.spinXEllipse.setMinimum(0)
        self.spinXEllipse.setMaximum(1280)
        self.spinXEllipse.setObjectName("spinXEllipse")

        self.spinEllipseThickness = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEllipseThickness.setGeometry(QtCore.QRect(160, 140, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEllipseThickness.setFont(font)
        self.spinEllipseThickness.setMinimum(1)
        self.spinEllipseThickness.setMaximum(5)
        self.spinEllipseThickness.setObjectName("spinEllipseThickness")

        self.spinAEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinAEllipse.setGeometry(QtCore.QRect(170, 50, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinAEllipse.setFont(font)
        self.spinAEllipse.setMinimum(0)
        self.spinAEllipse.setMaximum(1000)
        self.spinAEllipse.setObjectName("spinAEllipse")

        self.btnOkEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkEllipse.setGeometry(QtCore.QRect(70, 280, 93, 28))
        self.btnOkEllipse.setObjectName("btnOkEllipse")
        self.btnOkEllipse.clicked.connect(self.btnOkEllipseClicked)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 90, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 90, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(12, 180, 221, 91))
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
        self.spinGreenEllipse.setGeometry(QtCore.QRect(80, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinGreenEllipse.setFont(font)
        self.spinGreenEllipse.setMinimum(0)
        self.spinGreenEllipse.setMaximum(255)
        self.spinGreenEllipse.setObjectName("spinGreenEllipse")

        self.spinBlueEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinBlueEllipse.setGeometry(QtCore.QRect(150, 50, 60, 30))
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
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(80, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(150, 20, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")

        AddEllipse.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddEllipse)
        QtCore.QMetaObject.connectSlotsByName(AddEllipse)

    def btnOkEllipseClicked(self):
        self.signal.emit(self.spinXEllipse.value(), self.spinYEllipse.value(), self.spinAEllipse.value(), self.spinBEllipse.value(), self.spinEllipseThickness.value(), self.spinRedEllipse.value(), self.spinGreenEllipse.value(), self.spinBlueEllipse.value(), self.lineEllipseName.text())

    def retranslateUi(self, AddEllipse):
        _translate = QtCore.QCoreApplication.translate
        AddEllipse.setWindowTitle(_translate("AddEllipse", "Add Ellipse"))
        self.label_5.setText(_translate("AddEllipse", "Name : "))
        self.label_9.setText(_translate("AddEllipse", "Thickness : "))
        self.spinBEllipse.setToolTip(_translate("AddEllipse", "Set radius B for ellipse (in pixels)"))
        self.label_4.setText(_translate("AddEllipse", "A : "))
        self.spinYEllipse.setToolTip(_translate("AddEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinXEllipse.setToolTip(_translate("AddEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinAEllipse.setToolTip(_translate("AddEllipse", "Set radius A for ellipse (in pixels)"))
        self.btnOkEllipse.setText(_translate("AddEllipse", "OK"))
        self.label.setText(_translate("AddEllipse", "X : "))
        self.label_3.setText(_translate("AddEllipse", "B : "))
        self.label_2.setText(_translate("AddEllipse", "Y : "))
        self.groupBox.setTitle(_translate("AddEllipse", "Color"))
        self.spinRedEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.spinGreenEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.spinBlueEllipse.setToolTip(_translate("AddEllipse", "Set X for circle\'s center (in pixels)"))
        self.label_6.setText(_translate("AddEllipse", "Red"))
        self.label_7.setText(_translate("AddEllipse", "Green"))
        self.label_8.setText(_translate("AddEllipse", "Blue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddEllipse = QtWidgets.QMainWindow()
    ui = Ui_AddEllipse()
    ui.setupUi(AddEllipse)
    AddEllipse.show()
    sys.exit(app.exec_())
