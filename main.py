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
'''
#turtle.tracer(0)
turtle.up()
turtle.goto(0,-100)
turtle.left(90)
turtle.down()
branch(2, 400)
turtle.done()'''

def koch(order, size):
    if order == 0:
        turtle.fd(size)
    else:
        koch(order-1, size/3)
        turtle.lt(60)
        koch(order-1, size/3)
        turtle.rt(120)
        koch(order-1, size/3)
        turtle.lt(60)
        koch(order-1, size/3)
'''
turtle.up()
turtle.goto(-100,0)
turtle.down()
koch(2,100)
turtle.done()
'''
def koch_snow(n, x):
    for i in range(3):
            koch(n, x)
            turtle.rt(120)
'''turtle.up()
turtle.goto(-100, 0)
turtle.down()
koch_snow(3, 200)
turtle.done()'''

def minkowski(n, size):
    if n == 0:
        turtle.fd(size)
    else:
        minkowski(n-1, size)
        turtle.lt(90)
        minkowski(n - 1, size)
        turtle.rt(90)
        minkowski(n - 1, size)
        turtle.rt(90)
        minkowski(n - 1, size)
        minkowski(n - 1, size)
        turtle.lt(90)
        minkowski(n - 1, size)
        turtle.lt(90)
        minkowski(n - 1, size)
        turtle.rt(90)
        minkowski(n - 1, size)
'''turtle.up()
turtle.goto(-500, 0)
turtle.down()
minkowski(3,10)
turtle.done()'''

def ice_fractal_1(n, size):
    if n == 0:
        turtle.fd(size)

    else:
        x = size
        print(x)
        ice_fractal_1(n - 1, x)
        turtle.lt(90)
        ice_fractal_1(n - 1, x/2)
        turtle.rt(180)
        ice_fractal_1(n - 1, x/2)
        turtle.rt(-90)
        ice_fractal_1(n - 1, x)
'''turtle.pu()
turtle.goto(-500, 0)
turtle.pd()
turtle.rt(0)
ice_fractal_1(5, 50)
turtle.done()'''

def ice_fractal_2(n, size):
    if n == 0:
        turtle.fd(size)

    else:
        x = size
        ice_fractal_2(n - 1, x)
        turtle.lt(120)
        ice_fractal_2(n - 1, x/2)
        turtle.lt(180)
        ice_fractal_2(n - 1, x/2)
        turtle.lt(120)
        ice_fractal_2(n - 1, x / 2)
        turtle.lt(180)
        ice_fractal_2(n - 1, x / 2)
        turtle.lt(120)
        ice_fractal_2(n - 1, x)
'''        
turtle.pu()
turtle.goto(0, 0)
turtle.pd()
turtle.rt(0)
ice_fractal_2(2, 50)
turtle.done()'''

def levi(n, size):
    x = size #чтобы чем больше была глуб.рекурсии, тем лучше вписывался рисунок в экран
    if n == 0:
        turtle.fd(x)
    elif n % 2 == 0:
        turtle.lt(45)
        levi(n-1, x)
        turtle.rt(45)
        levi(n - 1, x)
        turtle.lt(90)
    else:
        turtle.lt(45)
        levi(n-1, x)
        turtle.rt(90)
        levi(n - 1, x)

levi(8, 10)
turtle.done()

