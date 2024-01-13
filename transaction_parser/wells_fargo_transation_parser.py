import transaction_parser


class WellsFargoTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def format_wells_fargo_credit_card(self):
        for transactions in self.statement:
            for transaction in transactions:
                del transaction[2:4]  # Remove Empty Space
        return self.statement
