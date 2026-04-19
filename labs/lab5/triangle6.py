# """
# Program to enter coordinates of 3 points
# and check if they can form a triangle
# Wednesday October 15, 2025
# Created by Santiago Cuervo
# """

def check_triangle(x1, y1, x2, y2, x3, y3):
    """
    Input: 3 points (x,y)
    Behavior: calculate Euclidian distance between each point
    Output: return if all 2 side combinations > leftover
            side, meaning can form a triangle
    """
    # Euclidian distance calculations
    d1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    d2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5
    d3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5
    # True or false based on distance (form triangle or not)
    if d1 + d2 > d3 and d1 + d3 > d2 and d2 + d3 > d1:
        return True
    else:
        return False

# User input for 3 coordinates
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))
x3 = float(input("Enter x3: "))
y3 = float(input("Enter y3: "))

# If else to print output (can / can't form triangle)
# Call to function
if check_triangle(x1, y1, x2, y2, x3, y3):
    print("These 3 coordinates can form a triangle")
else:
    print("These 3 coordinates cannot form a triangle")