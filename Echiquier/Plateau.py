import turtle
from random import randint

#region dessiner l'echiquier
Circuit = turtle.Turtle()
turtle.Screen().setworldcoordinates(-20, turtle.Screen().window_height()/(-2),500,20)
Circuit.hideturtle()
Circuit.speed(100)
for i in range(4):
    Circuit.forward(400)
    Circuit.right(90)
a = 0
b = 0
for i in range(8):
    if(b == 0):
        a=1
    else:
        a = 0
    for j in range(8):
        Circuit.penup()
        Circuit.goto(j * 50, i * 50 * (-1))
        Circuit.pendown()
        if(a == 0):
            Circuit.fillcolor('#33ff88')
            a=1
        else:
            Circuit.fillcolor('white')
            a=0
        Circuit.begin_fill()
        for k in range(4):
            Circuit.forward(50)
            Circuit.right(90)
        Circuit.end_fill()
    if(b==0):
        b=1
    else:
        b=0
#endregion

#region Mettre en place les déchets à ramasser d'une façon aléatoire
ListeDechets = []
compteurdechets = 0

while compteurdechets < 15:
    alea = (randint(0, 7), randint(0, 7))
    if alea not in ListeDechets:
        ListeDechets.append(alea)
        compteurdechets = compteurdechets + 1

for dechet in ListeDechets:
    Circuit.penup()
    Circuit.goto((20 + (50 * dechet[0])), (-25 - (50 * dechet[1])))
    Circuit.pendown()
    Circuit.fillcolor('red')
    Circuit.begin_fill()
    for i in range(3):
        Circuit.forward(10)
        Circuit.left(120)
    Circuit.end_fill()
#endregion





turtle.exitonclick()
