# Infection data for 5 wards over 7 days
# Each inner list = infections for 1 day across 5 wards
infection_data = [
    [10, 12, 11, 0, 0],
    [15, 18, 16, 0, 0],
    [20, 24, 22, 0, 0],
    [25, 30, 27, 0, 0],
    [30, 36, 33, 0, 0],
    [35, 42, 38, 0, 0],
    [40, 48, 44, 0, 0]
]

# Create dependency manually:
# Ward4 = Ward1 + Ward2
# Ward5 = 2 * Ward3
for row in infection_data:
    row[3] = row[0] + row[1]
    row[4] = 2 * row[2]

# Print the data
print("Infection Data (Rows = Days, Columns = Wards):")
for row in infection_data:
    print(row)

# Function to check if two columns are linearly dependent
def is_dependent(col1, col2):
    """Checks if two columns are proportional (i.e., one is a multiple of the other)"""
    ratio = None
    for a, b in zip(col1, col2):
        if b == 0 and a == 0:
            continue
        elif b == 0 or a == 0:
            return False
        current_ratio = a / b
        if ratio is None:
            ratio = current_ratio
        elif abs(ratio - current_ratio) > 1e-6:
            return False
    return True

# Extract columns from data
columns = list(zip(*infection_data))

# Compare all wards
print("\nDependency check between wards:")
num_wards = len(columns)
dependent_pairs = []
for i in range(num_wards):
    for j in range(i + 1, num_wards):
        if is_dependent(columns[i], columns[j]):
            dependent_pairs.append((i + 1, j + 1))
            print(f"→ Ward {i+1} is dependent on Ward {j+1}")

if not dependent_pairs:
    print("→ No dependent wards found.")

# Approximate rank
rank = num_wards - len({ward for pair in dependent_pairs for ward in pair})
print(f"\nApproximate 'rank' (unique information sources): {rank} out of {num_wards}")
