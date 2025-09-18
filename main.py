#Name: Nysa Patel
#Date: 09/15/2025
#Project Name: Turtle Project

import turtle
import math

t = turtle.Turtle()

t.penup()
t.setx(-700)
t.sety(400) #turtle position(fix how it shows the line before)

t.pendown()
t.shape("turtle")
t.color("lightgrey")
t.pensize(4)
t.speed(5)

for steps in range(40):
    for c in ('red', 'orange', 'yellow'):
        t.color(c)
        t.forward(steps)
        t.right(30) #create spiral

t.penup()
t.goto(-200,-150)

amplitude = 40
frequency = 0.05
phase_shift = 0
t.pendown()
t.color("blue")
for x in range(-900, 900):
    y = amplitude * math.sin(frequency * x + phase_shift)
    t.goto(x, y)

turtle.done()    # keep window open