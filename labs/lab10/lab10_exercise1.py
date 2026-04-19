# """
# Program with 4 functions: #1 gives bar plot to show size
# of all foods #2 gives line plot to show prices of all foods
# #3 gives a pie chart to show salaries of all workers #4 gives a
# scatter plot to show relationship between sizes + prices of foods
# Tuesday November 18, 2025
# Created by Santiago Cuervo
# """

# Import library
import matplotlib.pyplot as plt

# Function 1: gives bar plot to show size of all foods
def food_sizes(foods):
    """
    Input: list of foods
    Behavior: return bar plot to show all foods' sizes
    Output: bar plot
    """
    # Create lists
    sizes = []
    names = []
    # Add items to lists
    for item in foods:
        sizes.append(item[2])
        names.append(item[0])
    # Print lists
    print("Sizes=", sizes)
    print("Foods=", names)
    # Create bar plot
    plt.bar(range(len(sizes)), sizes, label = "Size")
    plt.xlabel("Foods")
    plt.ylabel("Size")
    plt.title("Sizes of all foods")
    plt.xticks(range(len(sizes)), names)
    plt.legend()
    plt.show()

# Function 2: gives line plot to show prices of all foods
def food_prices(foods):
    """
    Input: list of foods
    Behavior: return line plot to show all foods' prices
    Output: line plot
    """
    # Create lists
    prices = []
    names = []
    # Add items to lists
    for item in foods:
        prices.append(item[3])
        names.append(item[0])
    # Print lists
    print("Prices=", prices)
    print("Foods=", names)
    # Create line plot
    plt.plot(prices, 'ro-', label = "Price")
    plt.xlabel("Foods")
    plt.ylabel("Prices")
    plt.title("Prices of all foods")
    plt.xticks(range(len(prices)), names)
    plt.legend()
    plt.show()

# Function 3: gives a pie chart to show salaries of all workers
def worker_salaries(workers):
    """
    Input: worker
    Behavior: return pie chart to show all workers' salaries
    Output: pie chart
    """
    # Create lists
    salaries = []
    names = []
    # Add items to lists
    for item in workers:
        salaries.append(item[2])
        names.append(item[0])
    # Print lists
    print("Salaries=", salaries)
    print("Workers=", names)
    # Create pie chart
    plt.pie(salaries, labels = names)
    plt.title("Worker's Salaries")
    plt.show()

# Function 4: gives a scatter plot to show relationship between
#             sizes + prices of foods
def food_sizes_prices(foods):
    """
    Input: list of foods
    Behavior: return scatter plot to show relationship
              between sizes & prices of foods
    Output: scatter plot
    """
    # Create lists
    sizes = []
    prices = []
    # Add items to lists
    for item in foods:
        sizes.append(item[2])
        prices.append(item[3])
    # Print lists
    print("Sizes=", sizes)
    print("Prices=", prices)
    # Create scatterplot
    plt.scatter(sizes, prices)
    plt.xlabel("Sizes")
    plt.ylabel("Prices")
    plt.title("Relationship between sizes & prices of foods")
    plt.legend(["Sizes/Prices"], loc = "lower right")
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

# Call to functions
food_sizes(foods)
food_prices(foods)
worker_salaries(workers)
food_sizes_prices(foods)