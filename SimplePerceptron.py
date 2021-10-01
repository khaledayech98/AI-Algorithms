#region Import
import numpy as np

#endregion

#region Fonctions
def CalculSortieReelle(A, s):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if ( A[i][j] >= s ) :
                O[i][j] = 1


def CorrectionPoids(X, W, T, O, FacteurApprentissage, Seuil):
    while (np.array_equal(T, O) != False):
        for i in range(len(T)):
            if (False in T[i]):
                inequal = True
                break

        if (inequal == True):
            W = W + FacteurApprentissage * np.matmul(X, np.transpose(T - O))
        A = np.matmul(np.transpose(W), X)
        CalculSortieReelle(A, Seuil)
#endregion

#region Vecteur d'entrée

X = np.array([[1, 0, 1], [1, 1, 0], [0, 0, 1], [0, 1, 1]])
#endregion

#region Matrice des poids arbitrairement choisie
W = np.array([[0.90, 0.78, 0.64], [-0.54, 0.52, -0.11], [0.21, -0.09, 0.23], [-0.03, -0.96, 0.58]])   #Matrice des poids arbitrairement choisie
#endregion

#region Matrice désirée / théorique
T = np.array([[0, 0, 1], [1, 1, 1], [0, 1, 0]])
#endregion

#region Constantes
Seuil = 0
FacteurApprentissage= 0.75
#endregion

#region Matrice d'activation
A = np.matmul(np.transpose(W), X)
#endregion

#region Initialisation
O = np.zeros(shape=T.shape)
#endregion

#region Appel des fonctions
CalculSortieReelle(A, Seuil)
CorrectionPoids(X, W, T, O, FacteurApprentissage, Seuil)
#endregion


#region Résultat
print("La nouvelle matrice des poids est : \n\n", W)
#endregion
