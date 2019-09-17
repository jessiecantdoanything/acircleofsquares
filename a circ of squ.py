import turtle
turtle.shape("turtle")
turtle.color("Dark Slate Blue")
turtle.bgcolor("Lavender")

def square():
    for i in range(4):
        turtle.forward(100)
        turtle.right(90)

def squarecircle():
    for i in range(60):
        square()
        turtle.right(5)

turtle.speed(.5)
squarecircle()


turtle.exitonclick()