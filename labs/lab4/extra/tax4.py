# """
# Program to help Scrooge calculate the
# averaged tax for all his female employees
# Thursday October 9, 2025
# Created by Santiago Cuervo
# """

# User input
n = int(input("Enter number of Scrooge's employees: "))

# Set to 0
total = 0
count = 0

# For loop for each employee's details
for i in range(n):
    name = input("Enter employee's name: ")
    gender = int(input("Enter 0 for female, 1 for male: "))
    salary = float(input("Enter employee's salary: "))

    # Special case 1 (gender incorrectly inputted)
    if gender < 0 or gender > 1:
        print("Error: gender must be female (0) or male (1)")

    # Nested if loop to calculate employee's tax
    if gender == 0:
        # Special case 2 (negative salary)
        if salary < 0:
            print("Error: salary can't be negative")
            break
        elif salary < 1000:
            tax = 0.1 * salary
        elif salary < 2000:
            tax = 0.2 * salary
        else:
            tax = 0.3 * salary

        # Calculation for total tax and count
        total = total + tax
        count = count + 1

# Special case 3 (no female employees)
if total == 0:
    print("There are no female employees")
    quit()

# Output
print("Average tax for all female employees = ", total / count)