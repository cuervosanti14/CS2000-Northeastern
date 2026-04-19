# """
# Program to find who will arrive to
# school first between Tom and Jerry
# Thursday October 2, 2025
# Created by Santiago Cuervo
# """

# Input (distance, speed)
tom_distance = float(input("Tom's house's distance (miles) from school: "))
jerry_distance = float(input("Jerry's house's distance (miles) from school: "))
tom_speed = float(input("Tom's driving speed (mph) to school: "))
jerry_speed = float(input("Jerry's driving speed (mph) to school: "))

# Special case 1 (negative distance)
if tom_distance < 0 or jerry_distance < 0:
    print("Error: distance can't be negative")
    quit()
# Special case 2 (negative speeds / reverse)
elif tom_speed < 0 or jerry_distance < 0:
    print("Error: negative speed not included")
    quit()

# Calculating time spent going to school
tom_time = tom_distance / tom_speed
jerry_time = jerry_distance / jerry_speed

# If else statement (print who arrives first)
if tom_time > jerry_time:
    print("Jerry will arrive at school first")
elif jerry_time > tom_time:
    print("Tom will arrive at school first")
else:
    print("They will arrive at the same time")