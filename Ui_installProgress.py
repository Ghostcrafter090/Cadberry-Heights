from PyQt5 import QtCore, QtGui, QtWidgets
import os
import time
import threading

def installerCheck():
    while True:
        if checkInstall() == 0:
            print("close")
            exit(0)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 107)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(52, 14, 14, 255), stop:1 rgba(0, 0, 40, 255));")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 0, 371, 61))
        self.label.setStyleSheet("font: 8pt \"Onyx\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(170, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 75, 371, 21))
        self.label_2.setStyleSheet("font: 8pt \"OCR A Extended\";\n"
"background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(170, 0, 0);")
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Cadberry Heights Launcher (Installing Resources...)"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:36pt; font-weight:600;\">Cadberry Heights Launcher</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:9pt; font-weight:600;\">Installing Resources... (This may take a bit).</span></p></body></html>"))

def checkInstall():
    err = 0
    temp = os.environ['appdata']
    if os.path.isfile(temp + "\\.cadberryheights\\installede.derp") != True:
        err = 1
    return err

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    lc = threading.Lock()
    installerRun = threading.Thread(target=app.exec_())
    commandsRun = threading.Thread(target=installerCheck)
    installerRun.start()
    commandsRun.start()
    print("From Main")
    installerRun.join()
    commandsRun.join()
    Dialog.close()