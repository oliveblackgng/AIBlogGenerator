print("conversion of (1)km/h to m/s or (2)vice-versa?")
o=int(input(print("(1) or (2)? \n")))
if o == 1:
    v=float(input("enter the velocity:"))
    v=(v*5)/18
    print("velocity in m/s =",v)
elif o == 2:
    v=float(input("enter the velocity:"))
    v=(v*18)/5
    print("velocity in km/h =",v)
else:
    print("wrong input")


