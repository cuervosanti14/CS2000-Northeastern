# """
# Program to input values of 5 locks and
# a lockpick and print out whether Jerry
# can have the cheese or can't have the cheese
# OPTION 2: USING A LIST
# Tuesday October 21, 2025
# Created by Santiago Cuervo
# """

# Initialize list
lst_locks = []

# For loop (get users input for all lock's powers,
# add locks to locks list, and print list)
for i in range(5):
    lock = int(input("Enter lock's power: "))
    lst_locks.append(lock)
print("locks =", lst_locks)

# User input for lockpick's power
lockpick = int(input("Enter lockpick's power: "))

# Initialize boolean statement
lockpick_opens = True

# For loop + If statement (check list of locks to
# see if lockpick is more powerful than all locks,
# and if not print that jerry can't have cheese
# and set boolean statement to False)
for i in range(len(lst_locks)):
    if lst_locks[i] >= lockpick:
        print("Jerry cannot have the cheese")
        lockpick_opens = False
        break

# If boolean statement remains true, meaning that
# lockpick more powerful than all locks, then
# print that Jerry can have cheese
if lockpick_opens:
    print("Jerry can have the cheese")