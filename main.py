from budgetmanager import BudgetManager

def main():
    manager = BudgetManager()

    while True:
        print("1: Add income")
        print("2: Add expense")
        print("3: Expense chart")
        print("4: Income chart")
        print("Q: Quit")
        action = input("What do you want to do? ").lower()

        if action == 'q':
            print("We are finishing the program.")
            break

        elif action == '1':
            user_input = input("Enter the income amount and description (separated by a comma): ")
            amount_str, description = user_input.split(",")
            amount = float(amount_str.strip())
            manager.add_incomes(amount, description.strip())

        elif action == '2':
            user_input = input("Enter the expense amount and description (separated by a comma): ")
            amount_str, description = user_input.split(",")
            amount = float(amount_str.strip())
            manager.add_expenses(amount, description.strip())

        elif action == '3':
            manager.plot_expenses_pie_chart()

        elif action == '4':
            manager.plot_income_pie_chart()

        else:
            print("Invalid option, please try again.")
        manager.show_summary()
        manager.show_details()

if __name__ == "__main__":
    main()