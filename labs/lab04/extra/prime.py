# """
# Program to enter positive number n
# and print out if n is prime or not
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
n = int(input("Enter n: "))

# Is prime function
is_prime = True

# For loop to check if prime or not
for i in range(2,n):
    if n % i == 0:
        is_prime = False

# If else to print if is prime or not
if is_prime == False:
    print(n, "is not a prime number")
else:
    print(n, "is a prime number")