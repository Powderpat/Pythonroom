# author: Powderpat

import turtle

carlos = turtle.Turtle()

n = 5
length = 50
angle = 180 - 180 * (n - 2) / n
numbers = range(0, n)

for number in numbers:
	carlos.forward(length)
	carlos.left(angle)
