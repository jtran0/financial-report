from report_generator.report_generator import ReportGenerator
from transaction_parser.chase_transaction_parser import ChaseTransactionParser


class TestAccount:
    def test_chase_checking(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement("test_files/Test_ChaseCheckingAcc.csv")
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transations()
        assert report.ignore_payment == -7000
        assert report.total_income == 2300.00

    def test_chase_credit_card(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement(
            "test_files/Chase_CreditCard_Test_Sample.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transations()
        assert report.total_expense == -981
        assert report.ignore_payment == 1300

    def test_chase_checking_and_credit(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement("test_files/Test_ChaseCheckingAcc.csv")
        chase_transaction_parser.parse_statement(
            "test_files/Chase_CreditCard_Test_Sample.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.filter_transations()
        assert report.ignore_payment == -5700.00
        assert report.total_income == 2300.00
        assert report.total_expense == -981
