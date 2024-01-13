import transaction_parser


class AmericanExpressTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def format_amex_credit_card(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[3:-1]  # Remove clutter
        return self.statement
