print("enter 3 number: ")
i=1
while i<=3:
    if i==1:
        j1=float(input())
    if i==2:
        j2=float(input())
    if i==3:
        j3=float(input())
    i+=1
O=input("Enter an operator: ")
if O == "+":
    print(j1+j2+j3)
elif O == "-":
    print(j1-j2-j3)
elif O == "*":
    print(j1*j2*j3)
elif O == "/":
    print(j1/j2/j3)
else:
    print("this is a simple calculator")