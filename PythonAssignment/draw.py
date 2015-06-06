import turtle

def drawSquare():
    window=turtle.Screen()
    window.bgcolor("brown")



    brad=turtle.Turtle()
    brad.shape('arrow')
    brad.speed(1)
    brad.color("white")
 
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    window.exitonclick()

drawSquare()
