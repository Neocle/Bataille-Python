from modules.carte import Carte
import random

class Joueur:
    def __init__(self, nb_cartes, nom):
        self.nom = nom
        self.nb_cartes = nb_cartes
        self.main_joueur = []
        
    def get_nb_cartes(self):
        """Retourne le nombre de cartes du joueur."""
        return self.nb_cartes

    def get_nom(self):
        """Retourne le nom du joueur."""
        return self.nom

    def jouer_carte(self):
        """Enlève et renvoie la première carte de la main du joueur."""
        if self.main_joueur:
            carte_jouee = self.main_joueur.pop(0)
            self.nb_cartes = len(self.main_joueur)
            return carte_jouee
        return None

    def inserer_main(self, cartes_gagnees):
        """Insère les cartes gagnées dans la main du joueur."""
        random.shuffle(cartes_gagnees) 
        self.main_joueur += cartes_gagnees
        self.nb_cartes = len(self.main_joueur)
        
    def afficher_main(self):
        """Retourne une représentation de la main du joueur."""
        return self.main_joueur

if __name__ == "__main__":
    joueur = Joueur(2, "Alice")
    joueur.inserer_main([Carte('As', '♦'), Carte('10', '♠')])
    print(f"{joueur.get_nom()} a {joueur.get_nb_cartes()} cartes.")
    carte_jouee = joueur.jouer_carte()
    print(f"{joueur.get_nom()} joue: {carte_jouee.affichage_carte()}")
    print(f"{joueur.get_nom()} a maintenant {joueur.get_nb_cartes()} cartes.")
