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

    def parse_statement(self, statement_filepath: str):  # Open and create list
        with open(statement_filepath, "r") as statements:
            csvreader = csv.reader(statements)
            rows = []
            for row in csvreader:
                rows.append(row)
            self.statement.append(rows)
