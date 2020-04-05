# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog

class Ui_Login(QtWidgets.QMainWindow):
    
    signalNew = QtCore.pyqtSignal()
    signalLoad = QtCore.pyqtSignal(str)
    
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(400, 201)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 30, 280, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.btnNew = QtWidgets.QPushButton(self.centralwidget)
        self.btnNew.setGeometry(QtCore.QRect(66, 130, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnNew.setFont(font)
        self.btnNew.setObjectName("btnNew")
        self.btnNew.clicked.connect(self.btnNewClicked)

        self.btnLoad = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoad.setGeometry(QtCore.QRect(233, 130, 100, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.btnLoad.setFont(font)
        self.btnLoad.setObjectName("btnLoad")
        self.btnLoad.clicked.connect(self.btnLoadClicked)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def btnNewClicked(self):
        self.signalNew.emit()

    def btnLoadClicked(self):
        self.loadDialog = QFileDialog.Options()
        self.loadDialog = QFileDialog.DontUseNativeDialog
        loadFIlePath = QFileDialog.getOpenFileName(self, "Load Data", "/", "Text File (*.txt)", options = self.loadDialog)
        if loadFIlePath != ('', ''):
            self.signalLoad.emit(loadFIlePath[0])

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Create new or load?"))
        self.btnNew.setText(_translate("Login", "New"))
        self.btnLoad.setText(_translate("Login", "Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
