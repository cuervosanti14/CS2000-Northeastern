# """
# Program to check if a list is a fibonnaci sequence
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# Function: check if list is a fibonacci sequence
def fibonacci(lst):
    """
    Input: list
    Behavior: check if list is a fibonacci sequence
    Output: print if it is or if it isn't a fibonacci sequence
    """
    # Initialize boolean statement
    is_fibonacci = True
    # If first 2 values aren't 1, then can't be fibonacci sequence
    if lst[0] != 1 or lst [1] != 1:
            is_fibonacci = False
    # For loop: if one value is not equal to previous 2 values
    #           added together in list, then can't be fibonacci sequence
    for i in range(2, len(lst)):
        if lst[i] != lst[i - 1] + lst[i - 2]:
            is_fibonacci = False
    # If statement: if all conditions met, is fibonacci
    if is_fibonacci:
        print("List is a fibonacci sequence")
    # Else: if conditions not met, not fibonacci
    else:
        print("List is not a fibonacci sequence")

# User input (# of items in list)
n = 2
# While loop (only accept input > 3 for n_
while n < 3:
    n = int(input("Enter # of items: "))
    # If statement: if n < 3, print error message
    if n < 3:
        print("List is too short to check if it is a fibonacci sequence")
    # Else: if n > 3, exit loop
    else:
        break

# Initialize list
lst = []
# For loop: add n # of items to list
for i in range(n):
    item = int(input("Enter item: "))
    lst.append(item)

# Call to function
fibonacci(lst)