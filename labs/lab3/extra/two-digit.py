# """
# Program to check if 2 digit number
# satisifes condition of adding up to 9
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input (number)
number = int(input("Enter two-digit number: "))

# Special case (number inputted is negative OR not 2-digits)
if number < 10 or number > 99:
    print("Error: number is not 2 digits")
    quit()

# Using floor divison + remainer to get digit 1 and 2
digit1 = number // 10
digit2 = number % 10

# Checking if number satisifies condition + printing output
if digit1 + digit2 == 9:
    print("Number satisifies condition")
else:
    print("Number does not satisfy condition")