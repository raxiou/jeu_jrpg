from objet.Terrain import Terrain
from objet.personnage import Personage
from time import sleep
import keyboard

def affichage_terrain(terrain):
    for liste in terrain.affiche:
        print(liste)
    print('--------------')


def jeu():
    joueur = Personage('philipe', 'joueur', (0, 0))
    terrain = Terrain(joueur)
    arret = False
    affichage_terrain(terrain)
    while not arret:
        lettre = keyboard.read_key()
        if lettre == 'd':
            joueur.deplacement_droit(terrain)
            affichage_terrain(terrain)
        elif lettre == 'q':
            joueur.deplacement_gauche(terrain)
            affichage_terrain(terrain)
        elif lettre == 'z':
            joueur.deplacement_haut(terrain)
            affichage_terrain(terrain)
        elif lettre == 's':
            joueur.deplacement_bas(terrain)
            affichage_terrain(terrain)
        sleep(0.5)


jeu()



