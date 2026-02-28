sw="cat"
gw=""
i=0
while sw!=gw:
    i+=1
    if i<=3:
        gw=input()
        if sw==gw:
            print("you win!")
    else:
        print("you lose!")
        break
