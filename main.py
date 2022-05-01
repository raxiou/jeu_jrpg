from objet.Terrain import Terrain
from objet.personnage import Personage
from objet.sous_class_personnage.Monstre import Monstre
from time import sleep
import keyboard

def affichage_terrain(terrain):
    for liste in terrain.affiche:
        print(liste)
    print('--------------')


def jeu():
    joueur = Personage('philipe', (0, 0), 'X')

    monstre = Monstre('blob_1', (4,3), 'Tdsss', 'blobd')

    terrain = Terrain(joueur)
    arret = False
    affichage_terrain(terrain)
    while not arret:
        lettre = keyboard.read_key()
        if lettre == 'd':
            joueur.deplacement_droit(terrain)
            affichage_terrain(terrain)
            monstre.choix_deplacement((joueur.x, joueur.y), terrain)
        elif lettre == 'q':
            joueur.deplacement_gauche(terrain)
            affichage_terrain(terrain)
            monstre.choix_deplacement((joueur.x, joueur.y), terrain)
        elif lettre == 'z':
            joueur.deplacement_haut(terrain)
            affichage_terrain(terrain)
            monstre.choix_deplacement((joueur.x, joueur.y), terrain)
        elif lettre == 's':
            joueur.deplacement_bas(terrain)
            affichage_terrain(terrain)
            monstre.choix_deplacement((joueur.x, joueur.y), terrain)
        sleep(0.5)


jeu()



