import math
h=6.625e-34
Eg=5.6e-3
l=int(input("Enter by how much the width of the well is increased: "))
En=Eg/math.pow(l,2)
print("Therefore, the energy decreases to: "+str(En)+" eV")