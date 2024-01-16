from abc import ABC, abstractmethod
from typing import List
import transaction
import csv


class TransactionParser(ABC):
    """
    This class is responsible for parsing a list of bank transactions given a
    statement of transactions
    """

    def __init__(self):
        self.statement: List[transaction.Transaction] = []

    def parse_statement(self, statement_filepath: str):
        with open(statement_filepath, "r") as statements:
            csvreader = csv.DictReader(statements)
            for row in csvreader:
                # Create a Transaction object using keyword assignments with default values
                transaction_obj = transaction.Transaction(
                    posting_date=row.get("posting_date", "default_posting_date"),
                    description=row.get("description", "default_description"),
                    amount=float(row.get("amount", 0.0)),
                    balance=float(row.get("balance", 0.0)),
                    category=row.get("category", "default_category"),
                )
                self.statement.append(transaction_obj)
