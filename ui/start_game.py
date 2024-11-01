from PyQt5 import QtCore, QtGui, QtWidgets

class Start_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setWindowIcon(QtGui.QIcon('./images/icons/icon.png'))
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        Dialog.setStyleSheet("background-color: #2E8B57")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 40, 161, 41))
        self.label.setStyleSheet("QLabel { color: black; background-color: #E8F0FE; border: 1px solid #B0C4DE; border-radius: 6px; padding: 4px 8px; font-size: 14px; text-align: center; }")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 161, 41))
        self.label_2.setStyleSheet("QLabel { color: black; background-color: #E8F0FE; border: 1px solid #B0C4DE; border-radius: 6px; padding: 4px 8px; font-size: 14px; text-align: center; }")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 220, 281, 61))
        self.pushButton.setStyleSheet("QPushButton { color: #ffffff; background-color: #3C91E6; border: 1px solid #2B7CB8; border-radius: 8px; padding: 8px 16px; font-size: 20px; font-weight: bold; } QPushButton:hover { background-color: #5AA7EA; border: 1px solid #3C91E6; } QPushButton:pressed { background-color: #2B7CB8; border: 1px solid #235E8E; } QPushButton:disabled { background-color: #9DA9B3; color: #6C757D; border: 1px solid #6C757D; }")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 160, 141, 41))
        self.label_3.setStyleSheet("QLabel { color: black; background-color: #E8F0FE; border: 1px solid #B0C4DE; border-radius: 6px; padding: 4px 8px; font-size: 14px; text-align: center; }")
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(170, 160, 101, 41))
        self.comboBox.setStyleSheet("QComboBox { color: #333333; background-color: #FFFFFF; border: 1px solid #B0B0B0; border-radius: 4px; padding: 5px 20px 5px 5px; font-size: 14px; font-family: \"Arial\"; } QComboBox::drop-down { border: none; background-color: #FFFFFF; width: 30px; } QComboBox::down-arrow { image: url(\":/images/icons/arrow.png\"); } QComboBox:hover { border: 1px solid #3C91E6; } QComboBox:focus { border: 1px solid #3C91E6; } QComboBox:disabled { background-color: #F0F0F0; color: #A0A0A0; border: 1px solid #C0C0C0; } QComboBox QAbstractItemView { border: 1px solid #B0B0B0; selection-background-color: #3C91E6; selection-color: #FFFFFF; }")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(190, 40, 151, 41))
        self.lineEdit.setStyleSheet("QLineEdit { color: #333333; background-color: #FFFFFF; border: 1px solid #B0B0B0; border-radius: 4px; padding: 8px; font-size: 14px; font-family: \"Arial\"; } QLineEdit:focus { border: 1px solid #3C91E6; background-color: #E8F0FE; } QLineEdit:disabled { background-color: #F0F0F0; color: #A0A0A0; border: 1px solid #C0C0C0; }")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 100, 151, 41))
        self.lineEdit_2.setStyleSheet("QLineEdit { color: #333333; background-color: #FFFFFF; border: 1px solid #B0B0B0; border-radius: 4px; padding: 8px; font-size: 14px; font-family: \"Arial\"; } QLineEdit:focus { border: 1px solid #3C91E6; background-color: #E8F0FE; } QLineEdit:disabled { background-color: #F0F0F0; color: #A0A0A0; border: 1px solid #C0C0C0; }")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.comboBox.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.pushButton.raise_()
        self.label_3.raise_()

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        
        Dialog.setWindowTitle(_translate("Dialog", "Jeu de la Bataille"))
        self.label.setText(_translate("Dialog", "Nom du Joueur n°1 : "))
        self.label_2.setText(_translate("Dialog", "Nom du Joueur n°2 : "))
        self.pushButton.setText(_translate("Dialog", "Commencer la partie"))
        self.label_3.setText(_translate("Dialog", "Nombre de Cartes : "))
        self.comboBox.setItemText(0, _translate("Dialog", "32"))
        self.comboBox.setItemText(1, _translate("Dialog", "52"))
        self.lineEdit.setText(_translate("Dialog", "Joueur 1"))
        self.lineEdit_2.setText(_translate("Dialog", "Joueur 2"))
