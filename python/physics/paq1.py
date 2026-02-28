import math
h=6.625e-34
m=9.1e-31
e=1.6e-19
v=float(input("Enter Voltage (in V): \n "))
l=h/math.sqrt(2*m*e*v)
print("The de-Broglie wavelength: \n"+str(l)+"λ")
