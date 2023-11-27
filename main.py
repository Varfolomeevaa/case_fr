import turtle


def square(n):
    '''
    Function for drawing square
    :param n: size of side
    :return: None
    '''
    for _ in range(4):
        turtle.fd(n)
        turtle.rt(90)


def rec_square(n):
    '''
    Function for drawing rec_square
    :param n: depth of recursion
    :return: None
    '''
    if n <= 1:
        return None
    square(n)
    turtle.rt(10)
    turtle.penup()
    turtle.fd(0.1 * n)
    turtle.pendown()
    rec_square(0.9 * n)


def color_tree(depth, size):
    '''
    Function for drawing colorful tree
    :param depth: depth of recursion
    :param size: size of side
    :return: None
    '''
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


def branch(n, size):
    '''
    Function for drawing branch
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.lt(180)
        return

    x = size / (n + 1)
    for i in range(n):
        turtle.fd(x)
        turtle.lt(45)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.lt(90)
        branch(n - i - 1, 0.5 * x * (n - i - 1))
        turtle.rt(135)

    turtle.fd(x)
    turtle.lt(180)
    turtle.fd(size)


def koch(order, size):
    '''
    Function for drawing koch
    :param order: depth of recursion
    :param size: size of side
    :return: None
    '''
    if order == 0:
        turtle.fd(size)
    else:
        koch(order - 1, size / 3)
        turtle.lt(60)
        koch(order - 1, size / 3)
        turtle.rt(120)
        koch(order - 1, size / 3)
        turtle.lt(60)
        koch(order - 1, size / 3)


def koch_snow(n, x):
    '''
    Function for drawing
    :param n: depth of recursion
    :param x: size of side
    :return: None
    '''
    for i in range(3):
        koch(n, x)
        turtle.rt(120)


def minkowski(n, size):
    '''
    Function for drawing Minkowski line
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.fd(size)
    else:
        minkowski(n - 1, size)
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


def ice_fractal_1(n, size):
    '''
    Function for drawing the first ice fractal
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.fd(size)
    else:
        ice_fractal_1(n - 1, size)
        turtle.lt(90)
        ice_fractal_1(n - 1, size / 2)
        turtle.rt(180)
        ice_fractal_1(n - 1, size / 2)
        turtle.rt(-90)
        ice_fractal_1(n - 1, size)


def ice_fractal_2(n, size):
    '''
    Function for drawing the second ice fractal
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.fd(size)
    else:
        ice_fractal_2(n - 1, size)
        turtle.lt(120)
        ice_fractal_2(n - 1, size / 2)
        turtle.lt(180)
        ice_fractal_2(n - 1, size / 2)
        turtle.lt(120)
        ice_fractal_2(n - 1, size / 2)
        turtle.lt(180)
        ice_fractal_2(n - 1, size / 2)
        turtle.lt(120)
        ice_fractal_2(n - 1, size)


def levi(n, size):
    '''
    Function for drawing Levi line
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.fd(size)
    elif n % 2 == 0:
        turtle.lt(45)
        levi(n - 1, size)
        turtle.rt(45)
        levi(n - 1, size)
        turtle.lt(90)
    else:
        turtle.lt(45)
        levi(n - 1, size)
        turtle.rt(90)
        levi(n - 1, size)


def new_fractal_1(n, size):
    '''
    Function for drawing the first new fractal
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        for i in range(2):
            turtle.fd(size / 4)
            turtle.lt(90)
            turtle.fd(size / 4)
            turtle.rt(180)
            turtle.fd(size / 4)
            turtle.lt(90)
            turtle.fd(size / 4)
            turtle.rt(180)
    else:
        for i in range(3):
            ice_fractal_1(n, size / 2)
            new_fractal_1(n - 1, size)
            turtle.rt(120)


def new_fractal_2(n, size):
    '''
    Function for drawing the second new fractal
    :param n: depth of recursion
    :param size: size of side
    :return: None
    '''
    if n == 0:
        turtle.fd(size)
    else:
        for i in range(8):
            branch(n - 1, size)
            turtle.lt(360 / 8)


def main():
    print('Выберите фрактал:\n'
          '1.Рекурсивный квадрат\n'
          '2.Двоичное дерево\n'
          '3.Ветка\n'
          '4.Кривая Коха\n'
          '5.Снежинка Коха\n'
          '6.Кривая Минковского\n'
          '7.Ледяной фрактал №1\n'
          '8.Ледяной фрактал №2\n'
          '9.Кривая Леви\n'
          '10.Фрактал новый №1\n'
          '11.Фрактал новый №2\n')
    num_def = int(input('Введите номер:'))
    n = int(input('Введите глубину рекурсии:'))
    size = int(input('Введите длину стороны:'))
    turtle.speed(0)
    if num_def == 1:
        rec_square(size)
    elif num_def == 2:
        turtle.lt(90)
        color_tree(n, size)
    elif num_def == 3:
        turtle.up()
        turtle.goto(0, -100)
        turtle.left(90)
        turtle.down()
        branch(n, size)
    elif num_def == 4:
        turtle.up()
        turtle.goto(-100, 0)
        turtle.down()
        koch(n, size)
    elif num_def == 5:
        turtle.up()
        turtle.goto(-100, 0)
        turtle.down()
        koch_snow(n, size)
    elif num_def == 6:
        turtle.up()
        turtle.goto(-500, 0)
        turtle.down()
        minkowski(n, size)
    elif num_def == 7:
        turtle.up()
        turtle.goto(-500, 0)
        turtle.down()
        ice_fractal_1(n, size)
    elif num_def == 8:
        turtle.up()
        turtle.goto(-700, 0)
        turtle.down()
        ice_fractal_2(n, size)
    elif num_def == 9:
        levi(n, size)
    elif num_def == 10:
        new_fractal_1(n, size)
    elif num_def == 11:
        new_fractal_2(n, size)
    turtle.done()


main()
