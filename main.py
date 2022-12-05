import numpy as np
from PyQt6 import QtCore, QtGui, QtWidgets
from Authorisation import Ui_MainWindow
from encryption import Ui_encryption
from PyQt6.QtWidgets import QMessageBox
import sys

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


def returnToMain():
    encryption.close()
    MainWindow.show()


def getLog():
    log = ui.loginTextField.toPlainText()
    return log


def getPass():
    pas = ui.passwordTextField.toPlainText()
    return pas


def clear():
    ui.loginTextField.setPlainText("")
    ui.passwordTextField.setPlainText("")


def message(text):
    msg = QMessageBox()
    msg.setWindowTitle("Уведомление")
    msg.setText(text)
    msg.exec()


def encrypt(a):
    a = list(a)
    key = 7
    a = np.array(a)
    pass_len = len(a)
    matrix = np.full((5 + key, key), ' ')
    flag = 0
    for i in range(5 + key):
        for j in range(key):
            if flag < pass_len:
                matrix[i][j] = a[flag]
                flag += 1

    matrix = matrix.transpose()
    result = ""
    for i in range(key):
        for j in range(5 + key):
            result += matrix[i][j]
    return result


def decrypt(b):
    b = list(b)
    key = 7
    pass_len = len(b)
    matrix = np.full((key, 5 + key), ' ')
    flag = 0
    for i in range(key):
        for j in range(5 + key):
            if flag < pass_len:
                matrix[i][j] = b[flag]
                flag += 1
    matrix = matrix.transpose()
    result = ""
    for i in range(5 + key):
        for j in range(key):
            result += matrix[i][j]
    return result


def auth():
    with open('user_data.txt', 'r') as f:
        flag = 0
        credentials = getLog() + getPass()
        for row in f:
            if row == encrypt(credentials) + "\n":
                flag = 1
                break
    clear()
    if flag == 1:
        global encryption
        encryption = QtWidgets.QMainWindow()
        ui = Ui_encryption()
        ui.setupUi(encryption)
        MainWindow.close()
        encryption.show()

        def toMain():
            MainWindow.show()
            encryption.close()

        def textEnc():
            text = ui.plainTextEdit.toPlainText()
            if len(text) > 256:
                message("Превышен лимит символов")
            else:
                with open("encryptedText.txt", "w") as k:
                    k.write(encrypt(text))
                message("Зашифрованный текст записан в файл encryptedText.txt")

        def textBack():
            encryptedText = ui.plainTextEdit_2.toPlainText()
            if len(encryptedText) > 256:
                message("Превышен лимит символов")
            else:
                encryptedText = decrypt(encryptedText)
                encryptedText = encryptedText.strip()
                mes = "Расшифровка: \n" + encryptedText
                message(mes + "\nРасшифрованный текст записан в decryptedText.txt")
                with open("decryptedText.txt", "w") as k:
                    k.write(mes)

        ui.pushButton.clicked.connect(toMain)
        ui.encryptButton.clicked.connect(textEnc)
        ui.tutanhamonButton.clicked.connect(textBack)
    else:
        message("Неверный логин или пароль")


def registration():
    with open('log.txt', 'r') as f:
        for row in f:
            flag = 0
            if (encrypt(getLog()) + "\n") == row:
                message("Такой логин уже есть")
                flag = 1
                break
        if flag == 0:
            with open('log.txt', 'a') as f:
                f.write(encrypt(getLog()) + "\n")
            with open('user_data.txt', 'a') as d:
                credentials = getLog() + getPass()
                d.write(encrypt(credentials) + '\n')
            clear()
        else:
            message("Неправильные логин или пароль")


ui.registerButton.clicked.connect(registration)
ui.loginButton.clicked.connect(auth)

sys.exit(app.exec())
