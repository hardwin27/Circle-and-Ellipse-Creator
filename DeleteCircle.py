# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deletecircle.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteCircle(QtWidgets.QMainWindow):

    signal = QtCore.pyqtSignal(int)

    def setupUi(self, DeleteCircle):
        DeleteCircle.setObjectName("DeleteCircle")
        DeleteCircle.resize(170, 170)
        self.centralwidget = QtWidgets.QWidget(DeleteCircle)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 60, 87, 32))
        self.comboBox.setObjectName("comboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 87, 32))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.btnOkCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnOkCircle.setGeometry(QtCore.QRect(40, 110, 88, 34))
        self.btnOkCircle.setObjectName("btnOkCircle")
        self.btnOkCircle.clicked.connect(self.btnOkCircleClicked)
        DeleteCircle.setCentralWidget(self.centralwidget)

        self.retranslateUi(DeleteCircle)
        QtCore.QMetaObject.connectSlotsByName(DeleteCircle)

    def retranslateUi(self, DeleteCircle):
        _translate = QtCore.QCoreApplication.translate
        DeleteCircle.setWindowTitle(_translate("DeleteCircle", "Delete Circle"))
        self.label.setText(_translate("DeleteCircle", "Select Circle"))
        self.btnOkCircle.setText(_translate("DeleteCircle", "OK"))

    def btnOkCircleClicked(self):
        self.signal.emit(self.comboBox.currentIndex())
        self.comboBox.clear()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DeleteCircle = QtWidgets.QMainWindow()
    ui = Ui_DeleteCircle()
    ui.setupUi(DeleteCircle)
    DeleteCircle.show()
    sys.exit(app.exec_())
