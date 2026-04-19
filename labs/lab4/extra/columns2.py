# """
# Program to print out a matrix
# with 'n' rows and 'm' columns
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input
row = int(input("Enter rows: "))
col = int(input("Enter columns: "))

# For loop (check rows)
for i in range(row):
    # For loop (check columns)
    for j in range (col):
        # Check if rows + columns is even or odd to determine character
        if (i + j) % 2 == 0:
            print("*", end = " ")
        else:
            print("+", end = " ")
    # Move to next line once loop finished
    print()