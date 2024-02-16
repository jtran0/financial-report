from typing import Callable, List
from transaction_parser.transaction import Transaction


class Rule:
    """
    Represents a filtering rule.
    """

    def __init__(self, condition: Callable[[Transaction], bool]):
        self.condition = condition

    def matches(self, transaction: Transaction) -> bool:
        """
        Checks if the transaction matches the rule.
        """
        return self.condition(transaction)
