o=open("n.txt","r")

for line in o.readlines():
    print(line)
print(o.readable())
print(o.readline())
o.close()
