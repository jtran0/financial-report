from report_generator.report import Report
from typing import List


class ReportGenerator:
    def __init__(self):
        self.reports: List[Report] = []

    def import_transaction(self, transactions):
        liabilities = 0.0
        cash_balance = 0.0

        for transaction_obj in reversed(transactions):
            if transaction_obj.amount:
                liabilities += transaction_obj.amount
            if transaction_obj.balance:
                cash_balance = transaction_obj.balance
                print(cash_balance)

        net_worth = cash_balance - liabilities

        report = Report(
            net_worth=net_worth, cash_balance=cash_balance, liabilities=liabilities
        )

        self.reports.append(report)

    def print_report(self):
        if self.reports:
            total_liabilities = sum(report.liabilities for report in self.reports)

            total_cash_balance = sum(report.cash_balance for report in self.reports)

            total_net_worth = sum(report.net_worth for report in self.reports)

            print(f"Debt: {total_liabilities}")
            print(f"Cash: {total_cash_balance}")
            print(f"Net Worth: {total_net_worth}")
