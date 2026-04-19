# """
# Program to check if C
# is midpoint of A and B
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input (points)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

# If else (print if point 3 is midpoint or not)
if x3 == (x1 + x2) / 2 and y3 == (y1 + y2) / 2:
    print("Point 3 is the midpoint of the other 2 points")
else:
    print("Error: Point 3 is not the midpoint of the other 2 points")