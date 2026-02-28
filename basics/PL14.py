
def max(n1,n2,n3):

    if n1>n2 and n1>n3:
        print(f"n1 is the greatest")
    elif n2>n1 and n2>n3: # else if
        print(f"n2 is the greatest")
    else:
        print(f"n3 is the greatest")
print(max(1,2,3))