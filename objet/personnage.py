class Personage:
    def __init__(self, nom, type, position):
        self.nom = nom
        self.type = type
        self.x = position[0]
        self.y = position[1]
        self.pion = 'X'

    def affichage(self, Terrain, encienne_coordonne):
        Terrain.affiche_modif(self.x, self.y, self.pion, encienne_coordonne)

    def deplacement_haut(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x, self.y - 1):
            self.y -= 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_bas(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x, self.y + 1):
            self.y += 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_gauche(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x - 1, self.y):
            self.x -= 1
            self.affichage(terrain, encienne_coordonne)

    def deplacement_droit(self, terrain):
        encienne_coordonne = (self.x, self.y)
        if not terrain.mur(self.x + 1, self.y):
            self.x += 1
            self.affichage(terrain, encienne_coordonne)



