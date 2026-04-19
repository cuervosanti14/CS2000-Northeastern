# """
# Program to calculate bonus of
# Scrooge's employees
# Wednesday October 14, 2025
# Created by Santiago Cuervo
# """

# Function (calculate bonus based on age)
def calculate_bonus(age):
    """
    Input: age
    Behavior: calculate bonus based on age
    Output: return bonus
    """
    # Nested if else (bonus based on age)
    if age < 30:
        bonus = 0.1 * salary
    elif age < 40:
        bonus = 0.2 * salary
    elif age < 50:
        bonus = 0.3 * salary
    else:
        bonus = 0.4 * salary
    return bonus

# User input for n amount of employees
n = int(input("Enter n: "))
# Initialize variable
total = 0

# For loop (user input for salary + age)
for i in range(n):
    salary = float(input("Enter employee's salary: "))
    age = int(input("Enter employee's age: "))
    # Call to function to calculate total bonus
    total += calculate_bonus(age)

# Output (total bonus)
print("Total bonus for Scrooge's employees = ", total)