# """Ch
# Program to 1. calculate total values of all foods w/ quantity
# >= 5 (value = price * quantity) 2. Return list of foods (by
# names) that have quantity >= 5 3. Ask user to enter name and quantity
# of a food ~ if food is in list, update its quantity with entered
# quantity, otherwise tell user that food doesn't exist in list
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# Function 1: calculate total values of all foods w/ quantity
#             >= 5 (value = price * quantity)
def total_value():
    """
    Input: list
    Behavior: calculate total values of all foods that have
              quantity >= 5 (value = price * quantity)
    Output: total values of all foods w/ quantity >= 5
    """
    # Initialize variable
    total = 0
    # For loop: check if quantity >= 5
    for k,v in d.items():
        # Price at value 0
        price = v[0]
        # Quantity at value 1
        quantity = v[1]
        # If statement: add value to total if quantity >= 5
        if quantity >= 5:
            # Value equation
            total += price * quantity
    # Output (total value of foods w/ quantity >= 5)
    print("Total value of all foods that have a quantity greater than or equal to 5 =", total)

# Function 2: return list of foods (by names) that have quantity >= 5
def list_foods():
    """
    Input: list
    Behavior: get foods (by name) that have quantity >= 5
    Output: list w/ foods (by name) that have quantity >= 5
    """
    # Initialize list
    lst2 = []
    # For loop: check if quantity >= 5
    for k,v in d.items():
        # Quantity at value 1
        quantity = v[1]
        # If statement: add food to list if quantity >= 5
        if quantity >= 5:
            lst2.append(k)
    # Output (list of foods w/ quantity >= 5)
    print("List of foods that have a quantity bigger or equal to 5:", lst2)

# Function 3: ask user to enter name & quantity of a food. If food
#             is in list, update quantity w/ entered quantity. Otherwise,
#             tell the user that the food is not in the list
def update_quantity():
    """
    Input: list
    Behavior: ask user to enter name + quantity of food
              If food is in the list, update quantity w/ entered quantity
              Otherwise, tell the user that food isn't in list
    Output: updated quantity of entered food OR message that food isn't in list
    """
    # User input (food + quantity)
    food_name = input("Enter name of food: ")
    food_quantity = float(input("Enter quantity of food: "))
    # If statement: if food in list, update quantity
    if food_name in d:
        d[food_name][1] = food_quantity
        print("Updated fridge:", d)
    # Else: error message
    else:
        # Print error message if food is not within list
        print("ERROR: The food you entered doesn't exist within the list!")

# Dictionary of Tom's foods in fridge (name, price, quantity)
d = {"Apple": [5, 10], "Banana": [2, 4], "Grape": [4, 8], "Cheese": [5, 9]}

# Call to all functions
total_value()
list_foods()
update_quantity()