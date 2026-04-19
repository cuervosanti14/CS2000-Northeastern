# """
# Program to calculate area of cheese that
# Tom decides to give Jerry (1/2 of total area)
# Thursday October 16, 2025
# Created by Santiago Cuervo
# """

# Function 1 (get shape and radius, calculate
# area of hole based on shape, return area)
def hole_area(hole_type, r):
    """
    Input: hole type and radius
    Behavior: calculate area of hole based on shape
    Output: return area of hole
    """
    # Calculate circle OR square hole area
    if hole_type == "circle":
        return 3.14 * r ** 2
    elif hole_type == "square":
        return (2 * r) ** 2

# Function 2 (get width, height, amd number of holes in
# order to calculate and return cheese's area)
def jerrys_cheese(w, h, n):
    """
    Input: width, height, number of holes
    Behavior: calculate cheese's area
    Output: return cheese's area
    """
    # Calculate total area
    total_area = w * h
    # Initialize variable
    holes_area = 0
    # For loop (get type of hole)
    for i in range(n):
        # While + if else loop to ensure proper input
        while True:
            # User input for hole type
            hole_type = input("Enter type of hole (circle OR square): ")
            # Special case (improper input)
            if hole_type == "circle" or hole_type == "square":
                break
            else:
                print("Error: only circle and square holes allowed")
        # User input for radius
        r = float(input("Enter radius: "))
        # Hole's area calculations
        holes_area += hole_area(hole_type, r)
    # Cheese's area calculations
    cheese_area = total_area - holes_area
    # Special case (cheese's area is negative_
    if cheese_area < 0:
        print("Error: total area of cheese is negative!")
        return 0
    # Return jerry's half of cheese's area
    return cheese_area / 2

# User input for width, height, and n amount of holes
w = float(input("Enter cheese's width: "))
h = float(input("Enter cheese's height: "))
n = int(input("Enter number of holes: "))

# Output (Jerry cheese's area)
print("The cheese Tom gives Jerry has an area of =", jerrys_cheese(w, h, n))