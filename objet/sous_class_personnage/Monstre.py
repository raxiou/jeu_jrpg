from ..personnage import Personage
import math

class Monstre(Personage):

    def __init__(self, nom, position, representation, espece):
        super().__init__(nom, position, representation)

        self.espece = espece

    def choix_deplacement(self, cordonee_joueur, terrain):

        def calcule_distance(cordone1, cordonne2):
            return math.sqrt((cordone1[0]-cordonne2[0])**2 + (cordone1[1]-cordonne2[1])**2)

        cordonee_haut = (self.x - 1, self.y)
        cordonee_bas = (self.x + 1, self.y)
        cordonee_gauche = (self.x , self.y - 1)
        cordonee_droit = (self.x, self.y + 1)

        distance_haut = calcule_distance(cordonee_haut, cordonee_joueur)
        distance_bas = calcule_distance(cordonee_bas, cordonee_joueur)
        distance_gauche = calcule_distance(cordonee_gauche, cordonee_joueur)
        distance_droit = calcule_distance(cordonee_droit, cordonee_joueur)

        if distance_haut >= distance_bas and distance_haut >= distance_gauche and distance_haut >= distance_droit:
            self.deplacement_haut(terrain)
        elif distance_bas >= distance_haut and distance_bas >= distance_gauche and distance_bas >= distance_droit:
            self.deplacement_haut(terrain)
        elif distance_gauche >= distance_bas and distance_gauche >= distance_haut and distance_gauche >= distance_droit:
            self.deplacement_haut(terrain)
        elif distance_droit >= distance_bas and distance_droit >= distance_gauche and distance_droit >= distance_haut:
            self.deplacement_haut(terrain)













