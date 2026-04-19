# """
# Program to input values of 5 locks and
# a lockpick and print out whether Jerry
# can have the cheese or can't have the cheese
# OPTION 1: NOT USING A LIST
# Tuesday October 21, 2025
# Created by Santiago Cuervo
# """

# User input for power of each lock
lock1 = int(input("Enter lock 1's power: "))
lock2 = int(input("Enter lock 2's power: "))
lock3 = int(input("Enter lock 3's power: "))
lock4 = int(input("Enter lock 4's power: "))
lock5 = int(input("Enter lock 5's power: "))

# User input for power of lockpick
lockpick = int(input("Enter lockpick's power: "))

# If else statement (check whether lockpick is more
# powerful than all locks and can open them so Jerry
# can have the cheese or if he can't have the cheese
# because the lockpick isn't powerful enough)
if lockpick > lock1 and lockpick > lock2 and lockpick > lock3 and lockpick > lock4 and lockpick > lock5:
    print("Jerry can have the cheese")
else:
    print("Jerry cannot have the cheese")