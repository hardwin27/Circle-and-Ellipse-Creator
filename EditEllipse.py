# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editellipse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EditEllipse(QtWidgets.QMainWindow):

    signalComboEllipseNameIndexChanged = QtCore.pyqtSignal(int)
    signalBtnOkEditEllipseClicked = QtCore.pyqtSignal(int,int, int, int, int, int, int, int, int)


    def setupUi(self, EditEllipse):
        EditEllipse.setObjectName("EditEllipse")
        EditEllipse.resize(250, 350)
        self.centralwidget = QtWidgets.QWidget(EditEllipse)
        self.centralwidget.setObjectName("centralwidget")

        self.btnEditOkEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditOkEllipse.setGeometry(QtCore.QRect(70, 310, 93, 28))
        self.btnEditOkEllipse.setObjectName("btnEditOkEllipse")
        self.btnEditOkEllipse.clicked.connect(self.btnOkEditEllipseClicked)

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 120, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.spinEditYEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditYEllipse.setGeometry(QtCore.QRect(50, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditYEllipse.setFont(font)
        self.spinEditYEllipse.setMinimum(0)
        self.spinEditYEllipse.setMaximum(720)
        self.spinEditYEllipse.setObjectName("spinEditYEllipse")

        self.spinEditXEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditXEllipse.setGeometry(QtCore.QRect(50, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditXEllipse.setFont(font)
        self.spinEditXEllipse.setMinimum(0)
        self.spinEditXEllipse.setMaximum(1280)
        self.spinEditXEllipse.setObjectName("spinEditXEllipse")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(130, 120, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")

        self.spinEditAEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditAEllipse.setGeometry(QtCore.QRect(170, 80, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditAEllipse.setFont(font)
        self.spinEditAEllipse.setMinimum(0)
        self.spinEditAEllipse.setMaximum(1000)
        self.spinEditAEllipse.setObjectName("spinEditAEllipse")

        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(130, 80, 55, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")

        self.spinEditBEllipse = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditBEllipse.setGeometry(QtCore.QRect(170, 120, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditBEllipse.setFont(font)
        self.spinEditBEllipse.setMinimum(0)
        self.spinEditBEllipse.setMaximum(1000)
        self.spinEditBEllipse.setObjectName("spinEditBEllipse")

        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")

        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(12, 210, 221, 91))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")

        self.spinEditRedEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditRedEllipse.setGeometry(QtCore.QRect(10, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditRedEllipse.setFont(font)
        self.spinEditRedEllipse.setMinimum(0)
        self.spinEditRedEllipse.setMaximum(255)
        self.spinEditRedEllipse.setObjectName("spinEditRedEllipse")

        self.spinEditGreenEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditGreenEllipse.setGeometry(QtCore.QRect(80, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditGreenEllipse.setFont(font)
        self.spinEditGreenEllipse.setMinimum(0)
        self.spinEditGreenEllipse.setMaximum(255)
        self.spinEditGreenEllipse.setObjectName("spinEditGreenEllipse")

        self.spinEditBlueEllipse = QtWidgets.QSpinBox(self.groupBox)
        self.spinEditBlueEllipse.setGeometry(QtCore.QRect(150, 50, 60, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditBlueEllipse.setFont(font)
        self.spinEditBlueEllipse.setMinimum(0)
        self.spinEditBlueEllipse.setMaximum(255)
        self.spinEditBlueEllipse.setObjectName("spinEditBlueEllipse")

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

        self.comboEllipseName = QtWidgets.QComboBox(self.centralwidget)
        self.comboEllipseName.setGeometry(QtCore.QRect(60, 30, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboEllipseName.setFont(font)
        self.comboEllipseName.setObjectName("comboEllipseName")
        self.comboEllipseName.currentIndexChanged.connect(self.comboEllipseNameIndexChanged)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 170, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")

        self.spinEditEllipseThickness = QtWidgets.QSpinBox(self.centralwidget)
        self.spinEditEllipseThickness.setGeometry(QtCore.QRect(160, 170, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinEditEllipseThickness.setFont(font)
        self.spinEditEllipseThickness.setMinimum(1)
        self.spinEditEllipseThickness.setMaximum(5)
        self.spinEditEllipseThickness.setObjectName("spinEditEllipseThickness")

        self.btnEditOkEllipse.raise_()
        self.label_2.raise_()
        self.label.raise_()
        self.spinEditXEllipse.raise_()
        self.spinEditYEllipse.raise_()
        self.label_3.raise_()
        self.spinEditAEllipse.raise_()
        self.label_4.raise_()
        self.spinEditBEllipse.raise_()
        self.label_5.raise_()
        self.groupBox.raise_()
        self.comboEllipseName.raise_()
        self.label_9.raise_()
        self.spinEditEllipseThickness.raise_()
        
        EditEllipse.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditEllipse)
        QtCore.QMetaObject.connectSlotsByName(EditEllipse)

    def comboEllipseNameIndexChanged(self):
        self.signalComboEllipseNameIndexChanged.emit(self.comboEllipseName.currentIndex())

    def btnOkEditEllipseClicked(self):
        self.signalBtnOkEditEllipseClicked.emit(self.comboEllipseName.currentIndex(), self.spinEditXEllipse.value(), self.spinEditYEllipse.value(), self.spinEditAEllipse.value(), self.spinEditBEllipse.value(), self.spinEditEllipseThickness.value(), self.spinEditRedEllipse.value(), self.spinEditGreenEllipse.value(), self.spinEditBlueEllipse.value())
   
    def retranslateUi(self, EditEllipse):
        _translate = QtCore.QCoreApplication.translate
        EditEllipse.setWindowTitle(_translate("EditEllipse", "Edit Ellipse"))
        self.btnEditOkEllipse.setText(_translate("EditEllipse", "OK"))
        self.label_2.setText(_translate("EditEllipse", "Y : "))
        self.spinEditYEllipse.setToolTip(_translate("EditEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinEditXEllipse.setToolTip(_translate("EditEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.label.setText(_translate("EditEllipse", "X : "))
        self.label_3.setText(_translate("EditEllipse", "B : "))
        self.spinEditAEllipse.setToolTip(_translate("EditEllipse", "Set radius A for ellipse (in pixels)"))
        self.label_4.setText(_translate("EditEllipse", "A : "))
        self.spinEditBEllipse.setToolTip(_translate("EditEllipse", "Set radius B for ellipse (in pixels)"))
        self.label_5.setText(_translate("EditEllipse", "Select Ellipse"))
        self.groupBox.setTitle(_translate("EditEllipse", "Color"))
        self.spinEditRedEllipse.setToolTip(_translate("EditEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinEditGreenEllipse.setToolTip(_translate("EditEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.spinEditBlueEllipse.setToolTip(_translate("EditEllipse", "Set X for ellipse\'s center (in pixels)"))
        self.label_6.setText(_translate("EditEllipse", "Red"))
        self.label_7.setText(_translate("EditEllipse", "Green"))
        self.label_8.setText(_translate("EditEllipse", "Blue"))
        self.label_9.setText(_translate("EditEllipse", "Thickness : "))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EditEllipse = QtWidgets.QMainWindow()
    ui = Ui_EditEllipse()
    ui.setupUi(EditEllipse)
    EditEllipse.show()
    sys.exit(app.exec_())
