# """
# Program to calculate perimeter
# and area of equilateral triangle
# Friday September 26, 2025
# Created by Santiago Cuervo
# """

# User input (first side)
side1 = float(input("Enter side 1 length: "))

# Set all 3 sides of triangle equal to each other
side2 = side1
side3 = side1

# Calculate height of the triangle (and print)
height = ((side1 ** 2) + (side2 ** 2)) ** 0.5
print("Height = ", height)

# Calculate perimeter and area of the triangle
perimeter = side1 + side2 + side3
area = side1 * height

# Print output (perimeter and area)
print("Perimeter = ", perimeter, "\nArea = ", area)