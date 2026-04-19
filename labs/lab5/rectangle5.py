# """
# Program to enter width + height of N
# rectangles + count how many's area > 50
# Tuesday October 14, 2025
# Created by Santiago Cuervo
# """

# Function: determine if rectangle's area > 50
def check_rectangle_area(w,h):
    """
    Input: width + height
    Behavior: calculate area based on width + height
    Output: area > 50 or not
    """
    # Calculate area
    a = w * h
    # Return true if area > 50 and false if not
    if a > 50:
        return True
    else:
        return False

# User input for n amount of rectangles
n = int(input("Enter n: "))
# Initialize variable
count = 0
# For loop for width + height input
for i in range(n):
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    # If statement: increase count if rectangle's area > 50
    if check_rectangle_area(w,h) == True:
        count += 1

# Output: print # of rectangles w/ area > 50
print("# of rectangles with area > 50 = ", count)