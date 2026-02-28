print("KVL Calculator (Enter + for rise, - for drop)")

n = int(input("How many voltages in the loop? "))
total = 0

for i in range(n):
    total += float(input(f"Enter voltage #{i+1}: "))

print("\nTotal loop voltage:", total, "V")

if abs(total) < 1e-6:
    print("KVL VERIFIED")
else:
    print("KVL NOT VERIFIED")