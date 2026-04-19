# """
# Program to find x
# given 2 numbers
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# User input (#)
a = float(input("Enter a: "))
b = float(input("Enter b: "))

# Special case 1 (a is 0, but b is not)
if (a == 0 and b != 0):
    print("No value of x exists")
# Special case 2 (a and b are both 0)
elif a == 0 and b == 0:
    print("X = all real numbers")
# Normal case
else:
    x = b / a
    print("X = ", x)