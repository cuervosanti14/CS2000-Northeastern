# """
# Program to the calculate area of
# a circle centered at point A and
# going through point B
# given 2 points
# Thursday September 25, 2025
# Created by Santiago Cuervo
# """

# User input for point A
x1 = float(input("X1: "))
y1 = float(input("Y1: "))

# User input for point B
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

# Calculating radius of the circle
radius = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** 0.5

# Calculating area of the circle
area = 3.14 * (radius ** 2)

# Printing output (area)
print("Area of circle = ", area)