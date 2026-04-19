# """
# Program to check if a, b, and c
# form a good set or not
# (if 1 number = the sum of the other 2)
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (3 numbers)
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

# If else (determine good set or not)
if a + b == c or b + c == a or a + c == b:
    print("These numbers are a good set")
else:
    print("These numbers are not a good set")