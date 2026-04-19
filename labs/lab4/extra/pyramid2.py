# """
# Program to enter an integer and
# print out a triangle pattern 2
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
n = int(input("Enter n: "))

# Nested loop to print top half
for i in range(n):
    for j in range(i + 1):
        print("+", end = " ")
    print()

# Nested for loop to print bottom half
for i in range(n):
    for j in range(n - i - 1):
        print("+", end = " ")
    print()