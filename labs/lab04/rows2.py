# """
# Program to print out 'N' rows and 5 columns
# but odd row use '*' and even row use '+'
# Friday October 2, 2025
# Created by Santiago Cuervo
# """

# User input
num = int(input("Enter rows: "))

# For loop output
for i in range(num):
    if i % 2 == 0:
        print("*****")
    else:
        print("+++++")