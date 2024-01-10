from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Transaction:
    merchant_name_description: str
    amount: float
    # date_and_time:


# class Transaction:
#     def __init__(self, merchant_name_description, amount):
#         self.merchant_name_description = merchant_name_description
#         self.amount = amount


class BankStatement:
    def __init__(self):
        self.transactions: List[Transaction] = []

    def import_statement(self, csv_filepath: str):
        with open(csv_filepath) as statements:
            for transaction in statements:
                self.transactions.append(transaction)


# bank_statement = BankStatement()
# bank_statement.import_statement("./bankstatement.csv")
# print("Number of transactions: {}".format(len(bank_statement.transactions)))
