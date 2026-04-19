# """
# Program to find average value of
# all 2-digit numbers divisible by 7
# Friday October 2, 2025
# Created by Santiago Cuervo
# """

# Set avg to 0
total = 0
count = 0

# While loop (get all 2-digit numbers divisible by 7)
i = 10
while i < 100:
    if i % 7 == 0:
        total = total + i
        count = count + 1
    i = i + 1

# Output
print("Average value of all 2-digit numbers divisible by 7 = ", total / count)