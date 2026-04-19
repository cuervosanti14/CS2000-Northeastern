# """
# Program to find manhattan
# distance between 2 points
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (points)
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Manhattan distance formula
distance = abs(x1 - x2) + abs(y1 - y2)

# Output (manhattan distance)
print("Manhattan distance = ", distance)