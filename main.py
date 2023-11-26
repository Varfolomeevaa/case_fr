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
    turtle.fd(0.1*n)
    turtle.pendown()
    return rec_square(0.9*n)

rec_square(100)