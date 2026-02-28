import math
E=float(input(print("enter kinetic energy in eV: ")))
E=E*1.6e-19
m=9.1e-31
h=6.625e-34
wl=h/(math.sqrt(2*m*E))
print("wavelength =",wl)

