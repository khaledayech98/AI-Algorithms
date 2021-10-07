from random import *
L=[]
i=0
while(i<4):
    alea = (randint(0,7),randint(0,7))
    if (alea not in L):
        L.append(alea)
        i=i+1
print(L)
