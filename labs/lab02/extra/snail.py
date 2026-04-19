# """
# Program to calculate how many
# days the snail needs to reach
# the top of the pole
# Friday September 26, 2025
# Created by Santiago Cuervo
# """

# User input (height, climb, descent)
pole = float(input("Enter pole's height (meters): "))
climb = float(input("Enter snail's climb (meters): "))
descent = float(input("Enter snail's descent (meters): "))

# Check if climb > descend
if climb > descent:
    pass
# If not, print error message and quit
else:
    print("Error: snail's daily climb must be greater than its daily descend")
    quit()

# Calculation for days it takes the snail to reach top
days = pole / (climb - descent)

# Print output (time taken in days)
print("To get to the top, the snail needs:", days, "days")