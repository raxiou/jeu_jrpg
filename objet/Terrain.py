from copy import deepcopy
class Terrain:
    def __init__(self,joueur):
        '''La class Terrain comme son nom l'indique permet de gerer le terrain
         il a tout d'abord l'attribut terrain sous forme de liste de liste
         ensuite l'atribut affiche qui permet d'afficher le terrain avec les personnage dessus
         il a besoin du joueur pour permettre de placer celui ci derectement sur le terrain'''
        self.terrain = [
                      [0, 0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],]

        self.affiche = deepcopy(self.terrain)
        self.affiche_modif(joueur.x,joueur.y,joueur.pion, False) ##affiche le joueur


    def modif_terain(self,x,y,modification):
        '''modifie directement le terrain'''
        self.terrain[x][y] = modification

    def mur(self,x,y):
        '''renvoie True si la case est inaccessible'''
        return 1 == self.terrain[x][y]

    def affiche_modif(self,x,y,affichage, a_changer):
        '''modifie l'affichage par exemple quand le joueur se déplace'''
        print(a_changer)
        self.affiche[x][y] = affichage
        if a_changer:
            print('cc')
            print(self.terrain[a_changer[0]][a_changer[1]])
            self.affiche[a_changer[0]][a_changer[1]] = self.terrain[a_changer[0]][a_changer[1]]
