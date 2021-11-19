import math
n=int(input())
if n>0:
	x=math.sqrt(n)
else:
	print("enter positive value:")
if(x*x==float(n)):
	print("it is a perfect square")
else:
	print("it is non perfect square")

