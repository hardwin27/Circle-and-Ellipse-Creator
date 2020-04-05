# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteellipse.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteEllipse(QtWidgets.QMainWindow):

    signal = QtCore.pyqtSignal(int)

    def setupUi(self, DeleteEllipse):
        DeleteEllipse.setObjectName("DeleteEllipse")
        DeleteEllipse.resize(170, 170)
        self.centralwidget = QtWidgets.QWidget(DeleteEllipse)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 87, 32))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnOkEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkEllipse.setGeometry(QtCore.QRect(40, 110, 88, 34))
        self.btnOkEllipse.setObjectName("btnOkEllipse")
        self.btnOkEllipse.clicked.connect(self.btnOkEllipseClicked)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 87, 32))
        self.comboBox.setObjectName("comboBox")
        DeleteEllipse.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeleteEllipse)
        QtCore.QMetaObject.connectSlotsByName(DeleteEllipse)

    def btnOkEllipseClicked(self):
        self.signal.emit(self.comboBox.currentIndex())
        self.comboBox.clear()

    def retranslateUi(self, DeleteEllipse):
        _translate = QtCore.QCoreApplication.translate
        DeleteEllipse.setWindowTitle(_translate("DeleteEllipse", "Delete Ellipse"))
        self.label.setText(_translate("DeleteEllipse", "Select Ellipse"))
        self.btnOkEllipse.setText(_translate("DeleteEllipse", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteEllipse = QtWidgets.QMainWindow()
    ui = Ui_DeleteEllipse()
    ui.setupUi(DeleteEllipse)
    DeleteEllipse.show()
    sys.exit(app.exec_())
