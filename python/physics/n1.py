s= str(input("what do you need to find? (wavelength, velocity or mass ?) : ")).lower()
l=m=v=float()
if s == "wavelength":
    v=float(input("enter velocity (in SI): "))
    m = float(input("enter mass (in SI): "))
    l=(6.6e-34)/(m*v)
    print("wavelength =",l)
elif s == "velocity":
    m = float(input("enter mass (in SI): "))
    l = float(input("enter wavelength (in SI): "))
    v=(6.6e-34)/(l*m)
    print("velocity =",v)
elif s == "mass":
    v = float(input("enter velocity (in SI): "))
    l = float(input("enter wavelength (in SI): "))
    m=(6.6e-34)/(l*v)
    print("mass =",m)
else:
    print("this only solves numericals using λ=h/(mv)")

