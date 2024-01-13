from dataclasses import dataclass
import csv
from typing import List


@dataclass
class Transaction:
    def __init__(self, posting_date, description, amount, balance, category):
        self.posting_date = posting_date
        self.description = description
        self.amount = amount
        self.balance = balance
        self.category = category


class FinancialReport:
    def __init__(self):
        self.statement: List[Transaction] = []

    def import_statement(self, csv_filepath: str):  # Open and create list
        with open(csv_filepath, "r") as statements:
            csvreader = csv.reader(statements)
            rows = []
            for row in csvreader:
                rows.append(row)
            self.statement.append(rows)


class Chase(FinancialReport):
    def __init__(self):
        super().__init__()

    def format_bank_statement(self):
        for transactions in self.statement:
            for transaction in transactions:
                transaction.pop(0)  # Remove Detail Column
                transaction.pop(3)  # Remove Type Column
                transaction.pop(4)  # Remove Check or Slip Column
        return self.statement

    def format_credit_card(self):
        for transactions in self.statement:
            for transaction in transactions:
                transaction.pop(1)  # Remove Post Date
                transaction.pop(-1)  # Remove White Space
                transaction.pop(-2)  # Remove Type
        return self.statement


class AmericanExpress(FinancialReport):
    def __init__(self):
        super().__init__()

    def format_amex(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[3:-1]  # Remove clutter
        return self.statement


class Citi(FinancialReport):
    def __init__(self):
        super().__init__()

    def format_citi(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[0]  # Remove Status
                del transaction[-1]  # Remove Member Name
        return self.statement


class WellsFargo(FinancialReport):
    def __init__(self):
        super().__init__()

    def format_wells(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[2:4]  # Remove Empty Space
        return self.statement
