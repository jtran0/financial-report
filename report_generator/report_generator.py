from report_generator.report import Report
from typing import List


class ReportGenerator:
    def __init__(self):
        self.reports: List[Report] = []

    def generate_report(self, transactions):
        liabilities = 0.0
        cash_balance = 0.0

        for transaction_obj in transactions:
            liabilities += transaction_obj.amount
            cash_balance += transaction_obj.balance

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

            print(f"Total Debt: {total_liabilities}")
            print(f"Total Cash: {total_cash_balance}")
            print(f"Total Net Worth: {total_net_worth}")
