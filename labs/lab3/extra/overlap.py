# """
# Program to check if
# 2 circles overlap or not
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input (circle's centers, radii)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
r1 = float(input("Enter radius 1: "))
r2 = float(input("Enter radius 2: "))

# Calculating distance between centers (x and y)
distance_x = abs(x1 - x2)
distance_y = abs(y1 - y2)

# If else (print if circles overlap or not)
if distance_x > r1 + r2 and distance_y > r1 + r2:
    print("Circles do not overlap")
else:
    print("Circles overlap")