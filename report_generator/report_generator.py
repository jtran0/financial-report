from typing import List
from transaction_parser.transaction_parser import Transaction


class ReportGenerator:
    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.total_income = 0.0
        self.total_expense = 0.0
        self.cash_balance = 0.0

    def import_transactions(self, transactions: List[Transaction]):
        self.transactions += transactions

    def generate_checking_account_report(self):
        for transaction in self.transactions:
            if transaction.amount > 0:
                self.total_income += transaction.amount
            else:
                self.total_expense += transaction.amount
        lines = [
            f"Debit(Inbound): {round(self.total_income, 2)}",
            f"Credit(Outbound): {round(self.total_expense, 2)}",
            f"Net: {round(self.total_income + self.total_expense, 2)}",
        ]

        print("\n".join(lines))

    def generate_shopping_expense(self):
        shopping_expense = 0.0
        for transaction in self.transactions:
            if "Shopping" in transaction.category:
                shopping_expense += transaction.amount
                print(f"\nDescription: {transaction.description}")
                print(f"Amount: {round(transaction.amount, 2)}")
                print(f"Category: {transaction.category}")
        print(f"\nTotal Shopping Expense: ${round(shopping_expense, 2)}")

    def generate_restaurant_expense(self):
        restaurant_expense = 0.0
        for transaction in self.transactions:
            if "Restaurant" in transaction.category:
                restaurant_expense += transaction.amount
                print(f"\nDesciption: {transaction.description}")
                print(f"Amount: ${round(transaction.amount, 2)}")
                print(f"Category: {transaction.category}")
        print(f"\nTotal Restaurant Expense: ${round(restaurant_expense, 2)}")

    def generate_entertainment_expense(self):
        entertainment_expense = 0.0
        for transaction in self.transactions:
            if "Entertainment" in transaction.category:
                entertainment_expense += transaction.amount
                print(f"\nDesciption: {transaction.description}")
                print(f"Amount: ${round(transaction.amount, 2)}")
                print(f"Category: {transaction.category}")
        print(f"\nTotal Entertainment Expense {round(entertainment_expense, 2)}")
