# """
# Program to 1. calculate total values of all foods w/ price
# >= 3 (value = price * quantity) 2. Return list of foods (by
# names) that have price >= 3 3. Ask user to enter name and price
# of a food ~ if food is in list, update its price with entered
# price, otherwise tell user that food doesn't exist in list
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# Function 1: calculate total values of all foods w/ price
#             >= 3 (value = price * quantity)
def total_value():
    """
    Input: list
    Behavior: calculate total values of all foods that have
              price >= 3 (value = price * quantity)
    Output: total values of all foods w/ price >= 3
    """
    # Initialize variable
    total = 0
    # For loop: check if price >= 3
    for i in range(len(lst)):
        # Food record (name, price, quantity)
        record = lst[i]
        # Price at position 1
        price = record[1]
        # Quantity at position 2
        quantity = record[2]
        # If statement: add value to total if price >= 3
        if price >= 3:
            # Value equation
            total += price * quantity
    # Output (total value of foods w/ price >= 3)
    print("Total value of all foods that have a price greater than or equal to 3 =", total)

# Function 2: return list of foods (by names) that have price >= 3
def list_foods():
    """
    Input: list
    Behavior: get foods (by name) that have price >= 3
    Output: list w/ foods (by name) that have price >= 3
    """
    # Initialize list
    lst2 = []
    # For loop: check if price >= 3
    for i in range(len(lst)):
        # Food record (name, price, quantity)
        record = lst[i]
        # Name at position 0
        name = record[0]
        # Price at position 1
        price = record[1]
        # If statement: add food to list if price >= 3
        if price >= 3:
            lst2.append(name)
    # Output (list of foods w/ price >= 3)
    print("List of foods that have a price bigger or equal to 3:", lst2)

# Function 3: ask user to enter name & price of a food. If food
#             is in list, update price w/ entered price. Otherwise,
#             tell the user that the food is not in the list
def update_price():
    """
    Input: list
    Behavior: ask user to enter name + price of food
              If food is in the list, update price w/ entered price
              Otherwise, tell the user that food isn't in list
    Output: updated price of entered food OR message that food isn't in list
    """
    # User input (food + price)
    food_name = input("Enter name of food: ")
    food_price = float(input("Enter price of food: "))
    # Boolean statement initialize
    is_in_list = False
    # For loop: check if food is in list
    for i in range(len(lst)):
        # Index for food in list
        food = lst[i][0]
        # Food record (name, price, quantity)
        record = lst[i]
        # If statement: check if inputted food is in list
        if food == food_name:
            is_in_list = True
            break
    # If else statement: update price if food is in list or
    # print error message if food is not within list
    if is_in_list:
        # Update price if food is in the list
        new_price = food_price
        # New list with updated price
        lst[i] = (food_name, new_price, record[2])
        print(lst)
    else:
        # Print error message if food is not within list
        print("ERROR: The food you entered doesn't exist within the list!")

# List (of tuples) of Tom's foods in fridge (name, price, quantity)
lst = [("Apple", 5, 10), ("Banana", 2, 4), ("Grape", 4, 8), ("Cheese", 5, 9)]

# Call to all functions
total_value()
list_foods()
update_price()