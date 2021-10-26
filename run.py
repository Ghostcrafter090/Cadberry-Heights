import os
import subprocess
import sys
import requests
import zipfile
import threading
import time

from PyQt5 import QtCore, QtGui, QtWidgets

# Used for deliberatly throwing errors and the like
def nullWorker(nulln):
    return nulln

class fileIO:
    def getFile(path):
        error = 0
        try:
            file = open(path, "r")
            jsonData = file.read()
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        if error != 0:
            jsonData = error
        return jsonData

    def saveFile(path, jsonData):
        error = 0
        try:
            file = open(path, "w")
            file.write(jsonData)
            file.close()
        except:
            print("Unexpected error:", sys.exc_info())
            error = 1
        return error

class Server:
    def startServer():
        os.remove(".\\server-source\\logs\\latest.log")
        os.system("start /min "" .\\runServer.bat")
        n = 0
        while n == 0:
            latestLog = str(fileIO.getFile(".\\server-source\\logs\\latest.log"))
            if latestLog.find("[Server thread/INFO]: Done") != -1:
                n = 1

    def startGame(micCheck, login, password):
        err = 0
        if micCheck != True:
            try:
                temp = os.environ['appdata']
                subprocess.check_output(temp + "\\.cadberryheights\\game_launcher.exe --main-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\\install\" --work-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\" start forge-36.0.13 --login " + login + " --password " + password)
            except:
                err = 1
        else:
            if micCheck != True:
                try:
                    temp = os.environ['appdata']
                    subprocess.check_output(temp + "\\.cadberryheights\\game_launcher.exe --main-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\\install\" --work-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\" start forge-36.0.13 -m --login " + login + " --password " + password)
                except:
                    err = 1
        return err

    def closeServer():
        os.system("taskkill /f /im cadberry-server.exe")

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(399, 427)
        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(235, 61, 61, 255), stop:1 rgba(0, 0, 40, 255));")
        self.launchButton = QtWidgets.QPushButton(Dialog)
        self.launchButton.setGeometry(QtCore.QRect(10, 390, 75, 23))
        self.launchButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(203, 235, 61, 255), stop:1 rgba(0, 130, 40, 255));")
        self.launchButton.setInputMethodHints(QtCore.Qt.ImhNone)
        self.launchButton.setObjectName("launchButton")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 20, 381, 231))
        self.widget.setStyleSheet("image: url(gui/Cadberry_Heights_Title.png);")
        self.widget.setObjectName("widget")
        self.Title = QtWidgets.QLabel(Dialog)
        self.Title.setGeometry(QtCore.QRect(10, 0, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Onyx")
        self.Title.setFont(font)
        self.Title.setStyleSheet("background-color: rgba(0, 0, 0, 0);")
        self.Title.setObjectName("Title")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(300, 390, 75, 23))
        self.exitButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(203, 235, 61, 255), stop:1 rgba(0, 130, 40, 255));")
        self.exitButton.setObjectName("exitButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 260, 231, 20))
        self.lineEdit.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(164, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 310, 231, 20))
        self.lineEdit_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(164, 170, 127, 255), stop:1 rgba(255, 255, 255, 255));\n"
"color: rgb(0, 0, 0);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(-10, 260, 91, 16))
        self.label.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(0, 310, 81, 20))
        self.label_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_2.setObjectName("label_2")
        self.microsoftCheck = QtWidgets.QCheckBox(Dialog)
        self.microsoftCheck.setGeometry(QtCore.QRect(20, 350, 151, 21))
        self.microsoftCheck.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.microsoftCheck.setObjectName("microsoftCheck")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 350, 221, 21))
        self.label_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.label_3.setObjectName("label_3")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(150, 390, 81, 23))
        self.loginButton.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(203, 235, 61, 255), stop:1 rgba(0, 130, 40, 255));")
        self.loginButton.setObjectName("loginButton")
        self.checkEmail = QtWidgets.QWidget(Dialog)
        self.checkEmail.setGeometry(QtCore.QRect(340, 260, 21, 21))
        self.checkEmail.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(gui/dash.png);")
        self.checkEmail.setObjectName("checkEmail")
        self.checkPassword = QtWidgets.QWidget(Dialog)
        self.checkPassword.setGeometry(QtCore.QRect(340, 310, 21, 21))
        self.checkPassword.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"image: url(gui/dash.png);")
        self.checkPassword.setObjectName("checkPassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.launchButton.setText(_translate("Dialog", "Launch Game"))
        self.Title.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:18pt; color: red;\">Cadberry Heights Launcher</span></p></body></html>"))
        self.exitButton.setText(_translate("Dialog", "Exit"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Email:</span></p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"right\"><span style=\" font-size:12pt;\">Password:</span></p></body></html>"))
        self.microsoftCheck.setText(_translate("Dialog", "Microsoft Account"))
        self.label_3.setText(_translate("Dialog", "< Check this if you have a microsoft account!"))
        self.loginButton.setText(_translate("Dialog", "Check Login"))

    def launchSys(self):
        micCheck = self.microsoftCheck.isChecked()
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if self.checkLogin() == 0:
            Server.startGame(micCheck, login, password)
            Server.closeServer()

    def checkLogin(self):
        micCheck = self.microsoftCheck.isChecked()
        login = self.lineEdit.text()
        password = self.lineEdit_2.text()
        print(login)
        err = 0
        if micCheck != 1:
            try:
                temp = os.environ['appdata']
                subprocess.check_output(temp + "\\.cadberryheights\\game_launcher.exe --main-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\\install\" --work-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\" login " + login + " " + password)
            except Exception as erro:
                print(erro)
                err = 1
        else:
            try:
                temp = os.environ['appdata']
                subprocess.check_output(temp + "\\.cadberryheights\\game_launcher.exe --main-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\\install\" --work-dir \"" + temp + "\\.cadberryheights\\.cadberryheights\" login -m " + login + " " + password)
            except Exception as erro:
                print(erro)
                err = 1
        print(err)
        if err != 1:
            self.checkPassword.setStyleSheet("background-color: rgba(255, 255, 255, 0);\nimage: url(gui/check.png);")
            self.checkEmail.setStyleSheet("background-color: rgba(255, 255, 255, 0);\nimage: url(gui/check.png);")
        else:
            self.checkPassword.setStyleSheet("background-color: rgba(255, 255, 255, 0);\nimage: url(gui/ex.png);")
            self.checkEmail.setStyleSheet("background-color: rgba(255, 255, 255, 0);\nimage: url(gui/ex.png);")
        return err
    
    def exitN(nulln, nullf):
        nullWorker([nulln, nullf])
        exit(0)

    def connectSignalsSlots(self):
        self.launchButton.clicked.connect(self.launchSys)
        self.loginButton.clicked.connect(self.checkLogin)
        self.exitButton.clicked.connect(self.exitN)

def mainn():
    if __name__ == "__main__":
        import sys
        app = QtWidgets.QApplication(sys.argv)
        Dialog = QtWidgets.QDialog()
        ui = Ui_Dialog()
        ui.setupUi(Dialog)
        ui.connectSignalsSlots()
        Dialog.show()
        sys.exit(app.exec_())

class installer:
    def install():
        lc = threading.Lock()
        window = threading.Thread(target=installer.displayWindow)
        commands = threading.Thread(target=installer.runInstall)
        window.start()
        commands.start()
        print("From Main")
        window.join()
        commands.join()

    def runInstall():
        print("Installing...")
        temp = os.environ['appdata']
        installer.download("https://ourcloud.nspes.ca/index.php/s/PJooyrWPS8eyfXr/download", temp + "\\.cadberryheights\\game_launcher.zip", 5916635)
        installer.download("https://ourcloud.nspes.ca/index.php/s/qf4e7GSwqKpio2S/download", temp + "\\.cadberryheights\\.cadberryheights.zip", 960133185)
        installer.download("https://ourcloud.nspes.ca/index.php/s/rtom7zFzY75ym3R/download", temp + "\\.cadberryheights\\lib.zip", 322793643)
        installer.unpack(temp + "\\.cadberryheights\\.cadberryheights.zip", temp + "\\.cadberryheights")
        installer.unpack(temp + "\\.cadberryheights\\lib.zip", temp + "\\.cadberryheights\\.cadberryheights\\install")
        installer.unpack(temp + "\\.cadberryheights\\game_launcher.zip", temp + "\\.cadberryheights")
        fileIO.saveFile(temp + "\\.cadberryheights\\installed.derp", "1")
        print("Installed.")
        print("Checking for updates...")
        updater.checkUpdates()
        return 0
    
    def download(urlf, path, maxB):
        i = 0
        n = 0
        local_filename = path
        # NOTE the stream=True parameter below
        with requests.get(urlf, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192): 
                    # If you have chunk encoded response uncomment if
                    # and set chunk_size parameter to None.
                    #if chunk: 
                    i = i + 1
                    f.write(chunk)
                    percent = (n / maxB) * 100
                    print("Download Progress: " + str(int(percent)) + "% ::: iter_bytepos: " + str(n) + " ::: writing file chunk " + str(i) + "...")
                    n = n + 8192
        return local_filename

    def unpack(path, outDir):
        try:
            with zipfile.ZipFile(path, 'r') as zip_ref:
                print(zip_ref.printdir())
                print('Extracting .cadberryheights resources...')
                zip_ref.extractall(outDir)
                print("Done.")
        except Exception as erro:
                print("Could not unpack zip file.")
                print(erro)

    def checkInstall():
        err = 0
        temp = os.environ['appdata']
        if os.path.isfile(temp + "\\.cadberryheights\\installed.derp") != True:
            err = 1
        return err

    def displayWindow():
        temp = os.environ['temp']
        comm = 'from PyQt5 import QtCore, QtGui, QtWidgets\n\nclass Ui_Dialog(object):\n    def setupUi(self, Dialog):\n        Dialog.setObjectName("Dialog")\n        Dialog.resize(400, 107)\n        Dialog.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(52, 14, 14, 255), stop:1 rgba(0, 0, 40, 255));")\n        self.label = QtWidgets.QLabel(Dialog)\n        self.label.setGeometry(QtCore.QRect(10, 0, 371, 61))\n        self.label.setStyleSheet("font: 8pt \\"Onyx\\";\\n"\n"background-color: rgba(255, 255, 255, 0);\\n"\n"color: rgb(170, 0, 0);")\n        self.label.setObjectName("label")\n        self.label_2 = QtWidgets.QLabel(Dialog)\n        self.label_2.setGeometry(QtCore.QRect(10, 75, 371, 21))\n        self.label_2.setStyleSheet("font: 8pt \\"OCR A Extended\\";\\n"\n"background-color: rgba(255, 255, 255, 0);\\n"\n"color: rgb(170, 0, 0);")\n        self.label_2.setObjectName("label_2")\n\n        self.retranslateUi(Dialog)\n        QtCore.QMetaObject.connectSlotsByName(Dialog)\n\n    def retranslateUi(self, Dialog):\n        _translate = QtCore.QCoreApplication.translate\n        Dialog.setWindowTitle(_translate("Dialog", "Cadberry Heights Launcher (Installing Resources...)"))\n        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\\" font-size:36pt; font-weight:600;\\">Cadberry Heights Launcher</span></p></body></html>"))\n        self.label_2.setText(_translate("Dialog", "<html><head/><body><p><span style=\\" font-size:9pt; font-weight:600;\\">Installing Resources... (This may take a bit).</span></p></body></html>"))\n\nif __name__ == "__main__":\n    import sys\n    app = QtWidgets.QApplication(sys.argv)\n    Dialog = QtWidgets.QDialog()\n    ui = Ui_Dialog()\n    ui.setupUi(Dialog)\n    Dialog.show()\n    sys.exit(app.exec_())'
        fileIO.saveFile(temp + ".\\progress.py", comm)
        exec(comm)

class updater:
    def checkUpdates():
        temp = os.environ['appdata']
        installer.download("https://ourcloud.nspes.ca/index.php/s/owcaq5k2cGgKRSB/download", temp + "\\.cadberryheights\\updateList.cxl", 1000)
        updateList = fileIO.getFile(temp + "\\.cadberryheights\\updateList.cxl")
        if os.path.isfile(temp + "\\.cadberryheights\\currentUpdate.cx") == True:
            currentUpdate = fileIO.getFile(temp + "\\.cadberryheights\\currentUpdate.cx")
        else:
            currentUpdate = 0.9
            fileIO.saveFile(temp + "\\.cadberryheights\\currentUpdate.cx", "0.9")
        updater.update(updateList, currentUpdate)

    def update(updateList, currentUpdate):
        temp = os.environ['appdata']
        i = 0
        n = 0
        while i < len(updateList.split("\n")):
            if float(str(str(updateList.split("\n")[i]).split("^")[0])) > float(str(currentUpdate).split(" ")[0]):
                if updateList.split("\n")[i].split("^")[1] != "null":
                    fileIO.saveFile(temp + ".\\.cadberryheights\\updateexec.py", "print(\"Launcher Updater: No update to execute.\"")
                    url = updateList.split("\n")[i].split("^")[1]
                    installer.download(url, temp + ".\\.cadberryheights\\" + updateList.split("\n")[i].split("^")[0] + ".zip", 1000)
                    installer.unpack(temp + ".\\.cadberryheights\\" + updateList.split("\n")[i].split("^")[0] + ".zip", temp + ".\\.cadberryheights\\.cadberryheights")
                    try:
                        print("step 0")
                        comm = fileIO.getFile(temp + ".\\.cadberryheights\\updateexec.py")
                        print("step 1")
                        try:
                            exec(comm)
                        except:
                            print("Nothing to run.")
                        print("step 2")
                        fileIO.saveFile(temp + "\\.cadberryheights\\currentUpdate.cx", updateList.split("\n")[i].split("^")[0])
                        print("step 3")
                        print(temp + "\\.cadberryheights\\currentUpdate.cx" + ", " + updateList.split("\n")[i].split("^")[0])
                        print("step 4")
                        n = 1
                    except Exception as err:
                        print(str(err))
                else:
                    fileIO.saveFile(temp + "\\.cadberryheights\\currentUpdate.cx", "1.0")
            i = i + 1
        return n
                

def installerComm():
    temp = os.environ['appdata']
    os.chdir(temp + "\\.cadberryheights")
    if installer.checkInstall() != 0:
        installer.install()
        print("Lack of install detected.")
    updater.checkUpdates()
    print("installerComm")

def main():
    exit = 0
    while exit == 0:
        time.sleep(1)
        if installer.checkInstall() == 0:
            mainn()
            exit = 1

def run():
    os.system("mkdir \"%appdata%\\.cadberryheights\"")
    lc = threading.Lock()
    installerRun = threading.Thread(target=installerComm)
    commandsRun = threading.Thread(target=main)
    installerRun.start()
    commandsRun.start()

run()