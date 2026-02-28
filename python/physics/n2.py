import math
s= str(input("what do you need to find? (wavelength, kinetic energy or mass ?) : ")).lower()
l=m=v=k=float()
if s == "wavelength":
    v=float(input("enter velocity (in SI): "))
    m = float(input("enter mass (in SI): "))
    l=(6.6e-34)/(m*v)
    print("wavelength =",l)
elif s == "kinetic energy":
    m = float(input("enter mass (in SI): "))
    l = float(input("enter wavelength (in SI): "))
    k=pow((6.6e-34),2)/2*m*(pow(l,2))
    print("kinetic energy =",k)
elif s == "mass":
    v = float(input("enter velocity (in SI): "))
    l = float(input("enter wavelength (in SI): "))
    m=(6.6e-34)/(l*v)
    print("mass =",m)
else:
    print("this only solves numericals using λ=h/(2mEĸ)")