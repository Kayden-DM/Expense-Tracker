Expense Tracker
A command-line Python program that lets a user add expenses, view them, and calculate the total spent.

Concepts Used
Classes & Objects — an Expense class stores each expense's name, amount, and category.

Lists of Objects — the expense list holds every Expense instance added.

While Loop Menu — a looping menu lets the user pick actions until they exit.

Features
Add Expenses — record a name, amount, and category for each expense.

View Expenses — list all stored expenses with their details.

Total Spending — sum up all expense amounts with a running total.

Improvements
Input Validation — wrap the float() amount in try/except (invalid input currently crashes the program).

Category Filtering & Totals — allow viewing or summing expenses by category.

Persistent Storage — save expenses to a file so data isn't lost when the program closes.

