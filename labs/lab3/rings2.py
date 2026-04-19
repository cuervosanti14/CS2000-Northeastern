# """
# Program to calculate area and weight of
# each ring, then find max weight of 3 rings
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (radii)
radius1 = float(input("Radius 1: "))
radius2 = float(input("Radius 2: "))
radius3 = float(input("Radius 3: "))

# Special case (negative radius)
if radius1 < 0 or radius2 < 0 or radius3 < 0:
    print("Error: radius can't be negative")
    quit()

# Area calculations
area1 = 3.14 * (radius1 ** 2)
area2 = 3.14 * (radius2 ** 2)
area3 = 3.14 * (radius3 ** 2)

# Weight calculations
weight1 = 2 * area1
weight2 = 2 * area2
weight3 = 2 * area3

# If else (print ring with max weight and value)
if weight1 == max(weight1,weight2,weight3):
    print("Ring 1 has max weight of 3 rings: ", max(weight1,weight2,weight3))
elif weight2 == max(weight1,weight2,weight3):
    print("Ring 2 has max weight of 3 rings: ", max(weight1,weight2,weight3))
elif weight3 == max(weight1,weight2,weight3):
    print("Ring 3 has max weight of 3 rings: ", max(weight1,weight2,weight3))