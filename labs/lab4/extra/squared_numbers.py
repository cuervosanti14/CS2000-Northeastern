# """
# Program to find number of 3 digit
# numbers that are square
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# Set to 0
count = 0

# For loop (smallest 3-digit square is 100 (10) and largest is 961 (31))
for i in range(10, 32):
    square = i ** 2
    # Add square numbers to total
    if 99 < square < 1000:
        count = count + 1

# Output
print(count, "3-digit numbers are squares")