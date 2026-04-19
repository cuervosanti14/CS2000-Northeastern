# """
# Program to calculate avg temp. in his house in
# Celsius for N consecutive days given the temp.
# in degrees Fahrenheit
# Thursday October 16, 2025
# Created by Santiago Cuervo
# """

# Function (take in Fahrenheit, calculate Celsius, and return it)
def fahrenheit_to_celsius(f):
    """
    Input: degrees Fahrenheit
    Behavior: calculate degrees Celsius
    Output: return Celsius
    """
    # Calculating celsius
    c = ((5 / 9) * (f - 32))
    return c

# User input for n consecutive days
n = int(input("Enter n: "))

# Initialize variables
count = 0
sum = 0

# For loop (user input for Fahrenheit, add to sum, increase count)
for i in range(n):
    f = float(input("Enter degrees Fahrenheit: "))
    sum += fahrenheit_to_celsius(f)
    count += 1

# Output (avg. temp in degrees Celsius)
print("Average temp. in his house in Celsius = ", sum / count)