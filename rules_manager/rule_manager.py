from typing import Callable, List
from transaction_parser.transaction import Transaction
from rules_manager.rule import Rule


class RulesManager:
    """
    Manages rules for filtering transactions.
    """

    def __init__(self):
        self.rules: List[Rule] = []

    def add_rule(self, condition: Callable[[Transaction], bool]):
        """
        Adds a new filtering rule.
        """
        rule = Rule(condition)
        self.rules.append(rule)

    def remove_rule(self, rule: Rule):
        """
        Removes a filtering rule.
        """
        self.rules.remove(rule)

    def apply_rules(self, transactions: List[Transaction]) -> List[Transaction]:
        """
        Applies all rules to filter transactions.
        """
        filtered_transactions = []
        for transaction in transactions:
            if all(rule.matches(transaction) for rule in self.rules):
                filtered_transactions.append(transaction)
        return filtered_transactions
