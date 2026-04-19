# """
# Program to find how
# many good rings Marie has
# Friday October 2, 2025
# Created by Santiago Cuervo
# """

# User input
num = int(input("Enter number of rings: "))

# Set total to 0
total = 0

# For loop (radius input + area calculation)
for i in range(num):
    r = int(input("Enter radius of ring: "))
    area = 3.14 * (r ** 2)
    if area > 99:
        total = total + 1

# Output
print("Marie's number of good rings = ", total)