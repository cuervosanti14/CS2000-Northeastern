# """
# Program to tell Tom if ring, square
# or triangle has largest area
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
r = float(input("Enter ring's radius: "))
x = float(input("Enter square's sides: "))
y = float(input("Enter triangle's sides: "))

# Area calculations
ring = 3.14 * (r ** 2)
square = x ** 2
triangle = ((3 ** 0.5) / 4) * (y ** 2)

# Nested if else to print output
if ring > square and ring > triangle:
    print("Ring has the greatest area")
elif square > ring and square > triangle:
    print("Square has the greatest area")
elif triangle > ring and triangle > square:
    print("Triangle has the greatest area")
else:
    print("2 or more shapes have the same area")