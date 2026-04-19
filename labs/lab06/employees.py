# """
# Program #1 using Scrooge's list of employees to
# 1. calculate total salary for employees 25 and
# older 2. Check if there is an employee with a
# given name 3. Check if user input for employee is in
# list and if is increase salary by 20%. Otherwise
# print message saying employee isn't in list
# 4. Find employee with the highest salary
# Tuesday October 21, 2025
# Created by Santiago Cuervo
# """

# Function 1 (calculate total salary for
# employees who are 25 years or older)
def total_salary():
    """
    Input: list of employees
    Behavior: check if employee is 25 or older, and
              if they are, add their salary to total
    Output: total salary of employees 25 or older
    """
    # Initialize variable
    total = 0
    # For loop + if statement (check if employee is 25
    # or older + add their salary to total salary)
    for i in range(len(lst_employees)):
        if lst_employees[i][1] >= 25:
            total += lst_employees[i][2]
    # Output (total salary)
    print("Total salary for employees who are 25 "
          "or older =", total)

# Function 2 (check if there is an employee with a given name)
def is_exist(name):
    """
    Input: user input for name
    Behavior: check if inputted name is in list of employees
    Output: either name is or isn't in list of employees
    """
    for i in range(len(lst_employees)):
        # Check if name is in list of employees
        if name == lst_employees[i][0]:
            # Return index if name in list
            print(name, "is in the list")
            return i
    # Return -1 if name not in list
    print(name, "isn't in the list")
    return -1

# Function 3 (ask user to enter an employee's name and
# increase their salary by 20% if they're in the list.
# Otherwise, tell user that there is no employee w/ that name
def increase_salary():
    """
    Input: user input for employee
    Behavior: check if user input is in list. If it is
              then set to True, otherwise stays False.
    Output: either employee's new salary or that there
            is no employee of the inputted name
    """
    # User input for employee name
    employee = input("Enter employee's name: ")
    # Define position using function 2's index return value
    position = is_exist(employee)
    # If else statement (print new salary if user input
    # is correctly in the list of employees, and print
    # that employee name doesn't exist if not)
    if position != -1:
        lst_employees[position][2] *= 1.2
        print(employee, "new salary =", lst_employees[position][2])
    else:
        print("There is no employee by the name of", employee)

# Function 4 (find name of employee with highest salary)
def highest_salary():
    """
    Input: list of employees
    Behavior: go through each employee's salary and
              check if it is the highest salary
    Output: name and salary of employee w/ highest salary
    """
    # Initialize variable
    max = 0
    # For loop (check if employee's salary is greater
    # the max salary, and if it is set as new max)
    for i in range(len(lst_employees)):
        if lst_employees[i][2] > max:
            max = lst_employees[i][2]
            name_max = lst_employees[i][0]
    # Output (name and salary of employee w/ highest salary)
    print(name_max, "has the highest salary of =", max)

# List of employees [[Name, Age, Salary]]
lst_employees = [["Tom", 25, 100], ["Jerry", 30, 200],
                ["Daisy", 20, 100], ["Marie", 20, 250]]

# Call to each function
total_salary()

# User input for name
name = input("Enter a name: ")

# Call to each function
is_exist(name)
increase_salary()
highest_salary()