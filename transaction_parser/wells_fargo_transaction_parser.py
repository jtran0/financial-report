import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class WellsFargoTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.reader(statements)
            # Assumes there is no header in Wells Fargo CSV
            for row in csvreader:
                transaction_obj = Transaction(
                    transaction_date=row[0],
                    amount=float(row[1]),
                    description=row[4],
                )
                self.statement.append(transaction_obj)

    def print_transactions(self):
        """Only Used for test purposes"""
        lines = []
        for transaction_obj in self.statement:
            lines.append(f"Transaction Date: {transaction_obj.transaction_date}")
            lines.append(f"Description: {transaction_obj.description}")
            lines.append(f"Amount: {transaction_obj.amount}")
            lines.append("")
        print("\n".join(lines))
