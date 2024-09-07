import matplotlib.pyplot as plt

class BudgetManager:
    def __init__(self):
        self.incomes = []
        self.expenses = []

    def add_incomes(self, amount, description):
        self.incomes.append({"amount": amount, "description": description})

    def add_expenses(self, amount, description):
        self.expenses.append({"amount": amount, "description": description})

    def calculate_balance(self):
        total_incomes = sum(item['amount'] for item in self.incomes)
        total_expenses = sum(item['amount'] for item in self.expenses)
        return total_incomes - total_expenses

    def show_summary(self):
        print("\n=== Budget Summary ===")
        print(f"Total incomes: {sum(item['amount'] for item in self.incomes)} zł")
        print(f"Total expenses: {sum(item['amount'] for item in self.expenses)} zł")
        print(f"Balance: {self.calculate_balance()} zł")

    def show_details(self):
        print("\n=== Incomes Details ===")
        for income in self.incomes:
            print(f"Income: {income['amount']} zł, Description: {income['description']}")

        print("\n=== Expenses Details ===")
        for expense in self.expenses:
            print(f"Expense: {expense['amount']} zł, Description: {expense['description']}")

    def plot_expenses_pie_chart(self):
        labels=[expense['description'] for expense in self.expenses]
        amounts=[expense['amount'] for expense in self.expenses]

        if amounts:
            plt.figure(figsize=(6, 6))
            plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.title("Distribution of expenses")
            plt.axis('equal')
            plt.show()
        else:
            print('Error')

    def plot_income_pie_chart(self):
        labels=[income['description'] for income in self.incomes]
        amounts=[income['amount'] for income in self.incomes]

        if amounts:
            plt.figure(figsize=(6, 6))
            plt.pie(amounts, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.title("Distribution of expenses")
            plt.axis('equal')
            plt.show()
        else:
            print('Error')
