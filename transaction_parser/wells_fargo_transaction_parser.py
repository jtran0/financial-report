import csv

from transaction_parser.transaction_parser import TransactionParser
from transaction_parser.transaction import Transaction


class WellsFargoTransactionParser(TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.reader(statements)
            for row in csvreader:
                amount = float(row[1])
                reversed_amount = -amount if amount != 0 else 0.0

                transaction_obj = Transaction(
                    transaction_date=row[0],
                    amount=reversed_amount,
                    description=row[4],
                )
                self.statement.append(transaction_obj)
