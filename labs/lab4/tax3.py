# """
# Program to find total tax
# Scrooge must pay for his employees
# Friday October 3, 2025
# Created by Santiago Cuervo
# """

# User input
num = int(input("Enter # of employees: "))

# Set to 0
tax = 0
salary = 0

# For loop (hours, rate, salary, tax)
for i in range(num):
    hours = int(input("Enter work hours: "))
    rate = int(input("Enter rate per hour: "))
    salary = hours * rate
    if salary < 1000:
        tax = tax + salary * 0.1
    else:
        tax = tax + salary * 0.2

# Output
print("Total tax Scrooge must pay for his employees = ", tax)