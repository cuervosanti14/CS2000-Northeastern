# """
# Program to calculate area of
# cheese that Tom should have
# Friday September 26, 2025
# Created by Santiago Cuervo
# """

# User input (sides, diameters)
sideA = float(input("Enter side A length: "))
sideB = float(input("Enter side B length: "))
diameterC = float(input("Enter diameter of circle C: "))
diameterD = float(input("Enter diameter of circle D: "))

# Calculations (areas)
rectangle_area = sideA * sideB
circle_C_area =  3.14 * ((diameterC/2) ** 2)
circle_D_area = 3.14 * ((diameterD/2) ** 2)

# Calculation (area of half of cheese)
cheese = (rectangle_area - circle_C_area - circle_D_area) / 2

# Print area of cheese Tom should have
print("Tom should have this amount of cheese: ", cheese)