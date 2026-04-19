# """
# Program to create a bar plot to show the salary and hours of all
# workers in the same plot (should not be drawn in 2 different bars)
# Wednesday November 18, 2025
# Created by Santiago Cuervo
# """

# Import library
import matplotlib.pyplot as plt

# Function: create a bar plot to show the salary and
#           hours of all workers in the same plot
def salary_hours(workers):
    """
    Input: workers
    Behavior: return bar plot to show salary and
              hours of all workers in the same plot
    Output: bar plot
    """
    # Create lists
    salaries = []
    hours = []
    names = []
    # Add items to lists
    for item in workers:
        salaries.append(item[2])
        hours.append(item[3])
        names.append(item[0])
    # Print lists
    print("Salaries=", salaries)
    print("Hours=", hours)
    print("Workers=", names)
    # Create bar plot
    plt.bar(names, salaries, label = "Salary")
    # Stacks hours on top of salary for each worker (no overlap)
    plt.bar(names, hours, bottom = salaries, label = "Hours")
    plt.xlabel("Workers")
    plt.ylabel("Salary/Hours")
    plt.title("Worker's salaries and hours")
    plt.legend()
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
salary_hours(workers)