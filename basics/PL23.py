try:
    i=int(input("Enter an integer: "))
    print(i)
    v = 10 / 0
except ValueError:
    print("you did not enter an integer")
except ZeroDivisionError as e:
    print(e)
