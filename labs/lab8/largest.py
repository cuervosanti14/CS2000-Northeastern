# """
# Program given a list of integers and a positive number
# k to find the k-th largest number in the list
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# Function: sort list in descending order
def sort(lst):
    """
    Input: list
    Behavior: sort list in descending order
    Output: list in descending order
    """
    # For loop: sort list in descending order
    for i in range(len(lst)):
        max_index = i
        for j in range(i + 1, n):
            if lst[j] > lst[max_index]:
                max_index = j
        # Swap values
        lst[i], lst[max_index] = lst[max_index], lst[i]

# User input (# of items in list)
n = int(input("Enter # of items: "))
# Initialize k to negative #
k = -1
# While loop: make user input positive #
while k <= 0:
    k = int(input("Enter k: "))
    # If k is negative, print error message
    if k <= 0:
        print("Try again. K must be positive")
    # Else, exit loop (user inputted correctly)
    else:
        break

# Initialize list
lst = []
# For loop: add n # of items to list
for i in range(n):
    item = int(input("Enter item: "))
    lst.append(item)

# Call to function
sort(lst)

# If statement (print k-th largest # in list)
if k <= len(lst):
    print("#", k, "largest number in the list is:", lst[k-1])
# Else: ERROR ~ k is > than list size
else:
    print("ERROR: k is larger than the list's size")