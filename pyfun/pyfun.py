import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")
h = 0

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    t.color(c)
    t.forward(i * 3 / 5 + i)
    t.left(59)
    t.circle(60)
    h += 0.005

turtle.done
