import transaction_parser


class CitiTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def format_citi_credit_card(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[0]  # Remove Status
                del transaction[-1]  # Remove Member Name
        return self.statement
