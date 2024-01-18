from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    def __init__(
        self,
        transaction_date="",
        posting_date="",
        description="",
        amount=0.0,
        balance=0.0,
        category="",
    ):
        self.transaction_date = transaction_date
        self.posting_date = posting_date
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category
