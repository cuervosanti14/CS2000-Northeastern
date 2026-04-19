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
    Output: return area
    """
    # Calculate area
    a = w * h
    return a

# User input for n amount of rectangles
n = int(input("Enter n: "))
# Initialize variable
sum = 0
# For loop for width + height input
for i in range(n):
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    # Call to function & add to sum if area > 50
    a = calculate_area(w,h)
    if a > 50:
        sum = sum + a

# Output: print total area (sum)
print("Total area of rectangles whose areas are > 50 = ", sum)