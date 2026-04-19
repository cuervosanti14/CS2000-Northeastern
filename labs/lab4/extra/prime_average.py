# """
# Program to enter n different positive
# numbers and calculate average value of
# all prime numbers among them
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
n = int(input("Enter n: "))

# Set to 0
sum = 0
count = 0

# Nested for loop
for i in range(n):
    # User input
    x = int(input("Enter x: "))
    # Is prime function
    is_prime = True
    # For loop to check if x is prime #
    for j in range(2,x):
        if x % j == 0:
            is_prime = False
            break
    # Adding primes to sum + count
    if is_prime == True:
        sum = sum + x
        count = count + 1

# Special case (no prime #s)
if sum == 0:
    print("There are no prime numbers")
    quit()

# Output
print("Average of all prime numbers = ", sum / count)