i=int(input("Enter a number from 0 to 3: "))
j=int(input("Enter a number from 0 to 3: "))
number_grid = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[i][j])
n="like matrix: ith row and jth column"
for row in number_grid:
    print(row)
for row in number_grid:
    for col in row:
        print(col)