# """
# Program to find number of pythagorean
# triples where max (a,b,c) <= 1000
# Pythagorean: a * a = b * b + c * c
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# Set to 0
count = 0

# Nested for loop to check all possible variations
for a in range(1, 1001):
    for b in range (1, a+1):
        for c in range (1, b+1):
            # Check if a pythagorean triple
            if a * a == b * b + c * c:
                count = count + 1

# Output
print("Number of pythagorean triples where max(a,b,c) <= 1000: ", count)