import turtle

def squer(side):
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)

for i in range(4):
    squer(100)
turtle.left(45)
for _ in range(4):
    squer(100)
