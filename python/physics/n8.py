import math
v=float(input("enter velocity (in SI): "))
h=6.625e-34
m=float(input("enter mass (in SI): "))
a=float(input("enter accuracy percentage: "))
dv=(v*a)/100
dx=h/(4*math.pi*m*dv)
print("position: ",dx)