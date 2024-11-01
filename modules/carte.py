# -*- coding: utf-8 -*-

COULEURS = ('♦', '♥', '♣', '♠')
NOM = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
VALEURS = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

class Carte:
 
    def __init__(self, nom, couleur):
        self.__nom = nom
        self.__couleur = couleur
        self.__valeur = VALEURS[nom]
        
    def get_nom(self):  # getter
        return self.__nom

    def get_couleur(self):  # getter
        return self.__couleur

    def get_valeur(self):  # getter
        return self.__valeur

    def egalite(self, deuxieme_carte):
        """ Renvoie True si les cartes ont même valeur, False sinon """
        return self.get_valeur() == deuxieme_carte.get_valeur()
        
    def est_superieure_a(self, deuxieme_carte):
        """ Renvoie True si la valeur de self est supérieure à celle de carte """
        return self.get_valeur() > deuxieme_carte.get_valeur()

    def est_inferieure_a(self, deuxieme_carte):
        """ Renvoie True si la valeur de self est inferieure à celle de carte """
        return self.get_valeur() < deuxieme_carte.get_valeur()

    def affichage_carte(self):
        """ Affiche la carte caractérisée par son nom et sa couleur """
        return f"{self.get_nom()} de {self.get_couleur()}"
    
    def __repr__(self):
        return f"{self.get_nom()} de {self.get_couleur()}"
            
    
if __name__ == "__main__":
    # Test de la classe Carte
    carte1 = Carte('Dame', '♥')
    print(carte1)
    carte2 = Carte('Roi', '♣')
    print(carte2)
    print(carte1.est_inferieure_a(carte2))
    print(carte1.est_superieure_a(carte2))
    print(carte2.est_superieure_a(carte1))
    print(carte2.est_inferieure_a(carte1))
    print(carte1.affichage_carte())
    print(carte2.affichage_carte())