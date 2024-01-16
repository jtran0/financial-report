import transaction_parser
import transaction
import csv


class AmericanExpressTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                transaction_obj = transaction.Transaction(
                    trasanction_date=row.get("Transaction Date", ""),
                    posting_date=row.get("Date", ""),
                    description=row.get("Description", ""),
                    amount=float(row.get("Amount", 0.0)),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", ""),
                )
                self.statement.append(transaction_obj)
