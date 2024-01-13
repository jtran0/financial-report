import wells_fargo_transation_parser

# import Amex_transaction_parser
# import chase_transaction_parser
# import citi_transaction_parser

wells_fargo = wells_fargo_transation_parser.WellsFargoTransactionParser()
wells_fargo.parse_statement("/Users/jeffreyshu/jshu_finance/Wellsfargo/CreditCard1.csv")
wells_fargo.format_wells_fargo_credit_card()
for x in wells_fargo.statement:
    for y in x:
        print(y)
