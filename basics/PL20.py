i=float(input("Enter a number:"))
j=float(input("Enter another number:"))
print(i**j)
def power(x,y):
    r=1
    for i in range(y):
        r=r*x
    return r
print(power(2,3))
