# """
# Program to enter width + height of N
# rectangles + get sum of how many's area > 50
# Wednesday October 14, 2025
# Created by Santiago Cuervo
# """

# Function (calculate area based on width + height)
def calculate_area(w,h):
    """
    Input: width + height
    Behavior: calculate area based on width + height
    Output: area > 50 return a, if not return 0
    """
    # Calculate area
    a = w * h
    # If statement (return value based on area)
    if a > 50:
        return a
    else:
        return 0

# User input for n amount of rectangles
n = int(input("Enter n: "))
# Initialize variable
sum = 0
# For loop for width + height input
for i in range(n):
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    # Call to function & add to sum
    sum += calculate_area(w,h)

# Output: print total area (sum)
print("Total area of rectangles whose areas are > 50 = ", sum)