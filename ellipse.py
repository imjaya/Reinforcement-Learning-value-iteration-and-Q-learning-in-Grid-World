import turtle
import math

def draw_circle(turtle, color, size, x, y):
    turtle.penup()
    turtle.color(color)
    turtle.fillcolor(color)
    turtle.goto(x,y)
    turtle.begin_fill()
    turtle.circle(size)
    turtle.end_fill()
    turtle.pendown()

tommy = turtle.Turtle()
tommy.shape("circle")
#tommy.speed(500)
i=10
#draw_circle(tommy, "green", 10, 25, 0)
while i<=360:
   draw_circle(tommy,"blue",10,25+(100*math.cos(0+i)),100+(100*math.sin(0+i))) 
   i=i+0.05
