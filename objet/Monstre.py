from personnage import Personage

class Monstre(Personage):

    def __init__(self, nom, position, representation, espece):
        super().__init__(nom, position, representation)

        self.espece = espece

    def choix_deplacement(self, cordonee_joueur):


