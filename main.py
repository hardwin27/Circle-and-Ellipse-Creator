from PyQt5 import QtCore, QtWidgets, QtGui
from Login import Ui_Login
from MainWindow import Ui_MainWindow
from AddCircle import Ui_AddCircle
from AddEllipse import Ui_AddEllipse
from DeleteCircle import Ui_DeleteCircle
from DeleteEllipse import Ui_DeleteEllipse
from EditCircle import Ui_EditCircle
from EditEllipse import Ui_EditEllipse
import sys
import os

class Circle:
    def __init__(self, x, y, r, width, red, green, blue, name):
        self.xCenter = x
        self.yCenter = y
        self.radius = r
        self.width = width
        self.red = red
        self.green = green
        self.blue = blue
        self.name = name

class Ellipse:
    def __init__(self, x, y, a, b, width, red, green, blue, name):
        self.xCenter = x
        self.yCenter = y
        self.alpha = a
        self.beta = b
        self.width = width
        self.red = red
        self.green = green
        self.blue = blue
        self.name = name
    
class Control:

    def __init__(self, listCircle, listEllipse):
        self.listCircle = listCircle
        self.listEllipse = listEllipse

        self.loginWindow = QtWidgets.QMainWindow()
        self.loginUi = Ui_Login()
        self.loginUi.setupUi(self.loginWindow)
        self.loginUi.signalNew.connect(self.showMainWindow)
        self.loginUi.signalLoad.connect(self.loadFile)
        
        self.mainWindow = QtWidgets.QMainWindow()
        self.mainWindowUi = Ui_MainWindow()
        self.mainWindowUi.setupUi(self.mainWindow)
        self.mainWindowUi.signalAddCircle.connect(self.showAddCircle)
        self.mainWindowUi.signalAddEllipse.connect(self.showAddEllipse)
        self.mainWindowUi.signalDeleteCircle.connect(self.showDeleteCircle)
        self.mainWindowUi.signalDeleteEllipse.connect(self.showDeleteEllipse)
        self.mainWindowUi.signalEditCircle.connect(self.showEditCircle)
        self.mainWindowUi.signalEditEllipse.connect(self.showEditEllipse)
        self.mainWindowUi.signalClearScreen.connect(self.clearScreen)
        self.mainWindowUi.signalSave.connect(self.saveFile)

        self.addCircleWindow = QtWidgets.QMainWindow()
        self.addCircleUi = Ui_AddCircle()
        self.addCircleUi.setupUi(self.addCircleWindow)
        self.addCircleUi.signal.connect(self.addCircleToList)

        self.addEllipseWindow = QtWidgets.QMainWindow()
        self.addEllipseUi = Ui_AddEllipse()
        self.addEllipseUi.setupUi(self.addEllipseWindow)
        self.addEllipseUi.signal.connect(self.addEllipseToList)

        self.deleteCircleWindow = QtWidgets.QMainWindow()
        self.deleteCircleUi = Ui_DeleteCircle()
        self.deleteCircleUi.setupUi(self.deleteCircleWindow)
        self.deleteCircleUi.signal.connect(self.deleteCircleFromList)

        self.deleteEllipseWindow = QtWidgets.QMainWindow()
        self.deleteEllipseUi = Ui_DeleteEllipse()
        self.deleteEllipseUi.setupUi(self.deleteEllipseWindow)
        self.deleteEllipseUi.signal.connect(self.deleteEllipseFromList)

        self.editCircleWindow = QtWidgets.QMainWindow()
        self.editCircleUi = Ui_EditCircle()
        self.editCircleUi.setupUi(self.editCircleWindow)
        self.editCircleUi.signalComboCircleNameIndexChanged.connect(self.comboBoxCircleChanged)
        self.editCircleUi.signalBtnOkEditCircleClicked.connect(self.editCircleFromList)
        
        self.editEllipseWindow = QtWidgets.QMainWindow()
        self.editEllipseUi = Ui_EditEllipse()
        self.editEllipseUi.setupUi(self.editEllipseWindow)
        self.editEllipseUi.signalComboEllipseNameIndexChanged.connect(self.comboBoxEllipseChanged)
        self.editEllipseUi.signalBtnOkEditEllipseClicked.connect(self.editEllipseFromList)
        
        self.errorMessage = QtWidgets.QErrorMessage()
    
    def showMainWindow(self):
        listCircleLength = len(self.listCircle)
        listEllipseLength = len(self.listEllipse)
        self.mainWindowUi.painter.fillRect(0, 0, 1280, 720, QtGui.QColor(0, 0, 0))
        for index in range(listCircleLength):
            self.mainWindowUi.createCircle(int(self.listCircle[index].xCenter), int(self.listCircle[index].yCenter), int(self.listCircle[index].radius), int(self.listCircle[index].width), int(self.listCircle[index].red), int(self.listCircle[index].green), int(self.listCircle[index].blue))
        for index in range(listEllipseLength):
            self.mainWindowUi.createEllipse(int(self.listEllipse[index].xCenter), int(self.listEllipse[index].yCenter), int(self.listEllipse[index].alpha), int(self.listEllipse[index].beta), int(self.listEllipse[index].width), int(self.listEllipse[index].red), int(self.listEllipse[index].green), int(self.listEllipse[index].blue))
        if self.mainWindow.isVisible() == False:
            self.mainWindow.show()
        self.loginWindow.hide()
        self.addCircleWindow.hide()
        self.addEllipseWindow.hide()
        self.deleteCircleWindow.hide()
        self.deleteEllipseWindow.hide()
        self.editCircleWindow.hide()
        self.editEllipseWindow.hide()

    def addCircleToList(self, newX, newY, newRad, newWidth, newRed, newGreen, newBlue, newName):
        if newName == "":
            self.errorMessage.showMessage("Error. Name cannot be null")
        else:
            newName = newName.replace(" ", "")
            temp = Circle(newX, newY, newRad, newWidth, newRed, newGreen, newBlue, newName)
            self.listCircle.append(temp)
            self.showMainWindow()

    def addEllipseToList(self, newX, newY, newA, newB, newWidth, newRed, newGreen, newBlue, newName):
        if newName == "":
            self.errorMessage.showMessage("Error. Name cannot be null")
        else:
            newName = newName.replace(" ", "")
            temp = Ellipse(newX, newY, newA, newB, newWidth, newRed, newGreen, newBlue, newName)
            self.listEllipse.append(temp)
            self.showMainWindow()

    def deleteCircleFromList(self, removedIndex):
        if removedIndex != -1:
            del self.listCircle[removedIndex]
        self.showMainWindow()

    def deleteEllipseFromList(self, removedIndex):
        if removedIndex != -1:
            del self.listEllipse[removedIndex]
        self.showMainWindow()

    def editCircleFromList(self, index, newX, newY, newRad, newWidth, newRed, newGreen, newBlue):
        if index >= 0:
            listCircle[index].xCenter = newX
            listCircle[index].yCenter = newY
            listCircle[index].radius = newRad
            listCircle[index].width = newWidth
            listCircle[index].red = newRed
            listCircle[index].green = newGreen
            listCircle[index].blue = newBlue
        self.showMainWindow()

    def editEllipseFromList(self, index, newX, newY, newAlpha, newBeta, newWidth, newRed, newGreen, newBlue):
        if index >= 0:
            listEllipse[index].xCenter = newX
            listEllipse[index].yCenter = newY
            listEllipse[index].alpha = newAlpha
            listEllipse[index].beta = newBeta
            listEllipse[index].width = newWidth
            listEllipse[index].red = newRed
            listEllipse[index].green = newGreen
            listEllipse[index].blue = newBlue
        self.showMainWindow()
    
    def showAddCircle(self):
        self.addCircleWindow.show()

    def showAddEllipse(self):
        self.addEllipseWindow.show()

    def showDeleteCircle(self):
        listCircleLength = len(self.listCircle)
        self.deleteCircleUi.comboBox.clear()
        for index in range(listCircleLength):
            self.deleteCircleUi.comboBox.addItem(self.listCircle[index].name)
        
        self.deleteCircleWindow.show()

    def showDeleteEllipse(self):
        listEllipseLength = len(self.listEllipse)
        self.deleteEllipseUi.comboBox.clear()
        for index in range(listEllipseLength):
            self.deleteEllipseUi.comboBox.addItem(self.listEllipse[index].name)
        
        self.deleteEllipseWindow.show()

    def showEditCircle(self):
        listCircleLength = len(self.listCircle)
        self.editCircleUi.comboCircleName.clear()
        for index in range(listCircleLength):
            self.editCircleUi.comboCircleName.addItem(self.listCircle[index].name)

        self.editCircleWindow.show()

    def showEditEllipse(self):
        listEllipseLength = len(self.listEllipse)
        self.editEllipseUi.comboEllipseName.clear()
        for index in range(listEllipseLength):
            self.editEllipseUi.comboEllipseName.addItem(self.listEllipse[index].name)

        self.editEllipseWindow.show()

    def comboBoxCircleChanged(self, index):
        if index >= 0:
            self.editCircleUi.spinEditXCircle.setValue(int(self.listCircle[index].xCenter))
            self.editCircleUi.spinEditYCircle.setValue(int(self.listCircle[index].yCenter))
            self.editCircleUi.spinEditRCircle.setValue(int(self.listCircle[index].radius))
            self.editCircleUi.spinEditCircleThickness.setValue(int(self.listCircle[index].width))
            self.editCircleUi.spinEditRedCircle.setValue(int(self.listCircle[index].red))
            self.editCircleUi.spinEditGreenCircle.setValue(int(self.listCircle[index].green))
            self.editCircleUi.spinEditBlueCircle.setValue(int(self.listCircle[index].blue))

    def comboBoxEllipseChanged(self, index):
        if index >= 0:
            self.editEllipseUi.spinEditXEllipse.setValue(int(self.listEllipse[index].xCenter))
            self.editEllipseUi.spinEditYEllipse.setValue(int(self.listEllipse[index].yCenter))
            self.editEllipseUi.spinEditAEllipse.setValue(int(self.listEllipse[index].alpha))
            self.editEllipseUi.spinEditBEllipse.setValue(int(self.listEllipse[index].beta))
            self.editEllipseUi.spinEditEllipseThickness.setValue(int(self.listEllipse[index].width))
            self.editEllipseUi.spinEditRedEllipse.setValue(int(self.listEllipse[index].red))
            self.editEllipseUi.spinEditGreenEllipse.setValue(int(self.listEllipse[index].green))
            self.editEllipseUi.spinEditBlueEllipse.setValue(int(self.listEllipse[index].blue))
    
    def saveFile(self, saveFilePath):
        newFile = open(saveFilePath + ".txt", "w")
        listCircleLength = len(self.listCircle)
        listEllipseLength = len(self.listEllipse)
        newFile.write(str(listCircleLength) + "\n")
        for index in range(listCircleLength):
            newFile.write(str(self.listCircle[index].xCenter) + " " + str(self.listCircle[index].yCenter) + " " + str(self.listCircle[index].radius) + " " + str(self.listCircle[index].width) + " " + str(self.listCircle[index].red) + " " + str(self.listCircle[index].green) + " " + str(self.listCircle[index].blue) + " " + self.listCircle[index].name + os.linesep)
        newFile.write(str(listEllipseLength) + "\n")
        for index in range(listEllipseLength):
            newFile.write(str(self.listEllipse[index].xCenter) + " " + str(self.listEllipse[index].yCenter) + " " + str(self.listEllipse[index].alpha) + " " + str(self.listEllipse[index].beta) + " " + str(self.listEllipse[index].width) + " " + str(self.listEllipse[index].red) + " " + str(self.listEllipse[index].green) + " " + str(self.listEllipse[index].blue) + " " + self.listEllipse[index].name + os.linesep)
        newFile.close()

    def loadFile(self, loadFilePath):
        loadFile = open(loadFilePath, "r")
        listCircleLength = int(loadFile.readline())
        for index in range(listCircleLength):
            data = loadFile.readline()
            data = data.split(" ")
            tempCircle = Circle(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7].replace("\n", ""))
            self.listCircle.append(tempCircle)
            temp = loadFile.readline()
        listEllipseLength = int(loadFile.readline())
        for index in range(listEllipseLength):
            data = loadFile.readline()
            data = data.split(" ")
            tempEllipse = Ellipse(data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8].replace("\n", ""))
            self.listEllipse.append(tempEllipse)
            temp = loadFile.readline()

        self.showMainWindow()

    def clearScreen(self):
        self.listCircle.clear()
        self.listEllipse.clear()
        self.mainWindow.hide()
        self.showMainWindow()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    listCircle = []
    listEllipse = []
    controller = Control(listCircle, listEllipse)
    controller.loginWindow.show()
    sys.exit(app.exec_())