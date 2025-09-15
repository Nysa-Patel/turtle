#Name: Nysa Patel
#Date: 09/15/2025
#Project Name: Turtle Project


import turtle

t = turtle.Turtle()
turtle.hideturtle()
t.setx(-300)
t.sety(300) #turtle position(fix how it shows the line before)

turtle.showturtle()
t.shape("turtle")
t.color("lightgrey")
t.pensize(4)
t.speed(5)

for steps in range(45):
    for c in ('red', 'orange', 'yellow'):
        t.color(c)
        t.forward(steps)
        t.right(30) #create spiral


"""
for i in range(4):
    t.forward(100)
    t.right(90)
    """


turtle.done()    # keep window open