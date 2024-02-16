from report_generator.report_generator import ReportGenerator
from transaction_parser.chase_transaction_parser import ChaseTransactionParser
from transaction_parser.amex_transaction_parser import AmericanExpressTransactionParser
from transaction_parser.citi_transaction_parser import CitiTransactionParser


class TestAccount:
    def test_chase_checking(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement(
            "test/test_files/Test_ChaseCheckingAcc.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transactions()
        assert report.ignore_payment == -7000
        assert report.total_income == 2300.00

    def test_chase_credit_card(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement(
            "test/test_files/Chase_CreditCard_Test_Sample.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transactions()
        assert report.total_expense == -981
        assert report.ignore_payment == 1300

    def test_chase_checking_and_credit(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement(
            "test/test_files/Test_ChaseCheckingAcc.csv"
        )
        chase_transaction_parser.parse_statement(
            "test/test_files/Chase_CreditCard_Test_Sample.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transactions()
        assert report.ignore_payment == -5700.00
        assert report.total_income == 2300.00
        assert report.total_expense == -981

    def test_amex_credit_card(self):
        report = ReportGenerator()
        amex_transaction_parser = AmericanExpressTransactionParser()
        amex_transaction_parser.parse_statement(
            "test/test_files/Amex_Credit_Card_Sample.csv"
        )
        report.import_transactions(amex_transaction_parser.statement)
        report.filter_transactions()
        assert report.total_expense == -593.00
        assert report.ignore_payment == 1400.00

    def test_citi_credit_card(self):
        report = ReportGenerator()
        citi_transaction_parser = CitiTransactionParser()
        citi_transaction_parser.parse_statement(
            "test/test_files/Citi_Credit_Card_Sample.csv"
        )
        report.import_transactions(citi_transaction_parser.statement)
        report.filter_transactions()
        assert report.total_expense == 0
        assert report.ignore_payment == -1500.00
