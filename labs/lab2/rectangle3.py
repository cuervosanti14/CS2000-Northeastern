# """
# Program to calculate area + perimeter
# of rectangle created by 2 points
# Thursday September 25, 2025
# Created by Santiago Cuervo
# """

# User input for point 1
x1 = float(input("X1: "))
y1 = float(input("Y1: "))

 # User input for point 2
x2 = float(input("X2: "))
y2 = float(input("Y2: "))

# Check if x2 and y2 > 1 and y1
if x2 > x1 and y2 > y1:
    pass
# If not, print error message and quit
else:
    print("Error: x2 must be > x1 and y2 must be > y1")
    quit()

# Calculate length and width of rectangle
side1 = x2 - x1
side2 = y2 - y1

# Calculate area and perimeter of rectangle
perimeter = (2 * side1) + (2 * side2)
area = side1 * side2

# Print output (area and perimeter)
print("Area = ", area, "Perimeter = ", perimeter)