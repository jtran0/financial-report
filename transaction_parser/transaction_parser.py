from abc import ABC, abstractmethod
from typing import List
import transaction


class TransactionParser(ABC):
    """
    This class is responsible for parsing a list of bank transactions given a
    statement of transactions
    """

    def __init__(self):
        self.statement: List[transaction.Transaction] = []

    @abstractmethod
    def parse_statement(self, statement_filepath: str):
        raise NotImplementedError

    def print_transactions(self):
        lines = []
        for transaction_obj in self.statement:
            lines.append(f"Transaction Date: {transaction_obj.trasanction_date}")
            lines.append(f"Posting Date: {transaction_obj.posting_date}")
            lines.append(f"Description: {transaction_obj.description}")
            lines.append(f"Amount: {transaction_obj.amount}")
            lines.append(f"Balance: {transaction_obj.balance}")
            lines.append(f"Category: {transaction_obj.category}")
            lines.append("")
        print("\n".join(lines))
