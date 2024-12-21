import turtle
turtle.Screen().bgcolor("#D21043")
turtle.Screen().setup(400,400)
pollygone = turtle.Turtle()
six = 9
lenngth = 70
angle = 360/six
for g in range(six):
    pollygone.forward(lenngth)
    pollygone.left(angle)

turtle.done()