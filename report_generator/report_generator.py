from report_generator.report import Report
from typing import List
from transaction_parser.transaction_parser import Transaction


class ReportGenerator:
    def __init__(self):
        self.reports: List[Report] = []

    def import_transaction(self, transactions):
        liabilities = 0.0
        cash_balance = 0.0
        found_balance = False

        for transaction_obj in transactions:
            if transaction_obj.balance and not found_balance:
                cash_balance = transaction_obj.balance
                found_balance = True
                if found_balance:
                    break
            elif transaction_obj.amount:
                liabilities += transaction_obj.amount
            elif transaction_obj.debit or transaction_obj.credit:
                liabilities += transaction_obj.debit
                liabilities += transaction_obj.credit

        net_worth = cash_balance - liabilities

        report = Report(
            net_worth=net_worth, cash_balance=cash_balance, liabilities=liabilities
        )

        self.reports.append(report)

    def generate_report(self, transactions):
        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction.amount > 0:
                total_income += transaction.amount
            else:
                total_expense += transaction.amount
        print(
            "\nTotal Income: {} \nTotal Expense: {} \nNet: {}".format(
                round(total_income, 2),
                round(total_expense, 2),
                round(total_income + total_expense, 2),
            )
        )

    def print_report(self):
        if self.reports:
            total_liabilities = round(
                sum(report.liabilities for report in self.reports), 2
            )

            total_cash_balance = round(
                sum(report.cash_balance for report in self.reports), 2
            )

            total_net_worth = round(sum(report.net_worth for report in self.reports), 2)

            print(f"Debt: {total_liabilities}")
            print(f"Cash: {total_cash_balance}")
            print(f"Net Worth: {total_net_worth}")
