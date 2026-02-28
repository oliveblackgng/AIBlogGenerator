name=input("Enter you name: ")
print("Hey " +name+ "!")
n1= input("Enter a decimal number: ")
n2=input("Enter an integer: ")
s=float(n1) + int(n2)
p=float(n1)*int(n2)
print("product: "+str(p)+ "\nsum:"+str(s))
friends=["Rachel", "Monica", "Phoebe", "Chandler", "Ross", "Joey"]
friends.append("janice") # adds it as the last index in the array
friends.remove("Phoebe") # removes it from the array
friends.insert(2,"richard")
i=input("Enter a number from 0 to 6: ") # the inputed value is accepted as string too
print(friends[int(i)])
print(friends[0:5]) # prints all values from the index '0' to '5'
friends.clear() # clears all the array values/makes the array empty
