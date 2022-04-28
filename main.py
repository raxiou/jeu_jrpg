from objet.Terrain import Terrain
from objet.personnage import Personage
import time

def jeu():
    joueur = Personage('philipe', 'joueur', (0, 0))
    terrain = Terrain(joueur)
    arret = False
    while not arret:
        print(terrain.affiche)
        if input('direction?')=='d':
            joueur.deplacement_droit(terrain)
        time.sleep(1)


jeu()



