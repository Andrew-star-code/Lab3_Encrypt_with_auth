# Form implementation generated from reading ui file 'Authorisation.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.registerButton = QtWidgets.QPushButton(self.centralwidget)
        self.registerButton.setGeometry(QtCore.QRect(530, 240, 75, 23))
        self.registerButton.setObjectName("registerButton")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget)
        self.loginButton.setGeometry(QtCore.QRect(160, 320, 75, 23))
        self.loginButton.setObjectName("loginButton")
        self.passwordTextField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.passwordTextField.setGeometry(QtCore.QRect(90, 250, 201, 41))
        self.passwordTextField.setObjectName("passwordTextField")
        self.loginTextField = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.loginTextField.setGeometry(QtCore.QRect(90, 190, 201, 41))
        self.loginTextField.setObjectName("loginTextField")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авторизация"))
        self.registerButton.setText(_translate("MainWindow", "Регистрация"))
        self.loginButton.setText(_translate("MainWindow", "Вход"))
