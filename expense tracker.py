class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

expense = []

while True:
    print("====== EXPENSE TRACKER ======")
    print("1. Add expense")
    print("2. View expense")
    print("3. Show total expense")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        category = input("Enter expense category: ")
        expense.append(Expense(name, amount, category))
        print("Expense added")
    elif choice == "2":
        for e in expense:
            print(e.name, e.amount, e.category)
    elif choice == "3":
        total = 0
        for e in expense:
            total += e.amount
        print("Total expense:", total)
    elif choice == "4":
        break

    else:
        print("Invalid choice")