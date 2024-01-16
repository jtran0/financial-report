import transaction_parser


class ChaseTransactionParser(transaction_parser.TransactionParser):
    def __init__(self):
        super().__init__()

    def format_chase_bank_statement(self):
        for transactions in self.statement:
            for transaction in transactions:
                transaction.pop(0)  # Remove Detail Column
                transaction.pop(3)  # Remove Type Column
                transaction.pop(4)  # Remove Check or Slip Column
        return self.statement

    def format_chase_credit_card(self):
        for transactions in self.statement:
            for transaction in transactions:
                transaction.pop(1)  # Remove Post Date
                transaction.pop(-1)  # Remove White Space
                transaction.pop(-2)  # Remove Type
        return self.statement
