import transaction_parser
import transaction
import csv


class ChaseTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def parse_statement_chase(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                transaction_obj = transaction.Transaction(
                    trasanction_date=row.get("Transaction Date", ""),
                    posting_date=row.get("Posting Date", ""),
                    description=row.get("Description", ""),
                    amount=float(row.get("Amount", 0.0)),
                    balance=float(row.get("Balance", 0.0)),
                    category=row.get("Category", " "),
                )
                self.statement.append(transaction_obj)

    def format_chase_bank_statement(self):
        for transactions in self.statement:
            for transaction_line in transactions:
                transaction_line.pop(0)  # Remove Detail Column
                transaction_line.pop(3)  # Remove Type Column
                transaction_line.pop(4)  # Remove Check or Slip Column
        return self.statement

    def format_chase_credit_card(self):
        for transactions in self.statement:
            for transaction_line in transactions:
                transaction_line.pop(1)  # Remove Post Date
                transaction_line.pop(-1)  # Remove White Space
                transaction_line.pop(-2)  # Remove Type
        return self.statement
