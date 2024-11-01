from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog

class CreditsDialog(QDialog):
    def __init__(self, parent=None):
        super(CreditsDialog, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_2.clicked.connect(self.close)
        
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('./images/icons/icon.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 297)
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setAutoFillBackground(False)
        Dialog.setStyleSheet("background-color: #2E8B57")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(50, 140, 301, 61))
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setStyleSheet("QLabel {\n"
"    color: black;\n"
"    background-color: #E8F0FE;\n"
"    border: 1px solid #B0C4DE;\n"
"    border-radius: 6px;\n"
"    padding: 4px 8px;\n"
"    font-size: 18px;\n"
"    text-decoration: bold;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(140, 230, 111, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #ff4242;\n"
"    border: 1px solid #ff3434;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #e02d2d;\n"
"    border: 1px solid #ff3434;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #2B7CB8;\n"
"    border: 1px solid #235E8E;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #9DA9B3;\n"
"    color: #6C757D;\n"
"    border: 1px solid #6C757D;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 101, 101))
        self.label_2.setStyleSheet("background-color: rgba(46, 139, 87, 0);\n"
"border: 2px solid black;")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ui\\../images/icons/credits_pic.png"))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Jeu de la Bataille"))
        self.label.setText(_translate("Dialog", "Développé par ALIROL Loïs, 2024"))
        self.pushButton_2.setText(_translate("Dialog", "Fermer"))