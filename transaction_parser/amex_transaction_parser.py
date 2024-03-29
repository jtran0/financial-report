import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class AmericanExpressTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                transaction_obj = Transaction(
                    transaction_date=row.get("Date", ""),
                    description=row.get("Description", ""),
                    amount=-float(row.get("Amount", 0.0)),
                    category=row.get("Category", ""),
                )
                self.statement.append(transaction_obj)
