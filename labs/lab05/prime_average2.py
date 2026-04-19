# """
# Program to enter n different positive
# numbers and calculate average value of
# all prime numbers among them
# Wednesday October 15, 2025
# Created by Santiago Cuervo
# """

# Function (return true if x is prime, false if not)
def is_prime(x):
    """
    Input: x (number)
    Behavior: check if x is prime or not
    Output: return True or False
    """
    # Check if x is prime or not
    if n < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

# User input for n amount of numbers
n = int(input("Enter n: "))

# Initialize variables
sum = 0
count = 0

# Nested for loop
for i in range(n):
    # User input for x
    x = int(input("Enter x: "))
    # Special case (non-positive input)
    if x < 1:
        print("Error: not a number > 0")

    # If statement (if x is prime, add x to sum and increase count)
    if is_prime(x):
        sum += x
        count += 1

# Special case (no prime #s)
if sum == 0:
    print("There are no prime numbers")
    quit()

# Output (avg of all primes)
print("Average of all prime numbers = ", sum / count)