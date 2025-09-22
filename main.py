#Name: Nysa Patel
#Date: 09/15/2025
#Project Name: Turtle Project

import turtle 
import math

t = turtle.Turtle()
#screen=turtle.Screen()
t.screen.tracer(0,0)

t.penup()
t.setx(-700) 
t.sety(400)

t.pendown()
t.shape("turtle") #characteristics of pen and turtle
t.color("lightgrey")
t.pensize(4)
t.speed(5)

def draw_rectangle(color, x, y, width, height): #all the parameters for the rectangle
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2): #draws the rectangle based on parameters
        t.forward(width)
        t.right(90)
        t.forward(height)
        t.right(90)
    t.end_fill()
    #t.penup()
draw_rectangle("skyblue", -900, 500, 1800, 1000) #to draw the sky light blue
draw_rectangle("tan", -900, -100, 1800, 500) # to draw the sand on the bottom half of screen 

#draw the sine line for the top part
amplitude = 40 #parameters for wave
frequency = 0.05
phase_shift = 10
t.pendown()
t.wave_height = 105
t.color("blue")
for x in range(-900, 900):
    y = t.wave_height + amplitude * math.sin(frequency * x + phase_shift) #draws the wave
    t.goto(x, y)

def fill_wave(amplitude, frequency, phase_shift, base_y): #fills in the sine wave 
    t.penup()
    t.goto(-900, base_y)
    t.pendown()
    t.color("deepskyblue")
    t.begin_fill()
    for x in range(-900, 901):
        y= base_y + amplitude * math.sin(frequency * x + phase_shift)
        t.goto(x, y)
        t.goto(900, -100) #fills in everything from the wave to sand in light blue
        t.goto(-900, -100)
        t.end_fill()
fill_wave(40, 0.05, 10, 100)

def draw_sun(x, y): #draws the sun
    t.penup()
    t.goto(x, y)
    t.pendown()
    for steps in range(40):
        for c in ('red', 'orange', 'yellow'): #different colors of the spiral
            t.color(c)
            t.forward(steps)
            t.right(30) #create spiral 
draw_sun(-700, 400)

umbrellas = int(input('Enter how many umbrellas you want: ')) #asks the user how many umbrellas and then displays that many

def umbrella_design(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.pencolor('red')
    t.pensize(3)
    
    start_pos = t.position()
    for i in range(100):
        t.circle(55,95) #sizing for the geometric design for the umbrella
        t.left(100)
    t.penup()
    t.goto(start_pos)
    t.pendown()

starting_x= -700 #where the umbrellas start from
starting_y=-200
spacing=100
edge = 1000

current_x = starting_x #created new variables so that they don't get mixed up in the if statement
current_y = starting_y

for i in range(umbrellas): #for loop to draw all the umbrellas
    t.hideturtle()
    umbrella_design(current_x, current_y)
    current_x+= spacing
    if current_x>edge : #when it touches the edge, shifts to next line
        current_x = -700
        current_y -=100

t.screen.update()
turtle.done()    # keep window open
