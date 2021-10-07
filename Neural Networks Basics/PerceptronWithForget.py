import numpy as np

def CalculSortieReelle(A, s):
    for i in range(len(A)):
        for j in range(len(A[i])):
            if ( A[i][j] >= s ) :
                O[i][j] = 1

X = np.array([[1, 0, 1], [1, 1, 0], [0, 0, 1], [0, 1, 1]])

W = np.array([[0.90, 0.78, 0.64], [-0.54, 0.52, -0.11], [0.21, -0.09, 0.23], [-0.03, -0.96, 0.58]])   #Matrice des poids arbitrairement choisie

T = np.array([[0, 0, 1], [1, 1, 1], [0, 1, 0]])


Seuil = 0
FacteurApprentissage= 0.75
NombreIteration = 0
MatriceTransposeePoids = np.transpose(W)
MatriceEntreeTransposee = np.transpose(X)

A = np.matmul(MatriceTransposeePoids, X)

O = np.zeros(shape=T.shape)

CalculSortieReelle(A, Seuil)

while (True):
    if(np.array_equal(T,O)):
        break
    for i in range(len(T)):
        for j in range(len(T[0])):
            if (T[i][j] > O[i][j]):
                np.transpose(W)[j] = np.transpose(W)[j] + 0.3

            elif (T[i][j] < O[i][j]):
                np.transpose(W)[j] = np.transpose(W)[j] - 0.3
            A = np.matmul(np.transpose(W), X)
            CalculSortieReelle(A, Seuil)


print(W)

