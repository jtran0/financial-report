from transaction_parser.transaction import Transaction


class TransactionRules:
    @staticmethod
    def is_income(transaction: Transaction) -> bool:
        """
        Checks if a transaction is an income transaction.
        """
        income_indicators = ["payroll", "atm"]
        return any(
            indicator in transaction.description.lower()
            for indicator in income_indicators
        )

    @staticmethod
    def is_expense(transaction: Transaction) -> bool:
        """
        Checks if a transaction is an expense transaction.
        """
        expense_categories = [
            "entertainment",
            "food",
            "shopping",
            "groceries",
            "merchandise",
            "restaurant",
        ]
        expense_types = ["sale"]
        return any(
            category in transaction.category.lower() for category in expense_categories
        ) or any(type_ in transaction.type.lower() for type_ in expense_types)

    @staticmethod
    def is_payment(transaction: Transaction) -> bool:
        """
        Checks if a transaction is a transfer or payment made
        to a credit card or another account.
        """
        payment_type = ["auto"]
        return any(
            description in transaction.description.lower()
            for description in payment_type
        )
