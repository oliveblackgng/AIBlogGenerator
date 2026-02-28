def quadra(n):
    return n*n*n*n # can be used instead of calling the fn
print(quadra(4))
mof=input("enter gender: ")
if mof=="male" or mof=="Male" or mof=="M" or mof=="MALE" :
    print("you are a male")
elif mof=="female" or mof=="Female" or mof=="F" or mof=="FEMALE" :
    print("you are a female")
else:
    print("you are an inter")