# """
# Program given a list X of N integers to find the sublist
# with the longest length that is also a list of increasing #s
# Thursday November 6, 2025
# Created by Santiago Cuervo
# """

# User input (# of items in list)
n = int(input("Enter # of items: "))
# Initialize list
lst_x = []
# For loop: add n # of items to list
for i in range(n):
    item = int(input("Enter item: "))
    lst_x.append(item)

# Initialize sublists that will be compared
longest_sublst = []
current_sublst = []

# For loop: add values to current sublist as long as it is increasing
for i in range(n):
    # If statement (adds values if at start of list or increasing)
    if i == 0 or lst_x[i] > lst_x[i - 1]:
        current_sublst.append(lst_x[i])
    else:
        # If statement: if current sublist is longer than longest
        # sublist, then current sublist is new longest sublist
        if len(current_sublst) > len(longest_sublst):
            longest_sublst = current_sublst
        # Reset current sublist at end of loop
        current_sublst = [lst_x[i]]

# If statement: last check to see which sublist is the longest increasing one
if len(current_sublst) > len(longest_sublst):
    longest_sublst = current_sublst

# Output (longest increasing sublist)
print("Longest increasing sublist is:", longest_sublst)