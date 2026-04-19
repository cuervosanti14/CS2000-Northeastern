# CS2000 – Introduction to Program Design and Implementation

**Northeastern University | NUin Program – Queen's University Belfast | Fall 2025**
**Instructor:** Dr. Mai Thai Son

---

## Overview

This repository contains all lab exercises and the final project from CS2000, taken during my Northeastern NUin semester abroad at Queen's University Belfast. The course introduced core programming concepts using Python, with an emphasis on structured problem solving, clean code design, and building progressively more complex programs from scratch.

---

## Repository Structure

```
CS2000/
├── labs/
│   ├── lab2/        # Pseudocode, arithmetic, and basic I/O
│   ├── lab3/        # Conditionals and decision logic
│   ├── lab4/        # Loops (for and while)
│   ├── lab5/        # Functions and modular design
│   ├── lab6/        # Lists and data structures
│   ├── lab8/        # Tuples, dictionaries, and file I/O
│   ├── lab9/        # Exception handling and file operations
│   └── lab10/       # Data visualization with matplotlib
├── project/
│   ├── bookshop.py          # Final project – bookshop management system
│   └── data/
│       ├── data_books.txt
│       ├── data_customers.txt
│       └── data_transactions.txt
└── README.md
```

---

## Final Project – Simple Bookshop Management System

The final project is a U/I command-line application that simulates a real bookshop inventory and transaction system. Data is stored using plain text files, with full save and load functionality.

**Features implemented:**
- Show customer or book by ID
- Add and update books and customers
- Record purchase transactions with optional discounts
- Count books by type and calculate average price
- Query a customer's purchase history and total spend
- Aggregate purchases by book type
- Identify the best customer by total spending
- Show yearly purchase totals (2010–2020)
- Find the worst-performing book by number of purchases
- Compare total purchases between male and female customers
- Full error handling across all features (invalid IDs, types, negative values, insufficient stock)
- Save to and load from `.txt` files on program start and exit

---

## Topics Covered

The labs progress week by week through foundational Python concepts:

| Lab | Topics |
|-----|---------|
| Lab 2 | Pseudocode, arithmetic operations, basic I/O, data types |
| Lab 3 | Conditionals (`if`, `elif`, `else`), comparison operators, special cases |
| Lab 4 | `for` and `while` loops, nested loops, pattern problems |
| Lab 5 | Functions, parameters, return values, modular design principles |
| Lab 6 | Lists, list traversal (index and item), nested lists |
| Lab 8 | Tuples, dictionaries, updating and querying structured data |
| Lab 9 | Exception handling (`try`/`except`), reading and writing files |
| Lab 10 | Data visualization — bar, line, pie, and scatter plots with `matplotlib` |

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?logo=python&logoColor=white)

---

## Notes

- All labs include test cases with expected outputs, verified by hand and program runs.
- Each lab builds on the concepts from the previous week — later labs reuse and extend functions written earlier.
- The final project report includes detailed feature testing, proposed future improvements, and a reflection on system limitations in a real-world context.
