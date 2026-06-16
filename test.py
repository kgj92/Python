import turtle
t = turtle.Turtle()

def f():
    t.forwrad(100)
    t.left(90)

def h():
    f(),f(),f(),f()
    t.right()

c = ["green", "yellow", "blue", "red"]
for color in c:
    t.color("blue", color)
    t.begin_fill()
    h()
    t.end_fill()