# """
# Program to enter 2 positive #s 'a'
# and 'b' and print out 'a'
# triangles with size 'b'
# Wednesday October 15, 2025
# Created by Santiago Cuervo
# """

# Function (take triangle of size b and print it)
def draw_triangle(b):
    """
    Input: b (size of triangle)
    Behavior: for loop to print triangle
    Output: return desired triangle
    """
    # Nested for loop to print triangle of size b
    for i in range(b):
        for j in range(i + 1):
            print("*", end=" ")
        print()

# User input for 'a' triangles of size 'b'
a = int(input("Enter a: "))
b = int(input("Enter b: "))

# For loop to print 'a' number of triangles
for i in range(a):
    draw_triangle(b)