# """
# QUB Python Individual Final Project - Book Shop Software
# November 27, 2025
# Created by Santiago Cuervo
# """

# List of customers [[ID, name, gender, phone]]
lst_customers = []

# List of books [[ID, name, type, price, quantity]]
lst_books = []

# List of transactions [(customer ID, book ID, amount, total price, day, month, year)]
lst_trans = []

def load_from_file():
    """
    Load customers, books, and transactions from text files into lists
    """
    global lst_customers, lst_books, lst_trans

    print("Loading data from files...")

    # Load the customer file here
    f = open("data_customers.txt", "r")
    lst_customers = []
    for line in f:
        # Read each line and separate the info w/ commas
        id, name, gender, phone = line.split(",")
        # Add customers to the list
        lst_customers.append([int(id), name, gender, int(phone)])
    f.close()

    # For testing purpose only
    # print(lst_customers)

    # Load the book file here
    f = open("data_books.txt", "r")
    lst_books = []
    for line in f:
        # Read each line and separate the info w/ commas
        id, name, book_type, price, quantity = line.split(",")
        # Add books to the list
        lst_books.append([int(id), name, book_type, int(price), int(quantity)])
    f.close()

    # For testing purpose only
    # print(lst_books)

    # Load the transaction file here
    f = open("data_transactions.txt", "r")
    lst_trans = []
    for line in f:
        # Read each line and separate info w/ commas
        customer_id, book_id, amount, total_price, day, month, year = line.split(",")
        # Add transactions to the list of transactions
        lst_trans.append([int(customer_id), int(book_id), int(amount),
                          float(total_price), int(day), int(month), int(year)])
    f.close()

    # For testing purpose only
    # print(lst_trans)

    print("Load data completed...")

def save_to_file():
    """
    Save customers, books, and transactions from lists into text files
    """
    global lst_customers, lst_books, lst_trans

    print("Saving data to file...")

    # Save the customer file here
    f = open("data_customers.txt", 'w')
    for item in lst_customers:
        # id = item[0], name = item[1], gender = item[2], phone = item[3]
        id, name, gender, phone = item
        # Create a string w/ this info separated by commas to save to file
        # String will end with \n to end the line
        s = str(id) + "," + name + "," + gender + "," + str(phone) + "\n"
        # Write the string s to file
        f.write(s)
    f.close()

    # Save the book file here
    f = open("data_books.txt", 'w')
    for item in lst_books:
        # id = item[0], name = item[1], booktype = item[2],
        # price = item[3], quantity = item[4]
        id, name, book_type, price, quantity = item
        # Create a string w/ this info separated by commas to save to file
        # String will end with \n to end the line
        s = (str(id) + "," + name + "," + book_type + ","
        + str(price) + "," + str(quantity) + "\n")
        # Write the string s to file
        f.write(s)
    f.close()

    # Save the transaction file here
    f = open("data_transactions.txt", 'w')
    for item in lst_trans:
        # customer id = item[0], book id = item[1],
        # amount = item[2], total price = item[3],
        # day = item[4], month = item[5], year = item[6]
        customer_id, book_id, amount, total_price, day, month, year = item
        # Create a string w/ this info separated by commas to save to file
        # String will end with \n to end the line
        s = (str(customer_id) + "," + str(book_id) + ","
        + str(amount) + ","  + str(total_price) + ","
        + str(day) + "," + str(month) + "," + str(year) + "\n")
        # Write the string s to file
        f.write(s)
    f.close()

    print("Save data completed...")

def get_customer(id):
    """
    Return index of customer with the given ID
    in lst_customers, or -1 if not found
    """
    for i in range(len(lst_customers)):
        itemi = lst_customers[i]
        # If customer id is found, return its position
        if id == itemi[0]:
            return i
    return -1

def get_book(id):
    """
    Return index of the book with the given ID
    in lst_books, or -1 if not found
    """
    for i in range(len(lst_books)):
        itemi = lst_books[i]
        # If book id is found, return its position
        if id == itemi[0]:
            return i
    return -1

def show_all_info():
    """
    Print all customers, books, and transactions (useful for testing)
    """
    print("CUSTOMERS: ", lst_customers)
    print("BOOKS: ", lst_books)
    print("TRANSACTIONS: ", lst_trans)

def feature_1_show_customer():
    """
    Show all information of a customer given their ID
    """
    try:
        id = int(input("Enter customer ID: "))
    except ValueError:
        print("ERROR: Please enter an integer for customer ID")
        return

    pos = get_customer(id)
    # If customer is not in the list, print an error message
    if pos == -1:
        print("ERROR: Customer ID not found in the system")
    # Otherwise, return customer's information
    else:
        item = lst_customers[pos]
        print("Name:", item[1], " Gender:", item[2],
              " Phone Number:", item[3])

def feature_2_add_book():
    """
    Add a new book or update an existing book given its IDS and info
    """
    global lst_books

    try:
        id = int(input("Enter book ID: "))
        name = input("Enter book name: ")
        book_type = input("Enter book type: ")
        price = int(input("Enter book price: "))
        quantity = int(input("Enter total quantity of this book: "))
    except ValueError:
        print("ERROR: Invalid input. Please enter correct data types")
        return

    if price < 0 or quantity < 0:
        print("ERROR: Price and quantity cannot be negative")
        return

    pos = get_book(id)
    # If book is not found, add it to the list
    if pos == -1:
        lst_books.append([id, name, book_type, price, quantity])
        print("New book added successfully")
    # Otherwise, update existing book's name, type, price, and quantity
    else:
        lst_books[pos] = [id, name, book_type, price, quantity]
        print("Existing book updated successfully")

def feature_3_add_transaction():
    """
    Add a new transaction after validating customer, book, and stock
    Apply a  discount if # of books purchased > 10
    Update remaining book stock
    """
    global lst_books, lst_trans

    try:
        customer_id = int(input("Enter customer ID: "))
        book_id = int(input("Enter book ID: "))
        quantity = int(input("Enter quantity to purchase: "))
        day = int(input("Enter day of transaction: "))
        if day > 31 or day < 0:
            print("ERROR: Please enter a valid day (1-31)")
            return
        month = int(input("Enter month of transaction: "))
        if month > 12 or month < 0:
            print("ERROR: Please enter a valid month (1-12)")
            return
        year = int(input("Enter year of transaction: "))
        if year > 2020 or year < 2010:
            print("ERROR: Please enter a year between 2010 and 2020")
            return
    except ValueError:
        print("ERROR: Please enter integers for IDs, quantity, and date")
        return

    customer_pos = get_customer(customer_id)
    book_pos = get_book(book_id)

    # If customer is not in the list, print an error message
    if customer_pos == -1:
        print("ERROR: Customer ID not found in the system")
        return
    # If book not in list, print an error message
    elif book_pos == -1:
        print("ERROR: Book ID not found in the shop")
        return
    elif quantity <= 0:
        print("ERROR: Quantity must be a positive integer")
        return

    amount = lst_books[book_pos][4]
    price = lst_books[book_pos][3]

    # If quantity exceeds stock, print an error message
    if quantity > amount:
        print("ERROR: Not enough stock available for this book")
        return

    total_price = price * quantity

    # If customer buys > 10 books, they receive a discount
    if quantity > 10:
        try:
            discount = float(input("Enter discount (%): "))
        except ValueError:
            print("ERROR: Discount must be a number")
            return
        if discount < 0 or discount > 100:
            print("ERROR: Discount must be between 0 and 100")
            return
        total_price *= (1 - (discount / 100))

    # Add transaction to the system with all its info
    lst_trans.append([customer_id, book_id, quantity, total_price,
                          day, month, year])
    # Update book's stock
    lst_books[book_pos][4] -= quantity
    print("Transaction recorded successfully")

def feature_4_booktype_count():
    """
    Show number of books of a given type and their average price in the shop
    """
    booktype = input("Enter book type: ")

    total_price = 0
    count = 0

    for book in lst_books:
        # Check if book's type matches input
        if book[2] == booktype:
            total_price += book[3]
            count += 1

    #  Booktype is found in the shop
    if count > 0:
        average_price = total_price / count
        print(count, "books are type:", booktype,
          "AND average price of them:", average_price)
    # Otherwise, print an error message
    else:
        print("ERROR: No books in the shop are of this type")

def feature_5_customer_purchases():
    """
    Show total books purchased and total money spent by a customer given their ID
    """
    try:
        id = int(input("Enter customer ID: "))
    except ValueError:
        print("ERROR: Please enter an integer for customer ID")
        return

    if get_customer(id) == -1:
        print("ERROR: Customer ID not found in the system")
        return

    books = 0
    total_price = 0

    for trans in lst_trans:
        # If  inputted id = customer id in list of transactions,
        # add book quantity from transaction and total cost
        if id == trans[0]:
            books += trans[2]
            total_price += trans[3]

    print(books, "books were purchased by this customer and they"
                 " spent a total of:", total_price)

def feature_6_booktype_purchases():
    """
    Show total quantity sold and total money spent for all books of a given type
    """
    book_type = input("Enter booktype: ")

    books = 0
    total = 0

    for trans in lst_trans:
        book_id = trans[1]
        amount = trans[2]
        price = trans[3]
        for book in lst_books:
            # If ID exists and type = input, add book type
            # quantity and total money spent on them
            if book_id == book[0] and book_type == book[2]:
                books += amount
                total += price

    print(books, "total books of type:", book_type, "were purchased"
          " and the total money spent on these books:", total)

def feature_7_best_customer():
    """
    Print ID, name, phone, and total spent for the customer with the highest spending
    """
    max_money = 0
    max_id = None

    for customer in lst_customers:
        id = customer[0]
        total = 0
        for trans in lst_trans:
            # Calculate money spent for each customer
            if id == trans[0]:
                total += trans[3]
        # If customer spent the most money, get their ID and total
        if total > max_money:
            max_money = total
            max_id = id

    for customer in lst_customers:
        # Get the highest paying customer's ID, name, and phone #
        if customer[0] == max_id:
            max_name = customer[1]
            max_phone = customer[3]
            break

    print("Best customer:", max_name,
          "\nID:", max_id,
          "\nPhone number:", max_phone,
          "\nTotal amount spent:", max_money)

def feature_8_total_purchases_yearly():
    """
    Print total amount of money spent in the shop for each year from 2010 to 2020
    """
    d = {}
    # Initialize total money spent for each year
    for i in range(2010, 2021):
        d[i] = 0

    for trans in lst_trans:
        year = trans[6]
        # Add total money spent each year into the correct year
        if year in d:
            d[year] += trans[3]

    for year in d:
        print("Total amount of money spent in", year, "is:", d[year])

def feature_9_worst_book():
    """
    Print ID, name, type, and total purchases of the book with the lowest total purchases
    """
    min_quantity = 1000000
    min_id = None

    for book in lst_books:
        id = book[0]
        total = 0
        for trans in lst_trans:
            # Calculate quantity bought for each book
            if id == trans[1]:
                total += trans[2]
        # If a book is the least purchased, get its ID and total
        if total < min_quantity:
            min_quantity = total
            min_id = id

    for book in lst_books:
        # Get lowest purchased book's's ID, name, and type
        if book[0] == min_id:
            min_name = book[1]
            min_type = book[2]
            break

    print("The book with the lowest number of purchases is:", min_name,
          "\nID:",min_id,
          "\nType:", min_type,
          "\nTotal quantity purchased:", min_quantity)

def feature_10_gender_books():
    """
    Print total quantities of books purchased by male and female customers
    """
    male_books = 0
    female_books = 0

    for customer in lst_customers:
        id = customer[0]
        gender = customer[2]
        for trans in lst_trans:
            if id == trans[0]:
                # Set quantity of books to same as in list of transactions
                total = trans[2]
                if gender == "Male":
                    male_books += total
                else:
                    female_books += total

    # Print outputs (male total books and female total books)
    print("Total books purchased by males:", male_books,
          "\nTotal books purchased by females:", female_books)

def feature_11_show_book():
    """
    Show all information of a book given its ID
    """
    try:
        id = int(input("Enter a book ID: "))
    except ValueError:
        print("ERROR: Please enter an integer for book ID")
        return

    pos = get_book(id)
    # If the book is not in the shop, print an error message
    if pos == -1:
        print("ERROR: book ID not found in the shop")
    # Otherwise, print the book's name, price, and quantity
    else:
        item = lst_books[pos]
        print("Name:", item[1],
              "\nBook type:", item[2],
              "\nPrice:", item[3],
              "\nQuantity:", item[4])

def feature_12_add_customer():
    """
    Add a new customer or update an existing customer given their ID and info
    """
    global lst_customers

    try:
        id = int(input("Enter ID: "))
        name = input("Enter name: ")
        gender = input("Enter gender (Male OR Female): ")
        if gender != "Male" and gender != "Female":
            print("ERROR: Gender must be 'Male' or 'Female'")
            return
        phone = int(input("Enter phone: "))
    except ValueError:
        print("ERROR: Invalid input. Please enter the correct data types")
        return

    pos = get_customer(id)
    # If customer ID not found, add new customer to the list
    if pos == -1:
        lst_customers.append([id, name, gender, phone])
        print("New customer added successfully")
    # Otherwise, update customer's name, gender, and phone number
    else:
        lst_customers[pos] = [id, name, gender, phone]
        print("Existing customer updated successfully")

# Initial task: load data from files
load_from_file()

message = """
******** The book Shop program written by Santiago Cuervo ********
Feature 1: Show a customer
Feature 2: Add a book
Feature 3: Add a transaction
Feature 4: Count books by type
Feature 5: Show total books and money spent by a customer
Feature 6: Show total books and money spent for a book type
Feature 7: Find the best customer
Feature 8: Show total purchases for each year from 2010 to 2020
Feature 9: Find the worst book
Feature 10: Compare male and female customers by number of books purchased
Feature 11: Show a book by ID
Feature 12: Add a customer
...
0: Exit program 
"""

# Repeatedly run the main menu
while True:
    # For testing purpose only
    # show_all_info()

    # Print out all possible choices to users
    print(message)

    # Ask the user to select a choice
    try:
        x = int(input("Please enter your choice as indicated above: "))
    except ValueError:
        print("ERROR: Please enter a valid integer for your choice")
        continue

    # Get the user's choice and choose appropriate action
    if x == 1:
        # Feature 1 - show customer by ID
        feature_1_show_customer()
    elif x == 2:
        # Feature 2 - add book given book info
        feature_2_add_book()
    elif x == 3:
        # Feature 3 - add transaction given transaction info
        feature_3_add_transaction()
    elif x == 4:
        # Feature 4 - count # of books by type and their avg. price
        feature_4_booktype_count()
    elif x == 5:
        # Feature 5 - count # of books purchased by a customer
        #             as well as total amount of money spent
        feature_5_customer_purchases()
    elif x == 6:
        # Feature 6 - count # of purchased books by type
        #             as well as their total money made
        feature_6_booktype_purchases()
    elif x == 7:
        # Feature 7 - find the best customer
        feature_7_best_customer()
    elif x == 8:
        # Feature 8 - Show total purchases for all years
        #             from 2010 to 2021
        feature_8_total_purchases_yearly()
    elif x == 9:
        # Feature 9 - find the worst book
        feature_9_worst_book()
    elif x == 10:
        # Feature 10 - compare male and female customers
        feature_10_gender_books()
    elif x == 11:
        # Feature 11 - show book by ID
        feature_11_show_book()
    elif x == 12:
        # Feature 12 - add customer given customer info
        feature_12_add_customer()
    # Otherwise, stop while loop and end program
    else:
        print("Exiting program...")
        break  # To stop the while loop

# Finalize task: store data into files
save_to_file()

print("Program ended...")