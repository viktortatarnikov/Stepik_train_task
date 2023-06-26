import turtle

def kvad(size):
    turtle.pendown()
    turtle.pensize(15)
    turtle.dot()
    turtle.penup()
    turtle.forward(size)


for i in range(10):
    kvad(30)