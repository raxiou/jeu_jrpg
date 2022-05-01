from objet.Terrain import Terrain
from objet.personnage import Personage
from time import sleep
import keyboard

def jeu():
    joueur = Personage('philipe', 'joueur', (0, 0))
    terrain = Terrain(joueur)
    arret = False
    while not arret:
        print(terrain.affiche)
        lettre = keyboard.read_key()
        if lettre == 'd':
            joueur.deplacement_droit(terrain)
        elif lettre == 'q':
            joueur.deplacement_gauche(terrain)
        elif lettre == 'z':
            joueur.deplacement_haut(terrain)
        elif lettre == 's':
            joueur.deplacement_bas(terrain)
        sleep(1)


jeu()



