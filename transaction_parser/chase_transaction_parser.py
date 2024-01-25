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
                    transaction_date=row.get("Date", ""),
                    description=row.get("Description", ""),
                    amount=float(row.get("Amount", 0.0)),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", ""),
                )
                self.statement.append(transaction_obj)
                # balance_value = float(row.get("Balance", 0.0))

                # if balance_value:
                #     # If balance is found, skip processing the amount
                #     transaction_obj = Transaction(
                #         transaction_date=row.get("Date", ""),
                #         description=row.get("Description", ""),
                #         balance=balance_value,
                #         category=row.get("Category", ""),
                #     )
                # else:
                #     amount_value = float(row.get("Amount", 0.0))
                #     reversed_amount = -amount_value if amount_value != 0 else 0.0
                #     transaction_obj = Transaction(
                #         transaction_date=row.get("Date", ""),
                #         description=row.get("Description", ""),
                #         amount=reversed_amount,
                #         balance=balance_value,
                #         category=row.get("Category", ""),
                #     )
                # self.statement.append(transaction_obj)

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
