)
💸 Python Expense Tracker
A simple command-line expense tracking application built with Python. This program lets users add expenses, view all recorded expenses, and calculate the total amount spent. It's a great beginner project for learning about object-oriented programming (OOP), classes, lists, and menu-driven programs in Python.

📖 Python Expense Tracker
The Python Expense Tracker is a console-based application that helps users keep track of their spending. Each expense is stored as an object created from the Expense class, containing a name, amount, and category.

When the program starts, a looping menu appears with options to add an expense, view all expenses, show the total expense, or exit. Every added expense is appended to a list, which can then be iterated over to display details or sum up the total spending.

This project is ideal for anyone learning the fundamentals of Python classes, lists, and interactive programs.

✨ Features
Add an expense – Enter a name, amount, and category for each expense.

View all expenses – Displays every recorded expense with its name, amount, and category.

Show total expense – Calculates and prints the sum of all expense amounts.

Looping menu – Keeps running until the user chooses to exit.

Simple exit option – Quit the program cleanly at any time.

Object-oriented design – Each expense is an instance of the Expense class.

🛠️ What It Uses
Language & Library
Python 3 – No external libraries required (pure standard library).

Class: Expense
Method	Purpose
__init__(self, name, amount, category)	Initializes an expense with a name, amount, and category.
Attributes
name – The name/description of the expense.

amount – The monetary value of the expense.

category – The category the expense belongs to (e.g., food, transport).

Data Structure
python
expense = []  # A list that stores Expense objects
Python Concepts Demonstrated
Object-oriented programming – Defining and using a class.

Classes and objects – Creating instances of Expense.

Lists – Storing multiple expense objects.

Looping through lists – Using for e in expense.

Conditional logic – Handling menu choices.

Loops – while True for the main menu.

User input – Reading and processing input via input().

Type conversion – Using float() to convert the amount input.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays menus and expense details.

float() – Converts the amount input into a decimal number.

append() – Adds a new expense to the list.

break – Exits the main loop when the user chooses option 4.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
expense_tracker.py
No installation or dependencies are needed — just Python.

▶️ How to Run
Make sure you have Python 3 installed (python.org).

Save the code as expense_tracker.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python expense_tracker.py
Use the menu to add, view, and total your expenses.

