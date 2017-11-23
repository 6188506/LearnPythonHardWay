import turtle
import math
bob = turtle.Turtle()
print(bob)

def polygon(t, n, length):
	angle = 360.0/n
	for i in range(n):
		t.fd(length)
		t.lt(angle)

polygon(bob, n=8, length=70)


"""def circle(t, r):
	circumference = 2 * math.pi * r	
	n = int(circumference / 3) + 1
	length = circumference / n
	polygon(t, n, length)

circle(bob, 5)"""	

turtle.mainloop()


