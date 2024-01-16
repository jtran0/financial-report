from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    def __init__(
        self,
        trasanction_date="",
        posting_date="",
        description="",
        amount=0.0,
        balance=0.0,
        category="",
    ):
        self.trasanction_date = trasanction_date
        self.posting_date = posting_date
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category
