
#=======================Classe représentant l'arbre binaire ==================


class ArbreBinaire:
    def __init__(self, valeur):
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None

    def inserer_gauche(self,valeur):
        if self.enfant_gauche == None:
            self.enfant_gauche=ArbreBinaire(valeur)
        else:
            nouveau_noeud=ArbreBinaire(valeur)
            nouveau_noeud.enfant_gauche=self.enfant_gauche
            self.enfant_gauche=nouveau_noeud


    def inserer_droit(self,valeur):
        if self.enfant_droit == None :
            self.enfant_droit = ArbreBinaire(valeur)
        else :
            nouveau_noeud = ArbreBinaire(valeur)
            nouveau_noeud.enfant_droit = self.enfant_droit
            self.enfant_droit = nouveau_noeud

    def get_valeur(self):
        return self.valeur

    def get_enfant_gauche(self):
        return self.enfant_gauche

    def get_enfant_droit(self):
        return self.enfant_droit



#============================Jeu de tests========================================

racine = ArbreBinaire('A')
racine.inserer_gauche('B')
racine.inserer_droit('F')

b_noeud = racine.get_enfant_gauche()
b_noeud.inserer_gauche('C')
b_noeud.inserer_droit('D')

f_noeud = racine.get_enfant_droit()
f_noeud.inserer_gauche('G')
f_noeud.inserer_droit('H')

c_noeud = b_noeud.get_enfant_gauche()
c_noeud.inserer_droit('E')

g_noeud = f_noeud.get_enfant_gauche()
g_noeud.inserer_gauche('I')

h_noeud = f_noeud.get_enfant_droit()
h_noeud.inserer_droit('J')

def AfficheArbre(arbre):
    if arbre != None :
        return (arbre.get_valeur(),AfficheArbre(arbre.get_enfant_gauche()),AfficheArbre(arbre.get_enfant_droit()))

print(AfficheArbre(racine))