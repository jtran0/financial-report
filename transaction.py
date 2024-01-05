from dataclasses import dataclass
from datetime import datetime


@dataclass
class Transaction:
    date_and_time: datetime
    merchant_name_description: str
    amount: float
