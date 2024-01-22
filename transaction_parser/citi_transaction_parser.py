import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class CitiTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()
        self.balance = 0.0

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                transaction_obj = Transaction(
                    transaction_date=row.get("Date", ""),
                    posting_date=row.get("Posting Date", ""),
                    description=row.get("Description", ""),
                    amount=row.get("Amount", 0.0),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", ""),
                    debit=row.get("Debit", 0.0),
                    credit=row.get("Credit", 0.0),
                )
                self.statement.append(transaction_obj)

    def print_transactions(self):
        """Only Used for test purposes"""
        lines = []
        for transaction_obj in self.statement:
            lines.append(f"Transaction Date: {transaction_obj.transaction_date}")
            lines.append(f"Posting Date: {transaction_obj.posting_date}")
            lines.append(f"Description: {transaction_obj.description}")
            lines.append(f"Debit: {transaction_obj.debit}")
            lines.append(f"Credit: {transaction_obj.credit}")
            lines.append("")
        print("\n".join(lines))

    def get_balance(self):
        self.balance = 0.0
        for transaction_obj in self.statement:
            if transaction_obj.debit:
                self.balance += float(transaction_obj.debit)
            if transaction_obj.credit:
                self.balance += float(transaction_obj.credit)
        print(self.balance)
        return self.balance
