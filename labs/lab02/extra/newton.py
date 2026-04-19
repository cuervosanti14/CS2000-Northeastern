# """
# Program to calculate
# Newton's law of gravitation
# Friday September 26, 2025
# Created by Santiago Cuervo
# """

# User input (and gravitational constant)
mass1 = float(input("Enter mass of object 1: "))
mass2 = float(input("Enter mass of object 2: "))
distance = float(input("Enter distance between center of the masses: "))
gravity_constant = 6.674 * (10 ** -11)

# Calculation (formula)
force = gravity_constant * ((mass1 * mass2) / (distance ** 2))

# Print output (force)
print("Force = ", force)