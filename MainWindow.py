# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog


class Ui_MainWindow(QtWidgets.QMainWindow):

    signalAddCircle = QtCore.pyqtSignal()
    signalAddEllipse = QtCore.pyqtSignal()
    signalDeleteCircle = QtCore.pyqtSignal()
    signalDeleteEllipse = QtCore.pyqtSignal()
    signalEditCircle = QtCore.pyqtSignal()
    signalEditEllipse = QtCore.pyqtSignal()
    signalClearScreen = QtCore.pyqtSignal()
    signalSave = QtCore.pyqtSignal(str)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1300, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.lblScreen = QtWidgets.QLabel(self.centralwidget)
        self.lblScreen.setGeometry(QtCore.QRect(10, 10, 1280, 720))
        self.lblScreen.setFrameShape(QtWidgets.QFrame.Box)
        self.lblScreen.setObjectName("lblScreen")

        self.canvas = QtGui.QPixmap(1280, 720)
        self.lblScreen.setPixmap(self.canvas)
        self.painter = QtGui.QPainter(self.lblScreen.pixmap())
        self.pen = QtGui.QPen()

        self.btnAddCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddCircle.setGeometry(QtCore.QRect(20, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnAddCircle.setFont(font)
        self.btnAddCircle.setObjectName("btnAddCircle")
        self.btnAddCircle.clicked.connect(self.btnAddCircleClicked)

        self.btnAddEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnAddEllipse.setGeometry(QtCore.QRect(170, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.btnAddEllipse.setFont(font)
        self.btnAddEllipse.setObjectName("btnAddEllipse")
        self.btnAddEllipse.clicked.connect(self.btnAddEllipseClicked)

        self.btnDeleteCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteCircle.setGeometry(QtCore.QRect(320, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnDeleteCircle.setFont(font)
        self.btnDeleteCircle.setObjectName("btnDeleteCircle")
        self.btnDeleteCircle.clicked.connect(self.btnDeleteCircleClicked)

        self.btnDeleteEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnDeleteEllipse.setGeometry(QtCore.QRect(470, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnDeleteEllipse.setFont(font)
        self.btnDeleteEllipse.setObjectName("btnDeleteEllipse")
        self.btnDeleteEllipse.clicked.connect(self.btnDeleteEllipseClicked)

        self.btnClearScreen = QtWidgets.QPushButton(self.centralwidget)
        self.btnClearScreen.setGeometry(QtCore.QRect(1180, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnClearScreen.setFont(font)
        self.btnClearScreen.setObjectName("btnClearScreen")
        self.btnClearScreen.clicked.connect(self.btnClearScreenClicked)

        self.btnSave = QtWidgets.QPushButton(self.centralwidget)
        self.btnSave.setGeometry(QtCore.QRect(1030, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnSave.setFont(font)
        self.btnSave.setObjectName("btnSave")
        self.btnSave.clicked.connect(self.btnSaveClicked)

        self.btnEditCircle = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditCircle.setGeometry(QtCore.QRect(620, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnEditCircle.setFont(font)
        self.btnEditCircle.setObjectName("btnEditCircle")
        self.btnEditCircle.clicked.connect(self.btnEditCircleClicked)

        self.btnEditEllipse = QtWidgets.QPushButton(self.centralwidget)
        self.btnEditEllipse.setGeometry(QtCore.QRect(770, 740, 100, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.btnEditEllipse.setFont(font)
        self.btnEditEllipse.setObjectName("btnEditEllipse")
        self.btnEditEllipse.clicked.connect(self.btnEditEllipseClicked)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btnAddCircleClicked(self):
        self.signalAddCircle.emit()

    def btnAddEllipseClicked(self):
        self.signalAddEllipse.emit()

    def btnDeleteCircleClicked(self):
        self.signalDeleteCircle.emit()

    def btnDeleteEllipseClicked(self):
        self.signalDeleteEllipse.emit()

    def btnEditCircleClicked(self):
        self.signalEditCircle.emit()

    def btnEditEllipseClicked(self):
        self.signalEditEllipse.emit()

    def btnClearScreenClicked(self):
        self.signalClearScreen.emit()

    def createCircle(self, xCenter, yCenter, radius, width, red, green, blue):
        self.pen.setColor(QtGui.QColor(red, green, blue))
        self.pen.setWidth(width)
        self.painter.setPen(self.pen)
        x = 0
        y = radius
        d = 1 - radius

        while x <= y:
            self.painter.drawPoint(x + xCenter, y + yCenter)
            self.painter.drawPoint(y + xCenter, x + yCenter)
            self.painter.drawPoint(-x + xCenter, -y + yCenter)
            self.painter.drawPoint(-y + xCenter, -x + yCenter)
            self.painter.drawPoint(-x + xCenter, y + yCenter)
            self.painter.drawPoint(x + xCenter, -y + yCenter)
            self.painter.drawPoint(-y + xCenter, x + yCenter)
            self.painter.drawPoint(y + xCenter, -x + yCenter)
            if d < 0:
                d = d + 2 * x + 3
            else:
                d = d + 2 * (x - y) + 5
                y = y - 1
            x = x + 1

    def createEllipse(self, xCenter, yCenter, alpha, beta, width, red, green, blue):
        self.pen.setColor(QtGui.QColor(red, green, blue))
        self.pen.setWidth(width)
        self.painter.setPen(self.pen)
        x = 0
        y = beta
        d = 4 * pow(beta, 2) - 4 * pow(alpha, 2) * beta + pow(alpha, 2)

        while 2 * pow(beta, 2) * (x + 1) <= pow(alpha, 2) * (2 * y - 1):
            self.painter.drawPoint(x + xCenter, y + yCenter)
            self.painter.drawPoint(-x + xCenter, -y + yCenter)
            self.painter.drawPoint(-x + xCenter, y + yCenter)
            self.painter.drawPoint(x + xCenter, -y + yCenter)
            if d > 0 :
                y = y - 1
                d = d + pow(beta, 2) * (8 * x + 12) + pow(alpha, 2) * (8 - 8 * y)
            else:
                d = d + pow(beta, 2) * (8 * x + 12)
            x = x + 1

        d = pow(beta, 2) * pow((2 * x + 1), 2) + 4 * pow(alpha, 2) * pow((y - 1), 2) - 4 * pow(alpha, 2) * pow(beta , 2)
        while y > 0:
            self.painter.drawPoint(x + xCenter, y + yCenter)
            self.painter.drawPoint(-x + xCenter, -y + yCenter)
            self.painter.drawPoint(-x + xCenter, y + yCenter)
            self.painter.drawPoint(x + xCenter, -y + yCenter)
            if d < 0:
                x = x + 1
                d = d + pow(beta, 2) * (8 * x + 8) + pow(alpha, 2) * (12 - 8 * y)
            else:
                d = d + pow(alpha, 2) * (12 -  8 * y)
            y = y - 1
            self.painter.drawPoint(x + xCenter, y + yCenter)
            self.painter.drawPoint(-x + xCenter, -y + yCenter)
            self.painter.drawPoint(-x + xCenter, y + yCenter)
            self.painter.drawPoint(x + xCenter, -y + yCenter)

    def btnSaveClicked(self):
        self.saveDialog = QFileDialog.Options()
        self.saveDialog = QFileDialog.DontUseNativeDialog
        newFilePath = QFileDialog.getSaveFileName(self, "Save Data", "/", "Text File (*.txt)", options = self.saveDialog)
        if newFilePath != ('', ''):
            self.signalSave.emit(newFilePath[0])

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Main Window"))
        self.btnAddCircle.setText(_translate("MainWindow", "Add Circle"))
        self.btnAddEllipse.setText(_translate("MainWindow", "Add Ellipse"))
        self.btnDeleteCircle.setText(_translate("MainWindow", "Delete Circle"))
        self.btnDeleteEllipse.setText(_translate("MainWindow", "Delete Ellipse"))
        self.btnClearScreen.setText(_translate("MainWindow", "Clear Screen"))
        self.btnSave.setText(_translate("MainWindow", "Save"))
        self.btnEditCircle.setText(_translate("MainWindow", "Edit Circle"))
        self.btnEditEllipse.setText(_translate("MainWindow", "Edit Ellipse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
