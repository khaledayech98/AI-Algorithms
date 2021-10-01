
#===============================Fonctions======================================================

def TriListeObjetsSurValeur(ListeObjets):
    for i in range(len(ListeObjets)):
        for j in range(0,len(ListeObjets)-i-1):
            if(ListeObjets[j].valeur < ListeObjets[j+1].valeur):
                ListeObjets[j], ListeObjets[j+1] = ListeObjets[j+1],ListeObjets[j]

def RemplirLeSac(ListeObjetsTrieeParValeur,Sac):
    CapaciteTotale = 0
    CompteurObjet = 0
    while( (Sac.capacite >= CapaciteTotale) and (CompteurObjet <= len(ListeObjetsTrieeParValeur)-1)):

        if(Sac.capacite >= CapaciteTotale + ListeObjetsTrieeParValeur[CompteurObjet].poids ):
            Sac.ListeObjet.append(ListeObjetsTrieeParValeur[CompteurObjet])
            CapaciteTotale = CapaciteTotale + ListeObjetsTrieeParValeur[CompteurObjet].poids
        CompteurObjet = CompteurObjet + 1


#===============================Classes========================================================

class Objet :
    def __init__(self, nom, poids, valeur):
        self.poids = poids
        self.valeur = valeur
        self.nom=nom
    def GetPoids(self):
        return self.poids

    def GetValeur(self):
        return self.valeur
    def GetNom(self):
        return self.nom

class SacADos :
    def __init__(self,CapaciteMax,ListeObjet):
        self.capacite=CapaciteMax
        self.ListeObjet = ListeObjet

    def GetCapacite(self):
        return self.capacite

    def GetListeObjets(self):
        return self.ListeObjet


#==================================Jeu de tests================================================

#region Initialisation
Stylo = Objet("Stylo",1,3)
Cahier = Objet("Cahier",5,3)
Livre = Objet("Livre",10,5)
Portefeuille =Objet("Portefeuille", 8,2)
Regle =Objet("Regle", 2,1)
Calculatrice =Objet("Calculatrice", 1,1)
Lunettes = Objet("Lunettes", 1,8)

ListeObjets = [Stylo,Cahier,Livre,Portefeuille,Regle,Calculatrice,Lunettes]

Sac = SacADos(15,[])
#endregion
TriListeObjetsSurValeur(ListeObjets)
RemplirLeSac(ListeObjets,Sac)

for obj in Sac.ListeObjet:
    print(obj.nom,obj.poids)

#===============================================================================================