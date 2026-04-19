# """
# Program to calculate Tom's
# arrival time to school
# Thursday September 25, 2025
# Created by Santiago Cuervo
# """

# User input (distance + speed)
miles = float(input("Tom's house's distance from school: "))
mph = float(input("Tom's walking speed to school: "))

# Calculations (minutes walking)
walking_minutes = (miles / mph) * 60

# Start time in minutes (8 AM)
start_time = 8 * 60

# Time Tom arrives (in minutes) + 15 minute break
time_minutes = start_time + walking_minutes + 15

# Calculations (arrival time)
school_hour = int(time_minutes // 60)
school_minute = int(time_minutes % 60)

# Print output (arrival time)
print("Tom arrives at school at ", school_hour, ":", school_minute)