# Form implementation generated from reading ui file 'ui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textBrowserAnswer = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowserAnswer.setObjectName("textBrowserAnswer")
        self.gridLayout.addWidget(self.textBrowserAnswer, 2, 0, 1, 1)
        self.plainTextEditQuestion = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.plainTextEditQuestion.setObjectName("plainTextEditQuestion")
        self.gridLayout.addWidget(self.plainTextEditQuestion, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "English Helper"))
        self.textBrowserAnswer.setPlaceholderText(_translate("MainWindow", "The answer"))
        self.plainTextEditQuestion.setPlaceholderText(_translate("MainWindow", "The question"))
        self.pushButton.setText(_translate("MainWindow", "Generate Response"))