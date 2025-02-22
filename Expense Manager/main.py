def add_expenses(expenses, amount, category):
    expenses.append({'amount': amount, 'category': category})

def print_all_expenses(expenses):
    for expense in expenses:
        print(f"Amount: {expense['amount']}, Category: {expense['category']}")

def total_expenses(expenses):
    return sum(map(lambda expense: expense['amount'], expenses))

def filter_expenses_by_category(expenses, category):
    return filter(lambda expense: expense['category'] == category, expenses)

def main():
    expenses = []

    while True:
        print("1. Add Expense")
        print("2. Print Expenses")
        print("3. Total Expenses")
        print("4. Filter expenses by category")
        print("5. Exit")

        choice = input("Enter your choice: ")
        
        match(choice):
            case '1':
                amount = int(input("Enter the amount: "))
                category = input("Enter the category: ")
                add_expenses(expenses, amount, category)
            case '2':
                print_all_expenses(expenses)
            case '3':
                total = total_expenses(expenses)
                print(f"Total Expenses: {total}")
            case '4':
                category = input("Enter the category to filter: ")
                filtered_expenses = filter_expenses_by_category(expenses, category)
                print(list(filtered_expenses))
            case '5':
                exit()
            case _:
                print("Invalid choice!!")

if __name__ == "__main__":
    main()
