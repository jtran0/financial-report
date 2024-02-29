from typing import List
from transaction_parser.transaction import Transaction
from rules_manager.transaction_rules import TransactionRules
from rules_manager.rule_manager import RulesManager
from prettytable import PrettyTable


class ReportGenerator:
    """
    This class generates a report based on filtered lists of transactions.
    """

    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        self.total_expense = 0.0
        self.total_income = 0.0
        self.ignore_payment = 0.0
        self.net = 0.0
        self.income: List[Transaction] = []
        self.expense: List[Transaction] = []
        self.payments: List[Transaction] = []
        self.rules_manager = RulesManager()

    def import_transactions(self, transactions: List[Transaction]):
        """
        Store and accumulate lists of transaction objects for filtering.
        """
        self.transactions += transactions

    def filter_transactions(self):
        """
        Apply transaction rules to categorized transactions and filters
        the transactions into their corresponding lists. Then adds them to
        their corresponding total.
        """
        filtered_transactions = self.rules_manager.apply_rules(self.transactions)
        for transaction in filtered_transactions:
            if TransactionRules.is_income(transaction):
                self.total_income += transaction.amount
                self.income.append(transaction)
            elif TransactionRules.is_payment(transaction):
                self.ignore_payment += transaction.amount
                self.payments.append(transaction)
            elif TransactionRules.is_expense(transaction):
                self.total_expense += transaction.amount
                self.expense.append(transaction)
        self.net = self.total_income + self.total_expense

        return self.total_income, self.total_expense, self.ignore_payment

    def generate_table(self):
        """
        Prints a table of all imported transactions that are not filtered
        """
        statement = PrettyTable()
        statement.title = "All Transactions"
        statement.field_names = ["Date", "Description", "Amount", "Category", "Type"]
        for transaction in self.transactions:
            statement.add_row(
                [
                    f"{transaction.transaction_date}" or f"{transaction.posting_date}",
                    f"{transaction.description.strip()}",
                    f"{transaction.amount}",
                    f"{transaction.category}",
                    f"{transaction.type}",
                ]
            )
        print(statement)

    def generate_expenses(self):
        """
        Prints a table of all filtered expenses transactions
        """
        expense_statement = PrettyTable()
        expense_statement.title = "Expenses"
        for transaction in self.expense:
            expense_statement.field_names = [
                "Date",
                "Description",
                "Amount",
                "Category",
                "Type",
            ]
            expense_statement.add_row(
                [
                    f"{transaction.transaction_date}" or f"{transaction.posting_date}",
                    f"{transaction.description.strip()}",
                    f"{transaction.amount}",
                    f"{transaction.category}",
                    f"{transaction.type}",
                ]
            )
        return expense_statement

    def generate_income(self):
        """
        Prints a table of all filtered income transactions
        """
        income_statement = PrettyTable()
        income_statement.title = "Income"
        for transaction in self.income:
            income_statement.field_names = [
                "Date",
                "Description",
                "Amount",
                "Category",
                "Type",
            ]
            income_statement.add_row(
                [
                    f"{transaction.transaction_date}" or f"{transaction.posting_date}",
                    f"{transaction.description.strip()}",
                    f"{transaction.amount}",
                    f"{transaction.category}",
                    f"{transaction.type}",
                ]
            )
        return income_statement

    def generate_net(self):
        """
        Prints a table with the sum of all Income/Expense
        and the net from calculated from Income/Expense
        """
        net = PrettyTable()
        net.field_names = ["Total Income", "Total Expense", "Net"]
        net.add_row([f"{self.total_income}", f"{self.total_expense}", f"{self.net}"])
        return net

    def generate_payments(self):
        """
        Prints a table with all payment transactions to be ignored
        """
        payment_statement = PrettyTable()
        payment_statement.title = "Ignored Payments"
        for transaction in self.payments:
            payment_statement.field_names = [
                "Date",
                "Description",
                "Amount",
                "Category",
                "Type",
            ]
            payment_statement.add_row(
                [
                    f"{transaction.transaction_date}" or f"{transaction.posting_date}",
                    f"{transaction.description.strip()}",
                    f"{transaction.amount}",
                    f"{transaction.category}",
                    f"{transaction.type}",
                ]
            )
        return payment_statement
