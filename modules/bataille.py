from modules.jeu import JeuCartes
from modules.joueur import Joueur
from PyQt5 import QtCore

class Bataille(QtCore.QObject):
    game_over = QtCore.pyqtSignal(str)
    update_cards = QtCore.pyqtSignal(str, str)
    wait_for_input = QtCore.pyqtSignal()
    game_message = QtCore.pyqtSignal(str)

    def __init__(self, nb_cartes, joueur1, joueur2):
        super().__init__()
        self.jeu = JeuCartes(nb_cartes)
        self.jeu.melanger()
        self.joueurs = [Joueur(nb_cartes // 2, joueur1), Joueur(nb_cartes // 2, joueur2)]
        distribution = self.jeu.distribuer_jeu(2, nb_cartes // 2)
        self.joueurs[0].inserer_main(distribution[0])
        self.joueurs[1].inserer_main(distribution[1])
        self.tour = 0
        self.partie_terminee = False
        self.en_bataille = False
        self.etape_bataille = 0
        self.pile_j1 = []
        self.pile_j2 = []

    def get_nb_tour(self):
        return self.tour

    def jouer_tour(self):
        if self.partie_terminee:
            return True

        if self.en_bataille:
            self.jouer_etape_bataille()
            return False

        self.tour += 1

        carte_joueur_1 = self.joueurs[0].jouer_carte()
        carte_joueur_2 = self.joueurs[1].jouer_carte()

        if carte_joueur_1 is None or carte_joueur_2 is None:
            self.partie_terminee = True
            self.annoncer_vainqueur()
            return True

        self.update_cards.emit(
            f"images/{carte_joueur_1.get_valeur()}-{carte_joueur_1.get_couleur()}.png",
            f"images/{carte_joueur_2.get_valeur()}-{carte_joueur_2.get_couleur()}.png"
        )

        if carte_joueur_1.est_superieure_a(carte_joueur_2):
            self.game_message.emit(f"{self.joueurs[0].get_nom()} gagne\nle tour!")
            self.joueurs[0].inserer_main([carte_joueur_1, carte_joueur_2])
        elif carte_joueur_2.est_superieure_a(carte_joueur_1):
            self.game_message.emit(f"{self.joueurs[1].get_nom()} gagne\nle tour!")
            self.joueurs[1].inserer_main([carte_joueur_1, carte_joueur_2])
        else:
            self.en_bataille = True
            self.game_message.emit("Bataille!")
            self.etape_bataille = 1

            self.pile_j1 = [carte_joueur_1]
            self.pile_j2 = [carte_joueur_2]
            self.wait_for_input.emit()

        if self.joueurs[0].get_nb_cartes() == 0 or self.joueurs[1].get_nb_cartes() == 0:
            self.partie_terminee = True
            self.annoncer_vainqueur()
            return True
        
        return False
    def jouer_etape_bataille(self):
        if self.etape_bataille == 1:
            self.game_message.emit("Les joueurs posent une\ncarte face cachée")
            self.update_cards.emit("images/back.png", "images/back.png")
            if self.joueurs[0].get_nb_cartes() > 0 and self.joueurs[1].get_nb_cartes() > 0:
                self.pile_j1.append(self.joueurs[0].jouer_carte())
                self.pile_j2.append(self.joueurs[1].jouer_carte())
            self.etape_bataille = 2
            self.wait_for_input.emit()

        elif self.etape_bataille == 2:
            self.game_message.emit("Les joueurs posent une\ncarte face visible")
            if self.joueurs[0].get_nb_cartes() > 0 and self.joueurs[1].get_nb_cartes() > 0:
                carte_visible_j1 = self.joueurs[0].jouer_carte()
                carte_visible_j2 = self.joueurs[1].jouer_carte()
                self.pile_j1.append(carte_visible_j1)
                self.pile_j2.append(carte_visible_j2)
                self.update_cards.emit(
                    f"images/{carte_visible_j1.get_valeur()}-{carte_visible_j1.get_couleur()}.png",
                    f"images/{carte_visible_j2.get_valeur()}-{carte_visible_j2.get_couleur()}.png"
                )
                
                if carte_visible_j1.est_superieure_a(carte_visible_j2):
                    self.game_message.emit(f"{self.joueurs[0].get_nom()} gagne\nla bataille!")
                    self.joueurs[0].inserer_main(self.pile_j1 + self.pile_j2)
                elif carte_visible_j2.est_superieure_a(carte_visible_j1):
                    self.game_message.emit(f"{self.joueurs[1].get_nom()} gagne\nla bataille!")
                    self.joueurs[1].inserer_main(self.pile_j1 + self.pile_j2)
                else:
                    self.game_message.emit("Nouvelle bataille!")
                    self.etape_bataille = 1
                    return

            self.en_bataille = False
            self.etape_bataille = 0
            self.pile_j1.clear()
            self.pile_j2.clear()
        self.wait_for_input.emit()

    def annoncer_vainqueur(self):
        if self.joueurs[0].get_nb_cartes() == 0:
            winner_name = self.joueurs[1].get_nom()
        else:
            winner_name = self.joueurs[0].get_nom()
        self.game_over.emit(winner_name)

"""if __name__ == "__main__":
    partie = Bataille(52, "Lolo", "Toto")

    while not partie.partie_terminee:
        partie.jouer_tour()"""
