## Expense Tracker
A command-line expense tracker written in Python. It uses an Expense class to store a name, amount, and category for each entry, and runs an interactive menu loop for adding, viewing, and totalling expenses.

## Features
Add Expense — Prompts for a name, amount, and category, then stores the expense in a list.

View Expenses — Prints every recorded expense with its name, amount, and category.

Show Total — Adds up the amount of every expense and prints the total.

Menu Loop — Runs until the user selects option 4 to exit.

Exit — Breaks out of the loop cleanly when option 4 is chosen.

## Technologies Used
| Technology | Purpose |
|---|---|
| Python | Application logic |
| Class (`Expense`) | Encapsulates name, amount, and category |
| List (`expense`) | Stores all recorded expenses |
| `input()` / `print()` | Console interaction |
| `float()` | Parses expense amounts |
| `while True` loop | Keeps the menu running until exit |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Save the code as expense_tracker.py.

Open a terminal in the folder containing the file.

Run python expense_tracker.py.

Use the menu: 1 to add an expense, 2 to view all expenses, 3 to show the total, 4 to exit.

## Improvements
Validate amounts — float(input(...)) will crash on non-numeric input; wrap it in a try/except ValueError loop like the other projects so the user is re-prompted.

Persist the expenses — Save the list to a JSON file on exit and reload it on startup so expenses survive between sessions.
