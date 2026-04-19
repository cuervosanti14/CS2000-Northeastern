# """
# Program to find maximum value
# given 'N' amount of positive numbers
# Friday October 2, 2025
# Created by Santiago Cuervo
# """

# User input
num = int(input("Enter N: "))

# Set max to 0
max = 0

# For loop (user input, find max)
for i in range(num):
    x = int(input("Enter a positive number: "))
    # Special case (negative input)
    if x < 0:
        print("Error: must be positive")
    else:
        if x > max:
            max = x

# Output
print("Max = ", max)