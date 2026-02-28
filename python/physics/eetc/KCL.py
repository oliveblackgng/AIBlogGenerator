print("KCL Calculator (Enter + for entering, - for leaving)")

n = int(input("How many currents at the node? "))
total = 0

for i in range(n):
    total += float(input(f"Enter current #{i+1}: "))

print("\nTotal current sum:", total, "A")

if abs(total) < 1e-6:
    print("KCL VERIFIED")
else:
    print("KCL NOT VERIFIED")
