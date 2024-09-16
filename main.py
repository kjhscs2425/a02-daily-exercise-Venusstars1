import turtle

turtle.left(180)
side=200
for i in range(12):
    turtle.forward(side)
    turtle.left(90)
    side= side - 15

turtle.exitonclick()