from dataclasses import dataclass


@dataclass
class Transaction:
    def __init__(
        self,
        transaction_date="",
        posting_date="",
        description="",
        amount=0.0,
        balance=0.0,
        debit=0.0,
        credit=0.0,
        category="",
        type="",
    ):
        self.transaction_date = transaction_date
        self.posting_date = posting_date
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category
        self.debit = debit
        self.credit = credit
        self.type = type
