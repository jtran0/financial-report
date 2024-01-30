from typing import List
from transaction_parser.transaction_parser import Transaction


class ReportGenerator:
    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.total_expense = 0.0
        self.total_income = 0.0

    def import_transactions(self, transactions: List[Transaction]):
        self.transactions += transactions

    def generate_expense_report(self):
        for transaction in self.transactions:
            if "payroll" in transaction.description.lower():
                self.total_income += transaction.amount
            if "atm" in transaction.description.lower():
                self.total_income += transaction.amount
            if "auto" in transaction.description.lower():
                self.total_expense += transaction.amount
        return self.total_income + self.total_expense
