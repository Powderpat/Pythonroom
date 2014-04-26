# author: Powderpat

import turtle

carlos = turtle.Turtle()

n = 50

length = 50	
angle = 90
numbers = range(0, 100, 2)
colors = ["blue", "red", "yellow", "green"]

for number in numbers:
	for color in colors:
		carlos.color(color)
		carlos.forward(length)
		carlos.left(angle)
		length = length + 2
		
	
	