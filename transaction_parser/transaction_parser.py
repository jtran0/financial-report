from abc import ABC, abstractmethod
from typing import List

from transaction_parser.transaction import Transaction


class TransactionParser(ABC):
    """
    This class is responsible for parsing a list of bank transactions given a
    statement of transactions
    """

    def __init__(self):
        self.statement: List[Transaction] = []

    @abstractmethod
    def parse_statement(self, statement_filepath: str):
        raise NotImplementedError

    @abstractmethod
    def print_transactions(self):
        raise NotImplementedError
