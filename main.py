import sys
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from ui.bataille_gui import Ui_MainWindow
from ui.start_game import Start_Dialog
from ui.end_game import End_Dialog
from ui.credits import CreditsDialog
from modules.bataille import Bataille

class DialogueDemarrerPartie(QDialog):
    """ Classe de dialogue pour commencer une nouvelle partie. Permet de saisir les noms des joueurs et de choisir le nombre de cartes """
    def __init__(self):
        super().__init__()
        self.ui = Start_Dialog()
        self.ui.setupUi(self)
        # Connexion au bouton pour valider l'ouverture de la fentre de demarrage
        self.ui.pushButton.clicked.connect(self.demarrer_partie)

    def demarrer_partie(self):
        """
        Démarre la partie en récupérant les noms des joueurs et le nombre de cartes sélectionné.
        Valide les entrées avant de démarrer.
        """
        nom_joueur1 = self.ui.lineEdit.text().strip()
        nom_joueur2 = self.ui.lineEdit_2.text().strip()
        if not nom_joueur1 or not nom_joueur2:
            QMessageBox.warning(self, "Erreur", "Donnez des noms valides pour les deux joueurs!")
            return
        try:
            nb_cartes = int(self.ui.comboBox.currentText())
            if nb_cartes <= 0:
                raise ValueError("Nombre de cartes invalide")
        except ValueError:
            QMessageBox.warning(self, "Erreur", "Entrez un nombre de cartes valide!")
            return

        self.nom_joueur1 = nom_joueur1
        self.nom_joueur2 = nom_joueur2
        self.nb_cartes = nb_cartes
        self.accept()  # Ferme le dialog


class DialogueFinPartie(QDialog):
    """ Class pour afficher le dialogue de fin de partie. Montre le gagnant et propose de recommencer ou de fermer la partie """
    redemarrer_partie = QtCore.pyqtSignal()
    fermer_partie = QtCore.pyqtSignal()

    def __init__(self, nom_gagnant, parent=None):
        super().__init__(parent)
        self.ui = End_Dialog()
        self.ui.setupUi(self)
        # Affiche le nom du gagnant dans l'interface
        self.ui.label.setText(f"{nom_gagnant} a gagné la partie!")
        self.ui.pushButton.clicked.connect(self.recommencer_partie)
        self.ui.pushButton_2.clicked.connect(self.fermer_jeu)

    def recommencer_partie(self):
        """
        Émet un signal pour redémarrer la partie.
        """
        self.redemarrer_partie.emit()
        self.accept()

    def fermer_jeu(self):
        """
        Émet un signal pour fermer la partie.
        """
        self.fermer_partie.emit()
        self.reject()


class FenetrePrincipale(QMainWindow, Ui_MainWindow):
    """
    Classe principale de la fenêtre de jeu.
    Gère l'interface utilisateur, les actions de jeu, et les dialogues.
    """
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.partie = None
        self.jeu_auto_actif = False
        self.afficher_dialogue_demarrer_partie()

        # Connexion des boutons aux fonctions correspondantes
        self.pushButton_3.clicked.connect(self.ouvrir_dialogue_credits)
        self.pushButton_2.clicked.connect(self.jouer_automatiquement)

    def ouvrir_dialogue_credits(self):
        """ Ouvre le dialogue des crédits """
        dialogue_credits = CreditsDialog(self)
        dialogue_credits.exec_()

    def jouer_automatiquement(self):
        """ Active le mode de jeu automatique pour que les tours se jouent automatiquement """
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(False)
        self.jeu_auto_actif = True
        self.jouer_tours_auto()

    def afficher_dialogue_demarrer_partie(self):
        """ Affiche le dialogue de démarrage de partie pour recueillir les informations des joueurs """
        dialogue = DialogueDemarrerPartie()
        resultat_dialogue = dialogue.exec_()

        if resultat_dialogue == QDialog.Accepted:
            # Initialise une nouvelle partie avec les donnees des joueurs mis dans le dialogue de demarrage
            self.partie = Bataille(dialogue.nb_cartes, dialogue.nom_joueur1, dialogue.nom_joueur2)
            self.partie.partie_terminee_signal.connect(self.fin_partie)
            self.partie.mise_a_jour_cartes.connect(self.mettre_a_jour_images_cartes)
            self.partie.message_jeu.connect(self.mettre_a_jour_message)

            self.show()
            self.mettre_a_jour_labels()
        else:
            sys.exit()

    def fin_partie(self, nom_gagnant):
        """ Gère la fin de la partie, affiche le gagnant et envoie le dialogue de fin """
        self.jeu_auto_actif = False
        self.mettre_a_jour_labels()
        dialogue_fin_partie = DialogueFinPartie(nom_gagnant, self)

        dialogue_fin_partie.redemarrer_partie.connect(self.recommencer_partie)
        dialogue_fin_partie.fermer_partie.connect(self.close)

        dialogue_fin_partie.exec_()

    def recommencer_partie(self):
        """ Ferme la fenetre et relance le dialogue de démarrage de partie """
        self.close()
        self.afficher_dialogue_demarrer_partie()

    def mettre_a_jour_labels(self):
        """ Met a jour les labels avec le nombre de cartes des joueurs et le nb du tour """
        if self.partie:
            self.label.setText(f"{self.partie.joueurs[0].get_nom()}: {self.partie.joueurs[0].get_nb_cartes()} cartes")
            self.label_2.setText(f"{self.partie.joueurs[1].get_nom()}: {self.partie.joueurs[1].get_nb_cartes()} cartes")
            self.label_5.setText(f"Tour n°{self.partie.get_nb_tour()}")

    def mettre_a_jour_message(self, message):
        """ Met a jour le label des messages de jeu """
        self.label_6.setText(message)

    def jouer_tour(self):
        """ Joue un tour en appuyant sur le bouton 'jouer tour' avec un délai de 0.15 sec """
        self.pushButton.setEnabled(False)
        if self.partie and not self.partie.jouer_tour():
            self.mettre_a_jour_labels()

        # délai de 0.15 sec
        QtCore.QTimer.singleShot(150, lambda: self.pushButton.setEnabled(True))

    def jouer_tours_auto(self):
        """ Joue les tours automatiquement si le bouton 'jouer auto' a été activé """
        if self.partie is None or not self.jeu_auto_actif:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            return

        if self.partie and not self.partie.jouer_tour():
            self.mettre_a_jour_labels()

        if self.partie.partie_terminee:
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(True)
            return

        # joue le tour d'apres automatiquelent avec un delai dune seconde
        QtCore.QTimer.singleShot(1000, self.jouer_tours_auto)

    def mettre_a_jour_images_cartes(self, image_joueur1, image_joueur2):
        """
        Met à jour les images des cartes jouées pour chaque joueur dans l'interface.
        
        :param image_joueur1: Chemin de l'image de la carte du joueur 1.
        :param image_joueur2: Chemin de l'image de la carte du joueur 2.
        """
        self.label_3.setPixmap(QtGui.QPixmap(image_joueur1))
        self.label_4.setPixmap(QtGui.QPixmap(image_joueur2))

# créé l'interface graphique
if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre_principale = FenetrePrincipale()
    fenetre_principale.show()
    sys.exit(app.exec_())
