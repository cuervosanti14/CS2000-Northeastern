# """
# Program to print A number of
# rows and B number of columns
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input
row = int(input("Enter rows: "))
col =  int(input("Enter columns: "))

# For loop (goes through number of rows)
for i in range(row):
    # For loop (goes through each column)
    for j in range(col):
        print("*", end = "")
    # Move to next line once loop finished
    print()