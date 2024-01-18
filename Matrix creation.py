import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

matrix = np.zeros((rows, cols))

for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Enter the element at position ({i+1}, {j+1}): "))

# Print the matrix
print("The matrix you entered is:")
print(matrix)
