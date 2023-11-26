import turtle


def square(n):
    for _ in range(4):
        turtle.fd(n)
        turtle.rt(90)


def rec_square(n):
    if n <= 1:
        return None
    square(n)
    turtle.rt(10)
    turtle.penup()
    turtle.fd(0.1 * n)
    turtle.pendown()
    return rec_square(0.9 * n)


# rec_square(100)

def color_tree(depth, size):
    turtle.colormode(255)
    cg = 255 - int(depth * (250 / 6)) % 255
    turtle.color(0, cg, 0)
    if depth == 0:
        turtle.fd(size)
    else:
        turtle.fd(size)
        turtle.rt(45)
        color_tree(depth - 1, size * 0.6)
        turtle.penup()
        turtle.bk(size * 0.6)
        turtle.pendown()
        turtle.lt(90)
        color_tree(depth - 1, size * 0.6)
        turtle.penup()
        turtle.bk(size * 0.6)
        turtle.pendown()
        turtle.rt(45)


'''
turtle.left(90)
color_tree(4, 100)
turtle.done()
'''

def branch(n, size):
    if n == 0:
        turtle.lt(180)
        return

    x = size/(n+1)
    for i in range(n):
        turtle.fd(x)
        turtle.lt(45)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.lt(90)
        branch(n-i-1, 0.5*x*(n-i-1))
        turtle.rt(135)

    turtle.fd(x)
    turtle.lt(180)
    turtle.fd(size)

#turtle.tracer(0)
turtle.up()
turtle.goto(0,-100)
turtle.left(90)
turtle.down()
branch(2, 400)
turtle.done()