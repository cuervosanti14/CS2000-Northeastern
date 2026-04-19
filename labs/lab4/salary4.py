# """
# Program to calculate average
# salary of all of Scrooge's employees
# Friday October 2, 2025
# Created by Santiago Cuervo
# """

# User input
num = int(input("Enter # of employees: "))

# Set to 0
salary = 0
count = 0

# For loop (hours, rate, salary, # of employees)
for i in range(num):
    hours = int(input("Enter work hours: "))
    rate = int(input("Enter rate per hour: "))
    salary = salary + (hours * rate)
    count = count + 1

# Output
print("Average salary of all employees = ", salary / count)