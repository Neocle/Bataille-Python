from modules.jeu import JeuCartes
from modules.joueur import Joueur
from PyQt5 import QtCore

class Bataille(QtCore.QObject):
    """ Classe pour le jeu de bataille entre deux joueurs """
    partie_terminee_signal = QtCore.pyqtSignal(str)
    mise_a_jour_cartes = QtCore.pyqtSignal(str, str)
    attendre_entree = QtCore.pyqtSignal()
    message_jeu = QtCore.pyqtSignal(str)
    
    def __init__(self, nb_cartes, joueur1, joueur2):
        """
        Initialise le jeu de bataille

        nb_cartes: Nombre total de cartes dans le jeu.
        joueur1: Nom du premier joueur.
        joueur2: Nom du second joueur.
        """
        super().__init__()
        self.jeu = JeuCartes(nb_cartes)
        self.jeu.melanger()
        # Initialisation des joueurs avec la moitié des cartes pour chacun.
        self.joueurs = [Joueur(nb_cartes // 2, joueur1), Joueur(nb_cartes // 2, joueur2)]
        distribution = self.jeu.distribuer_jeu(2, nb_cartes // 2)
        self.joueurs[0].inserer_main(distribution[0])
        self.joueurs[1].inserer_main(distribution[1])
        self.tour = 0
        self.partie_terminee = False
        self.en_bataille = False
        self.etape_bataille = 0
        # Piles de cartes temporaires pour les batailles
        self.pile_j1 = []
        self.pile_j2 = []

    def get_nb_tour(self):
        """
        Retourne le nombre actuel de tours joués dans la partie
        return Nombre de tours joués.
        """
        return self.tour

    def jouer_tour(self):
        """
        Effectue un tour du jeu, gère la logique de comparaison de cartes
        return True si la partie est terminée et False sinon
        """
        if self.partie_terminee:
            return True

        # étape de la bataille si en cours
        if self.en_bataille:
            self.jouer_etape_bataille()
            return False

        self.tour += 1

        # Les joueurs jouent une carte
        carte_joueur_1 = self.joueurs[0].jouer_carte()
        carte_joueur_2 = self.joueurs[1].jouer_carte()

        # un joueur n'a plus de carte -> perd la partie
        if carte_joueur_1 is None or carte_joueur_2 is None:
            self.partie_terminee = True
            self.annoncer_vainqueur()
            return True

        # signal pour l'interface graphique
        self.mise_a_jour_cartes.emit(
            f"images/{carte_joueur_1.get_valeur()}-{carte_joueur_1.get_couleur()}.png",
            f"images/{carte_joueur_2.get_valeur()}-{carte_joueur_2.get_couleur()}.png"
        )

        # Determine le gagnant du tour 
        if carte_joueur_1.est_superieure_a(carte_joueur_2):
            self.message_jeu.emit(f"{self.joueurs[0].get_nom()} gagne\nle tour!") # envoie un signal pour l'interface graphgique
            self.joueurs[0].inserer_main([carte_joueur_1, carte_joueur_2])
        elif carte_joueur_2.est_superieure_a(carte_joueur_1):
            self.message_jeu.emit(f"{self.joueurs[1].get_nom()} gagne\nle tour!")
            self.joueurs[1].inserer_main([carte_joueur_1, carte_joueur_2])
        else:
            # Cartes egales -> bataille
            self.en_bataille = True
            self.message_jeu.emit("Bataille!")
            self.etape_bataille = 1

            self.pile_j1 = [carte_joueur_1]
            self.pile_j2 = [carte_joueur_2]
            self.attendre_entree.emit()

        # Verifie si un joueur a perdu toutes ses cartes
        if self.joueurs[0].get_nb_cartes() == 0 or self.joueurs[1].get_nb_cartes() == 0:
            self.partie_terminee = True
            self.annoncer_vainqueur()
            return True
        
        return False

    def jouer_etape_bataille(self):
        """
        Gère les étapes de la bataille lorsque les deux joueurs ont joué des cartes
        de même valeur. Deux étapes: cartes face cachées et cartes face visibles
        """
        if self.etape_bataille == 1:
            # Étape 1 : Les joueurs posent une carte face cachée
            self.message_jeu.emit("Les joueurs posent une\ncarte face cachée")
            self.mise_a_jour_cartes.emit("images/back.png", "images/back.png")
            if self.joueurs[0].get_nb_cartes() > 0 and self.joueurs[1].get_nb_cartes() > 0:
                self.pile_j1.append(self.joueurs[0].jouer_carte())
                self.pile_j2.append(self.joueurs[1].jouer_carte())
            self.etape_bataille = 2
            self.attendre_entree.emit()

        elif self.etape_bataille == 2:
            # Étape 2 : Les joueurs posent une carte face visible
            self.message_jeu.emit("Les joueurs posent une\ncarte face visible")
            if self.joueurs[0].get_nb_cartes() > 0 and self.joueurs[1].get_nb_cartes() > 0:
                carte_visible_j1 = self.joueurs[0].jouer_carte()
                carte_visible_j2 = self.joueurs[1].jouer_carte()
                self.pile_j1.append(carte_visible_j1)
                self.pile_j2.append(carte_visible_j2)
                self.mise_a_jour_cartes.emit(
                    f"images/{carte_visible_j1.get_valeur()}-{carte_visible_j1.get_couleur()}.png",
                    f"images/{carte_visible_j2.get_valeur()}-{carte_visible_j2.get_couleur()}.png"
                )
                
                # Determine le gagnant/relance une autre bataille
                if carte_visible_j1.est_superieure_a(carte_visible_j2):
                    self.message_jeu.emit(f"{self.joueurs[0].get_nom()} gagne\nla bataille!")
                    self.joueurs[0].inserer_main(self.pile_j1 + self.pile_j2)
                elif carte_visible_j2.est_superieure_a(carte_visible_j1):
                    self.message_jeu.emit(f"{self.joueurs[1].get_nom()} gagne\nla bataille!")
                    self.joueurs[1].inserer_main(self.pile_j1 + self.pile_j2)
                else:
                    # Nouvelle egalite -> relance la bataille
                    self.message_jeu.emit("Nouvelle bataille!")
                    self.etape_bataille = 1
                    return

            # Fin -> réinitialise les piles de cartes
            self.en_bataille = False
            self.etape_bataille = 0
            self.pile_j1.clear()
            self.pile_j2.clear()
        self.attendre_entree.emit()

    def annoncer_vainqueur(self):
        """
        Détermine et annonce le gagnant de la partie en fonction du joueur
        qui a encore des cartes. Émet un signal avec le nom du vainqueur pour l'interrface graphique
        """
        if self.joueurs[0].get_nb_cartes() == 0:
            nom_vainqueur = self.joueurs[1].get_nom()

            self.mise_a_jour_cartes.emit(
                f"images/blank.png",
                f"images/back.png"
            )
        else:
            nom_vainqueur = self.joueurs[0].get_nom()
        self.partie_terminee_signal.emit(nom_vainqueur)
