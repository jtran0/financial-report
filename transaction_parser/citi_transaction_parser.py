import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class CitiTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                debit_value = row.get("Debit", "")
                credit_value = row.get("Credit", "")

                # Convert non-numeric strings to 0.0
                try:
                    debit_value = float(debit_value)
                except ValueError:
                    debit_value = 0.0

                try:
                    credit_value = float(credit_value)
                except ValueError:
                    credit_value = 0.0

                transaction_obj = Transaction(
                    transaction_date=row.get("Date", ""),
                    posting_date=row.get("Posting Date", ""),
                    description=row.get("Description", ""),
                    amount=row.get("Amount", 0.0),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", ""),
                    debit=debit_value,
                    credit=credit_value,
                )
                self.statement.append(transaction_obj)
