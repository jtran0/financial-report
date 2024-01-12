import transaction

jshu_chase_sapphire = transaction.Chase()
jshu_chase_sapphire.import_statement(
    "/Users/jeffreyshu/jshu-Chase/Chase6024_Activity20220112_20240112_20240112.CSV"
)
jshu_chase_sapphire.format_credit_card()
for x in jshu_chase_sapphire.statement:
    for y in x:
        print(y)

jshu_bank = transaction.Chase()
jshu_bank.import_statement(
    "/Users/jeffreyshu/jshu-Chase/Chase4838_Activity_20240112.CSV"
)
jshu_bank.format_bank_statement()
for x in jshu_bank.statement:
    for y in x:
        print(y)
