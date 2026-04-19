# """
# Program to calculate Jerry's
# 3 rings' value
# Thursday September 25, 2025
# Created by Santiago Cuervo
# """

# User input (radii and cost)
radius_1 = float(input("Ring 1's radius: "))
radius_2 = float(input("Ring 2's radius: "))
radius_3 = float(input("Ring 3's radius: "))
pounds = float(input("Cost per square meter (£): "))

# Calculations (area)
area_1 = 3.14 * (radius_1**2)
area_2 = 3.14 * (radius_2**2)
area_3 = 3.14 * (radius_3**2)
total_area = area_1 + area_2 + area_3

# Cost calculation
cost = total_area * pounds

# Output (overall value)
print("Overall value of Jerry's rings = ", cost)