from dataclasses import dataclass
from typing import List


@dataclass
class Transaction:
    def __init__(self, posting_date, description, amount, balance, category):
        self.posting_date = posting_date
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category
