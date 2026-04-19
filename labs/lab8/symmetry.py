# """
# Program given a list of integers to check if list is symmetrical
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# User input (# of items in list)
n = int(input("Enter # of items: "))

# Initialize list
lst = []

# For loop: add n # of items to list
for i in range(n):
    item = int(input("Enter item: "))
    lst += [item]
# Print list
print(lst)

# Initialize bool statement
is_symmetrical = True
# For loop: check if list is symmetrical or not
for i in range(len(lst) // 2):
    # If statement: check if list is not symmetrical
    if lst[i] != lst[len(lst) - i - 1]:
        is_symmetrical = False
        break

# If statement: print is symmetrical if it is
if is_symmetrical:
    print("List is symmetrical")
# Else: print is not symmetrical if is not
else:
    print("List is not symmetrical")