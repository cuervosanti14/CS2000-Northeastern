# """
# Program with 2 functions: ask users to enter
# a list of N integer numbers & increase
# all even numbers at even positions by 5
# Tuesday October 21, 2025
# Created by Santiago Cuervo
# """

# Function 1 (ask user to enter a list of N integer #s)
def get_num():
    """
    Input: empty list
    Behavior: get user input for each item in
              list and return list with values
    Output: list with user input for items
    """
    # For loop (get user input for items + add to list)
    for i in range(n):
        item = int(input("Enter item: "))
        lst.append(item)
    # Print original list (output)
    print("Original list: ", lst)

# Function 2 (increase all even #s at even positions by 5)
def even_nums():
    """
    Input: original list
    Behavior: check if item is at an even position
              and then check if item is an even #.
              If it is, increase # by 5
    Output: new list with increased items
    """
    # For loop
    for i in range(len(lst)):
        # Check for even position
        if i % 2 == 0:
            # Check for even #
            if lst[i] % 2 == 0:
                # Increase even # at even position by 5
                lst[i] += 5
    # Output (new list w/ increased values)
    print("New list: ", lst)

# User input (n # of items in list)
n = int(input("Enter number of items in the list: "))

# Initialize list
lst = []

# Call to both functions
get_num()
even_nums()