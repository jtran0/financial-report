from transaction_parser.transaction import Transaction


class TransactionRules:
    @staticmethod
    def is_income(transaction: Transaction) -> bool:
        """
        Checks if a transaction is an income transaction.
        """
        return (
            "payroll" in transaction.description.lower()
            or "atm" in transaction.description.lower()
        )

    @staticmethod
    def is_expense(transaction: Transaction) -> bool:
        """
        Checks if a transaction is an expense transaction.
        """
        return (
            "entertainment" in transaction.category.lower()
            or "food" in transaction.category.lower()
            or "shopping" in transaction.category.lower()
            or "groceries" in transaction.category.lower()
            or "sale" in transaction.type.lower()
            or "merchandise" in transaction.category.lower()
            or "restaurant" in transaction.category.lower()
        )

    @staticmethod
    def is_payment(transaction: Transaction) -> bool:
        """
        Checks if a transaction is a transfer or payment made
        to a credit card or another account.
        """
        return "auto" in transaction.description.lower()
