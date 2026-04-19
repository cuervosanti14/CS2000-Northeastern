# """
# Program to create a pie chart to show salaries for male and female workers
# Wednesday November 18, 2025
# Created by Santiago Cuervo
# """

# Import library
import matplotlib.pyplot as plt

# Function: create a pie chart to show salaries for male and female workers
def salary_pie(workers):
    """
    Input: workers
    Behavior: return pie chart to show salaries for male and female workers
    Output: pie chart
    """
    # Initialize variables
    male_salary = 0
    female_salary = 0
    # Add items to variables
    for item in workers:
        if item[1] == "Male":
            male_salary += item[2]
        else:
            female_salary += item[2]
    # Print variables
    print("Male salary=", male_salary)
    print("Female salary=", female_salary)
    # Create pie chart
    plt.pie([male_salary, female_salary], labels = ["Male", "Female"])
    plt.title("Salary by gender")
    plt.show()

# list of workers [(Name,Gender,Salary,Hours)]
workers = [
    ("Thor","Male",20,5),
    ("Captain","Male",10,4),
    ("Widow","Female",30,10),
    ("Witch","Female",40,6),
    ("Loki","Male",15,1),
    ("Thanos","Male",50,20)
]

# list of foods [(Name,Type,Size,Price,Number)]
foods = [
    ("Orange",	"A",	3,	3,	2),
    ("Lemon",	"A",	3,	2,	4),
    ("Grape",	"B",	1,	4,	5),
    ("Melon",	"C",	6,	5,	2),
    ("Banana",	"B",	4,	1,	5),
    ("Coconut","C",	5,	4,	3),
    ("Watermelon",	"D",	9,	3,	3),
    ("Cherry",	"B",	1,	7,	5),
    ("Avocado",	"A",	2,	6,	4),
    ("Mango",   "A",    4,    5,    2)
]

# Call to function
salary_pie(workers)