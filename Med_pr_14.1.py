import turtle

def romb(size):
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(120)
    turtle.forward(size)
    turtle.left(60)
    turtle.forward(size)
    turtle.left(120)


for _ in range(10):
    romb(100)

    turtle.left(36)