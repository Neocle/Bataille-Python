import random
from modules.carte import Carte, COULEURS, NOM

class JeuCartes:
    """Représente un jeu de cartes pour un jeu de cartes standard."""
    
    def __init__(self, nb_cartes):
        if nb_cartes not in [32, 52]:
            raise ValueError("Le jeu doit contenir 32 ou 52 cartes.")
        self.nb_cartes = nb_cartes
        self.jeu = []
        self.creer_jeu()
        
    def creer_jeu(self):
        """Crée le jeu de cartes en fonction du type de jeu (32 ou 52 cartes)."""
        depart = 7 if self.nb_cartes == 32 else 2
        for couleur in COULEURS:
            for j in range(depart - 2, len(NOM)):
                self.jeu.append(Carte(NOM[j], couleur))
              
    def get_jeu(self):
        """Retourne le jeu de cartes."""
        return self.jeu
         
    def melanger(self):
        """Mélange les cartes."""
        random.shuffle(self.jeu)
         
    def distribuer_carte(self):
        """Distribue une carte du haut du jeu."""
        return self.jeu.pop() if self.jeu else None
        
    def distribuer_jeu(self, nb_joueurs, nb_cartes):
        """Distribue des cartes aux joueurs."""
        distribution = []
        for _ in range(nb_joueurs):
            main_joueur = [self.distribuer_carte() for _ in range(nb_cartes)]
            distribution.append(main_joueur)
        return distribution

        
if __name__ == "__main__":
    mon_jeu = JeuCartes(32)
    print(mon_jeu)
    le_paquet = mon_jeu.get_jeu()
    print("--------------------------------------------------------------------------------")
    print("Paquet de cartes créé :")
    print("--------------------------------------------------------------------------------")
    for carte in le_paquet:
        print(carte.affichage_carte())
    mon_jeu.melanger()
    print("--------------------------------------------------------------------------------")
    print("Paquet de cartes mélangé :")
    print("--------------------------------------------------------------------------------")
    for carte in le_paquet:
        print(carte.affichage_carte())
    print("--------------------------------------------------------------------------------")
    jeu_divise = mon_jeu.distribuer_jeu(2, 16)
    for i, main in enumerate(jeu_divise):
        print(f"----------------------> Jeu {i+1}")
        for carte in main:
            print(carte.affichage_carte())