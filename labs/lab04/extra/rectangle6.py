# """
# Program to enter an integer and
# print out a rectangle pattern 2
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
a = int(input("Enter a: "))

# Nested for loop
for i in range(a):
    # For loop for + in each line
    for j in range(i + 1):
        print("+", end = " ")
    # For loop for * in each line
    for k in range(a - i - 1):
        print('*', end = " ")
    print()