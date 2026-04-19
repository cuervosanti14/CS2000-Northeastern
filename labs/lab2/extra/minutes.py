# """
# Program to convert minutes
# to seconds, hours, and days
# Friday September 26, 2025
# Created by Santiago Cuervo
# """

# User input (minutes)
minutes = int(input("Enter # of minutes: "))

# Calculation (seconds, hours, days)
seconds = minutes * 60
hours = minutes / 60
days = hours / 24

# Print output (calculations)
print("Seconds = ", seconds, "\nHours = ", hours, "\nDays = ", days)