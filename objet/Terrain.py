from copy import deepcopy
class Terrain:
    def __init__(self,joueur):
        self.terrain = [
                      [0, 0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],]

        self.affiche = deepcopy(self.terrain)
        self.affiche_modif(joueur.x,joueur.y,joueur.pion, False)


    def modif_terain(self,x,y,modification):
        self.terrain[x][y] = modification

    def mur(self,x,y):
        return 1 == self.terrain[x][y]

    def affiche_modif(self,x,y,affichage, a_changer):
        print(a_changer)
        self.affiche[x][y] = affichage
        if a_changer:
            print('cc')
            print(self.terrain[a_changer[0]][a_changer[1]])
            self.affiche[a_changer[0]][a_changer[1]] = self.terrain[a_changer[0]][a_changer[1]]
