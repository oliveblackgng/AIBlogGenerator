a,b,c=input("enter two numbers: ").split(",")
a=int(a)
b=int(b)
c=int(c)
if a>b and a>c:
    print(a,"is greater than" ,b,"and",c)
elif a<b and a<c:
    print(a,"is less than",b,"and",c)
else:
    print(a,"is equal to",b,"and",c)
