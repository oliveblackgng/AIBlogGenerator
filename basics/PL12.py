tall=True # boolean value
g=input("enter your gender (M OR F): ")
if (g=="M"):
    print("you are a short male")
elif not (g=="M") and tall:
    print("you are a tall female")
else:
    print("not tall female nor short male")
