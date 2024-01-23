from dataclasses import dataclass


@dataclass
class Report:
    def __init__(self, net_worth, cash_balance, liabilities):
        self.net_worth = net_worth
        self.cash_balance = cash_balance
        self.liabilities = liabilities
