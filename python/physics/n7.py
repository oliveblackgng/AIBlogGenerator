import math
wl=float(input(print("enter wavelength of electron and photon (in m): ")))
c=3e8
h=6.625e-34
m=9.1e-31
e1=(h*c)/wl
e2=pow(h,2)/(2*m*pow(wl,2))
print("on comparision =",(e1/e2))

