# """
# Program to perform 5 functions given Scrooge's list of employees [name, age, salary]
# 1. Write info of employees from list into a file "data.txt" where each employee
# will be a row (name, age, salary separated by commas) 2. Load all info from file "data.txt"
# to list 3. Ask user to enter name of a employee, and if not in list, print message
# to let user know, otherwise print out all his/her info (including age + salary)
# 4. Ask user to enter name, age, and salary of an employee. If the employee is not in
# the list, add employee into list of employees. If the employee is already in the list,
# update the age and salary for employee. 5. Ask user to enter a float number 'x'
#and count how many employees have a salary greater than or equal to float number 'x'
# Wednesday November 12, 2025
# Created by Santiago Cuervo
# """

# List of employees [[Name, Age, Salary]]
lst = [["Tom", 25, 100,], ["Jerry", 30, 200], ["Daisy", 10, 100],
       ["Marie", 20, 250]]

# Function 1: write all information of employees from 'lst' into
#             a file called "data.txt" where each employee will be
#             in a row (name, age, and salary are separated by commas)
def lst_to_file(lst):
    """
    Input: lst
    Behavior: write all info from 'lst' into a "data.txt" file
    Output: return each employee info in a row
    """
    # Open the file to save
    try:
        with open("data.txt", "w") as f:
            # Put each item of 'lst' into file
            for item in lst:
                # We create a string: "name, age, salary" from item = [name, age, salary]
                s = item[0] + "," + str(item[1]) + "," + str(item[2]) + "\n"
                # Write str to file
                f.write(s)
    # Exception: error while writing file
    except Exception as e:
        print("There was an error while writing the file", e)

# Function 2: load all information from file "data.txt" to 'lst'
def file_to_lst():
    """
    Input: file
    Behavior: load employee info from "data.txt" into 'lst'
    Output: return new list with info from "data.txt" file
    """
    # Initialize new list
    new_lst = []
    # Open the file
    try:
        with open("data.txt", "r") as f:
            # For loop (remove newline character at end + split line into parts separated by commas)
            for line in f:
                parts = line.strip().split(",")
                # Check that there are 3 parts (name, age, salary)
                if len(parts) == 3:
                    name = parts[0]
                    # Convert age and salary from strings to #s
                    age = int(parts[1])
                    salary = float(parts[2])
                    new_lst.append([name, age, salary])
    # Exception: file not found
    except FileNotFoundError:
        print("File not found, returning an empty list")
    # Exception: error converting data
    except ValueError:
        print("Error converting data properly")
    # Exception: error reading file
    except Exception as e:
        print("There was an error while reading the file", e)
    # Return new list
    return new_lst

# Function 3: check if name is in the list
def is_exist(name):
    """
    Input: user input for name
    Behavior: check if name is in list
    Output: return position of item if in list
    """
    # For loop (check if item is in list)
    for i in range(len(lst)):
        # If statement: check if item is the same as user input
        if lst[i][0] == name:
            # Return item's index
            return i
    # Return -1 if name not in list
    return -1

# Function 4: ask users to enter the name of a employee. If employee is not in the list,
#             print out a message to let the user know. If the employee is in the list,
#             print out all of his/her information including age and salary
def check_employee():
    """
    Input: user input for name
    Behavior: check if name is in list
    Output: return employee info if in list, otherwise print that name is not in list
    """
    # User input for employee
    try:
        name = input("Enter name of employee: ")
        # Call to function
        position = is_exist(name)
        # If else statement (print if name is in list or if it is not in list)
        if position == -1:
            print(name, "is not in the list")
        else:
            print(name, "is in the list. Info:", lst[position])
    # Exception: error searching for name
    except Exception as e:
        print("Error searching for name in list", e)

# Function 5: ask users to enter name, age, and salary of an employee. If the employee
#             is not in the list, add employee into list of employees. If the employee
#             is already in the list, update age and salary for this employee
def add_update_employee():
    """
    Input: user input for name
    Behavior: check if name is in list
    Output: return employee info if in list, otherwise print that name is not in list
    """
    # User input (name, age, salary)
    try:
        name = input("Enter employee's name: ")
        age = int(input("Enter employee's age: "))
        salary = float(input("Enter employee's salary: "))
        # Call to function
        position = is_exist(name)
        # If else statement (add new employee to list or update current employee's salary)
        if position == -1:
            lst.append([name, age, salary])
            print(name, "added as new employee to list of employees")
            print(lst)
        else:
            lst[position][1] = age
            lst[position][2] = salary
            print("Updated employee:", name)
            print(lst)
    # Exception: invalid inputs
    except ValueError:
        print("Invalid input for age and salary. Please enter correct values")
    # Exception: error adding or updating employees
    except Exception as e:
        print("Error while adding or updating employees", e)

# Function 6: ask users to enter a float # 'x', then count how many
#             employees have a salary greater than or equal to 'x'
def count_salaries():
    """
    Input: user input for float value 'x'
    Behavior: check how many employees have salary >= 'x'
    Output: return # of employees with salary >= 'x'
    """
    # User input for float # 'x'
    try:
        x = float(input("Enter value for x: "))
        # Initialize variable
        count = 0
        # For loop (loop through employees in list)
        for employee in lst:
            # If statement (check if employee salary >= x, and if so increase count)
            if employee[2] >= x:
                count += 1
        # Output (# of employees)
        print(count, "employees have a salary >=", x)
    # Exception: invalid input
    except ValueError:
        print("Invalid input. Please enter correct float number")
    # Exception: error counting salaries
    except Exception as e:
        print("Error counting salaries", e)

# Call to functions
lst_to_file(lst)
lst = file_to_lst()
check_employee()
add_update_employee()
count_salaries()