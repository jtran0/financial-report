import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class ChaseTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()
        self.balance = 0.0

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                transaction_obj = Transaction(
                    transaction_date=row.get("Transaction Date", ""),
                    posting_date=row.get("Posting Date", ""),
                    description=row.get("Description", ""),
                    amount=float(row.get("Amount", 0.0)),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", ""),
                )
                self.statement.append(transaction_obj)

    def print_transactions(self):
        """Only Used for test purposes"""
        lines = []
        for transaction_obj in self.statement:
            lines.append(f"Transaction Date: {transaction_obj.transaction_date}")
            lines.append(f"Posting Date: {transaction_obj.posting_date}")
            lines.append(f"Description: {transaction_obj.description}")
            lines.append(f"Amount: {transaction_obj.amount}")
            lines.append(f"Balance: {transaction_obj.balance}")
            lines.append(f"Category: {transaction_obj.category}")
            lines.append("")
        print("\n".join(lines))

    def get_balance(self):
        for transaction_obj in self.statement:
            if transaction_obj.amount:
                self.balance += transaction_obj.amount
        return self.balance
