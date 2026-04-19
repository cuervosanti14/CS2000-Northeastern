# """
# Program to check if point is
# inside, on, or outside a circle
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (circle center, radius, point)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
r1 = float(input("Enter radius: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# If else (print whether point is outside, inside, or on circle)
if (x2 < x1 - r1 or x2 > x1 + r1) and (y2 < y1 - r1 or y2 > y1 + r1):
    print("Point is outside of circle")
elif (x1 - r1 < x2 < x1 + r1) and (y1 - r1 < y2 < y1 + r1):
    print("Point is inside of circle")
else:
    print("Point is on the circle")