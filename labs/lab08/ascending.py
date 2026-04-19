# """
# Program given a list of integers to sort list in ascending order
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# Function: sort list in ascending order
def ascending():
    """
    Input: list
    Behavior: sort list in ascending order
    Output: list in ascending order
    """
    # For loops: compare adjacent items + swap if they're out of order
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

# User input (# of items in list)
n = int(input("Enter # of items: "))
# Initialize list
lst = []
# For loop: add n # of items to list
for i in range(n):
    item = int(input("Enter item: "))
    lst.append(item)

# Print original list
print("Original list:", lst)
# Call to function
ascending()
# Print new list
print("New list:", lst)