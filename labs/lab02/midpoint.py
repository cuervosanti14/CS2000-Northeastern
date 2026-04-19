# """
# Program to calculate midpoint
# given 2 points
# Thursday September 25, 2025
# Created by Santiago Cuervo
# """

# User input for point 1
x1 = float(input("X1: "))
y1 = float(input("Y1: "))

# User input for point 2
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

# Calculate x and y for midpoint
x3 = (x1 + x2) / 2
y3 = (y1 + y2) / 2

# Print output (midpoint)
print("Midpoint = ", (x3, y3))