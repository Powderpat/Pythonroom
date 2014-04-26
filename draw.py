# author: Powderpat

import turtle

carlos = turtle.Turtle()

n = 50
t = 30
length = 1	
angle = 30
numbers = range(0, n)


for number in numbers:
	
	carlos.forward(length)
	carlos.left(angle)
	length = length + 2
	if length > 150:
		length = 0
		
	
	