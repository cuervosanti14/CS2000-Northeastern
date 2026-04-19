# """
# Program to enter width + height of N
# rectangles + get avg area of rectangles
# whose perimeters > 50
# Wednesday October 14, 2025
# Created by Santiago Cuervo
# """

# Function 1 (calculate area based on width + height)
def calculate_area(w,h):
    """
    Input: width + height
    Behavior: calculate area based on width + height
    Output: return area
    """
    # Calculate area
    a = w * h
    return a

# Function 2 (calculate perimeter based on width + height)
def calculate_perimeter(w,h):
    """
    Input: width + height
    Behavior: calculate perimeter based on width + height
    Output: return perimeter
    """
    # Calculate perimeter
    p = 2 * w + 2 * h
    return p

# User input for n amount of rectangles
n = int(input("Enter n: "))
# Initialize variable
sum = 0
count = 0
# For loop for width + height input
for i in range(n):
    w = float(input("Enter width: "))
    h = float(input("Enter height: "))
    # Call to functions
    a = calculate_area(w,h)
    p = calculate_perimeter(w,h)
    # If perimeter > 50, add area to sum and increase count by 1
    if p > 50:
        sum = sum + a
        count += 1

# Special case
if count == 0:
    print("No rectangles have perimeter > 50")
    quit()

# Output: print avg area (sum / count)
print("Avg area of rectangles whose perimeters are > 50 = ", sum / count)