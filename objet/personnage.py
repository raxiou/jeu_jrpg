class Personage:
    def __init__(self, nom, type, position):
        '''class qui permet de créer les personnage
        nom et le nom de celui ci
        type est son espèce/role
        position est ca position sous forme de tuple par exemple: (1,0) pour x=1 et y =0
        pion est ca représentation dans l'affichage'''
        self.nom = nom
        self.type = type
        self.x = position[0]
        self.y = position[1]
        self.pion = 'X'

    def affichage(self, Terrain, encienne_coordonne):
        '''modifie l'affichage du terrain'''
        Terrain.affiche_modif(self.x, self.y, self.pion, encienne_coordonne)

    def deplacement_haut(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x - 1, self.y):
            self.x -= 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_bas(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x + 1, self.y):
            self.x += 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_gauche(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x, self.y- 1):
            self.y -= 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_droit(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x, self.y+ 1):
            self.y += 1
            self.affichage(terrain, encienne_coordonne)



