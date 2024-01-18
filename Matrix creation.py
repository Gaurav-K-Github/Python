import numpy as np

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Create an empty matrix of the specified dimensions
matrix = np.zeros((rows, cols))

# Prompt the user to enter the elements of the matrix
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = float(input(f"Enter the element at position ({i+1}, {j+1}): "))

# Print the matrix
print("The matrix you entered is:")
print(matrix)
