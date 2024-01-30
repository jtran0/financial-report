from typing import List
from transaction_parser.transaction_parser import Transaction


class ReportGenerator:
    """
    This class is responsible for filtering and generating
    a report from a collection of imported csv statments.
    """

    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.total_expense = 0.0
        self.total_income = 0.0
        self.ignore_payment = 0.0

    def import_transactions(self, transactions: List[Transaction]):
        """
        Store and accumulate lists of transaction
        objects for filtering
        """
        self.transactions += transactions

    def filter_transations(self):
        """
        Scan for key words
        in attributes of the transaction object
        and add them to the Report Generator
        class attributes.
        """
        for transaction in self.transactions:
            if "payroll" in transaction.description.lower():
                self.total_income += transaction.amount
            if "atm" in transaction.description.lower():
                self.total_income += transaction.amount
            if "auto" in transaction.description.lower():
                self.ignore_payment += transaction.amount
            if "Payment" in transaction.type.lower():
                self.ignore_payment += transaction.amount
            if "sale" in transaction.type.lower():
                self.total_expense += transaction.amount
            if "merchandise" in transaction.category.lower():
                self.total_expense += transaction.amount
            if "restaurant" in transaction.category.lower():
                self.total_expense += transaction.amount
        return self.total_income, self.total_expense, self.ignore_payment
