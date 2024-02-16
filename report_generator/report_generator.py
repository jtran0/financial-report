from typing import List
from transaction_parser.transaction_parser import Transaction
from rules_manager.transaction_rules import TransactionRules


class ReportGenerator:
    """
    This class generates a report based on filtered lists of transactions.
    """

    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.total_expense = 0.0
        self.total_income = 0.0
        self.ignore_payment = 0.0

    def import_transactions(self, transactions: List[Transaction]):
        """
        Store and accumulate lists of transaction objects for filtering.
        """
        self.transactions += transactions

    def filter_transactions(self):
        """
        Apply transaction rules to categorize transactions.
        """
        for transaction in self.transactions:
            if TransactionRules.is_income(transaction):
                self.total_income += transaction.amount
            elif TransactionRules.is_payment(transaction):
                self.ignore_payment += transaction.amount
            elif TransactionRules.is_expense(transaction):
                self.total_expense += transaction.amount

        return self.total_income, self.total_expense, self.ignore_payment
