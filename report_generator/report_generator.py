from typing import List
from transaction_parser.transaction_parser import Transaction


class ReportGenerator:
    def __init__(self) -> None:
        self.transactions: List[Transaction] = []

    def import_transactions(self, transactions: List[Transaction]):
        self.transactions += transactions

    def generate_expense_report(self):
        total_income = 0
        total_expense = 0
        for transaction in self.transactions:
            if transaction.amount > 0:
                total_income += transaction.amount
            else:
                total_expense += transaction.amount
        lines = [
            f"Total income: {round(total_income, 2)}",
            f"Total expense: {round(total_expense, 2)}",
            f"Net: {round(total_income + total_expense, 2)}",
        ]

        print("\n".join(lines))
