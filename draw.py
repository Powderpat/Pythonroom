# author: Powderpat

import turtle

carlos = turtle.Turtle()

n = 6
length = 100
angle = 180 - 180 * (n - 2) / n
#numbers = range(0, n)
colors = [ "red", "yellow", "orange", "green", "magenta", "blue"]

yash = turtle.Turtle()

for color in colors:
	carlos.color(color)
	carlos.forward(length)
	carlos.left(angle)
	