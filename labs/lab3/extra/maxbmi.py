# """
# Program to print out who has
# highest BMI and lowest BMI
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (heights, weights)
tom_height = float(input("Enter Tom's height: "))
tom_weight = float(input("Enter Tom's weight: "))
butch_height = float(input("Enter Butch's height: "))
butch_weight = float(input("Enter Butch's weight: "))
red_height = float(input("Enter Red's height: "))
red_weight = float(input("Enter Red's weight: "))

# Special case 1 (negative height)
if tom_height < 0 or butch_height < 0 or red_height < 0:
    print("Error: height can't be negative")
    quit()
# Special case 2 (negative weight)
if tom_weight < 0 or butch_weight < 0 or red_weight < 0:
    print("Error: weight can't be negative")
    quit()

# BMI calculations
tom_bmi = tom_weight / (tom_height ** 2)
butch_bmi = butch_weight / (butch_height ** 2)
red_bmi = red_weight / (red_height ** 2)

# If else (highest BMI)
if tom_bmi == max(tom_bmi,butch_bmi,red_bmi):
    print("Tom has the highest BMI")
elif butch_bmi == max(tom_bmi,butch_bmi,red_bmi):
    print("Butch has the highest BMI")
else:
    print("Red has the highest BMI")

# If else (lowest BMI)
if tom_bmi == min(tom_bmi,butch_bmi,red_bmi):
    print("Tom has the lowest BMI")
    quit()
if butch_bmi == min(tom_bmi,butch_bmi,red_bmi):
    print("Butch has the highest BMI")
    quit()
else:
    print("Red has the lowest BMI")
    quit()