from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setWindowIcon(QtGui.QIcon('./images/icons/icon.png'))
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 760)

        font_id = QtGui.QFontDatabase.addApplicationFont("fonts/theboldfont.ttf")
        if font_id == -1:
            print("Erreur : la police n'a pas pu être chargée.")
        else:
            font_family = QtGui.QFontDatabase.applicationFontFamilies(font_id)[0]

        MainWindow.setStyleSheet("background-color: #2E8B57\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 570, 281, 81))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("QLabel {\n"
"    color: black; \n"
"    background-color: #E8F0FE;\n"
"    border: 1px solid #B0C4DE;\n"
"    border-radius: 6px; \n"
"    padding: 4px 8px; \n"
"    font-size: 18px;\n"
"    text-align: center;\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(710, 570, 281, 81))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setStyleSheet("QLabel {\n"
"    color: black; \n"
"    background-color: #E8F0FE; \n"
"    border: 1px solid #B0C4DE; \n"
"    border-radius: 6px; \n"
"    padding: 4px 8px;\n"
"    font-size: 18px;\n"
"    text-align:center;\n"
"}\n"
"")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(420, 560, 211, 101))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #3C91E6; \n"
"    border: 1px solid #2B7CB8;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px; \n"
"    font-size: 24px; \n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5AA7EA; \n"
"    border: 1px solid #3C91E6; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2B7CB8; \n"
"    border: 1px solid #235E8E;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #9DA9B3; \n"
"    color: #6C757D; \n"
"    border: 1px solid #6C757D;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(40, 40, 341, 491))
        self.label_3.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("ui\\../images/back.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(680, 40, 341, 491))
        self.label_4.setStyleSheet("background-color: rgba(0,0,0,0)")
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("ui\\../images/back.png"))
        self.label_4.setObjectName("label_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(460, 670, 131, 31))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #ff4646; \n"
"    border: 1px solid #c33434;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px; \n"
"    font-size: 14px; \n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #e63c3c; \n"
"    border: 1px solid #c33434;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #bd3131; \n"
"    border: 1px solid #8b2525;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #9DA9B3; \n"
"    color: #6C757D; \n"
"    border: 1px solid #6C757D;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setGeometry(QtCore.QRect(420, 230, 211, 41))
        self.label_5.setFont(QtGui.QFont(font_family, 22))
        self.label_5.setStyleSheet("QLabel {\n"
"    color: black; \n"
"    background-color: #E8F0FE; \n"
"    border: 1px solid #B0C4DE; \n"
"    border-radius: 6px; \n"
"    padding: 4px 8px;\n"
"    font-size: 18px;\n"
"    text-align:center;\n"
"}\n"
"")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(425, 290, 200, 75))
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setFont(QtGui.QFont(font_family, 11))
        self.label_6.setStyleSheet("color: white\n"
"")
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 690, 41, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    color: #ffffff;\n"
"    background-color: #3C91E6; \n"
"    border: 1px solid #2B7CB8;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px; \n"
"    font-size: 24px; \n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #5AA7EA; \n"
"    border: 1px solid #3C91E6; \n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2B7CB8; \n"
"    border: 1px solid #235E8E;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #9DA9B3; \n"
"    color: #6C757D; \n"
"    border: 1px solid #6C757D;\n"
"}")
        self.pushButton_3.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ui\\../images/icons/credits.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QtCore.QSize(48, 48))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.partie = None

        self.pushButton.clicked.connect(self.jouer_tour)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Jeu de la Bataille"))
        self.label.setText(_translate("MainWindow", "{Joueur1}: {nbCartes} cartes"))
        self.label_2.setText(_translate("MainWindow", "{Joueur2}: {nbCartes} cartes"))
        self.pushButton.setText(_translate("MainWindow", "Jouer un tour"))
        self.pushButton_2.setText(_translate("MainWindow", "Jouer auto"))
        self.label_5.setText(_translate("MainWindow", "Tour n°{tour}"))
        self.label_6.setText(_translate("MainWindow", ""))

    def mettre_a_jour_labels(self):
        if self.partie:
            self.label.setText(f"{self.partie.joueurs[0].get_nom()}: {self.partie.joueurs[0].get_nb_cartes()} cartes")
            self.label_2.setText(f"{self.partie.joueurs[1].get_nom()}: {self.partie.joueurs[1].get_nb_cartes()} cartes")
            self.label_5.setText(f"tour n°{self.partie.get_nb_tour()}")

    def update_message_label(self, message):
        self.label_6.setText(message)

    def jouer_tour(self):
        self.pushButton.setEnabled(False)
        if self.partie and not self.partie.jouer_tour():
            self.mettre_a_jour_labels()

        QtCore.QTimer.singleShot(1000, lambda: self.pushButton.setEnabled(True))

    def auto_play_turns(self):
        if self.partie is None or not self.auto_play_active:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            return

        if self.partie and not self.partie.jouer_tour():
            self.mettre_a_jour_labels()

        if self.partie.partie_terminee:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            return

        QtCore.QTimer.singleShot(1000, self.auto_play_turns)

    def update_card_images(self, image_joueur1, image_joueur2):
        self.label_3.setPixmap(QtGui.QPixmap(image_joueur1))
        self.label_4.setPixmap(QtGui.QPixmap(image_joueur2))