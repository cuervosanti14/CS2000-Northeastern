# """
# Program to calculate
# tax for his employees
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (name, salary)
name = input("Enter name of employee: ")
salary = float(input("Enter employee's salary: "))

# Set to 0
tax = 0

# Special case 1 (negative salary)
if salary < 0:
    print("Error: salary can't be negative")
    quit()
# If else (calculate tax from salary)
elif salary < 1000:
    tax = salary * 0.1
elif salary < 2000:
    tax = salary * 0.2
elif salary < 3000:
    tax = salary * 0.3
else:
    tax = salary * 0.4

# Output (name, salary, tax)
print(name, "'s salary = ", salary, "and their tax = ", tax)