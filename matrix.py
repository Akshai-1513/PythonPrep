n = int(input("Enter the value of n: "))
m = int(input("Enter the value of m: "))

matrix1 = []
print("Enter the values of matrix1:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input())) # get the input from the user 
    matrix1.append(row) # Add the value to the array

matrix2 = []
print("Enter the values of matrix2:")
for i in range(n):
    row = []
    for j in range(m):
        row.append(int(input()))
    matrix2.append(row)

matrix = [[0 for _ in range(m)] for _ in range(n)] # This will create a matrix with the values of 0

print("Matrix Addition:")
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix1[i][j] + matrix2[i][j] # Add the two matrix
        print(matrix[i][j], end=" ") # end command will leavee some space
    print()

print("Matrix Subtraction:")
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix1[i][j] - matrix2[i][j] # Sub the matrix
        print(matrix[i][j], end=" ")
    print()  

print("Matrix Multiplication:")
for i in range(n):
    for j in range(m):
        matrix[i][j] = matrix1[i][j] * matrix2[i][j] # multiply the two matrix
        print(matrix[i][j], end=" ")
    print()  
