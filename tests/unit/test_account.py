import pytest
from report_generator.report_generator import ReportGenerator
from transaction_parser.chase_transaction_parser import ChaseTransactionParser
from transaction_parser.amex_transaction_parser import AmericanExpressTransactionParser
from transaction_parser.citi_transaction_parser import CitiTransactionParser


@pytest.fixture
def chase_checking_parser():
    parser = ChaseTransactionParser()
    parser.parse_statement("test_files/Test_ChaseCheckingAcc.csv")
    return parser


@pytest.fixture
def chase_credit_card_parser():
    parser = ChaseTransactionParser()
    parser.parse_statement("test_files/Chase_CreditCard_Test_Sample.csv")
    return parser


@pytest.fixture
def amex_credit_card_parser():
    parser = AmericanExpressTransactionParser()
    parser.parse_statement("test_files/Amex_Credit_Card_Sample.csv")
    return parser


@pytest.fixture
def citi_credit_card_parser():
    parser = CitiTransactionParser()
    parser.parse_statement("test_files/Citi_Credit_Card_Sample.csv")
    return parser


class TestAccount:
    def test_chase_checking(self, chase_checking_parser):
        report = ReportGenerator()
        report.import_transactions(chase_checking_parser.statement)
        report.filter_transactions()
        assert report.ignore_payment == -7000
        assert report.total_income == 2300.00

    def test_chase_credit_card(self, chase_credit_card_parser):
        report = ReportGenerator()
        report.import_transactions(chase_credit_card_parser.statement)
        report.filter_transactions()
        assert report.total_expense == -981
        assert report.ignore_payment == 1300

    def test_chase_checking_and_credit(
        self, chase_checking_parser, chase_credit_card_parser
    ):
        report = ReportGenerator()
        report.import_transactions(chase_checking_parser.statement)
        report.import_transactions(chase_credit_card_parser.statement)
        report.filter_transactions()
        assert report.ignore_payment == -5700.00
        assert report.total_income == 2300.00
        assert report.total_expense == -981

    def test_amex_credit_card(self, amex_credit_card_parser):
        report = ReportGenerator()
        report.import_transactions(amex_credit_card_parser.statement)
        report.filter_transactions()
        assert report.total_expense == -593.00
        assert report.ignore_payment == 1400.00

    def test_citi_credit_card(self, citi_credit_card_parser):
        report = ReportGenerator()
        report.import_transactions(citi_credit_card_parser.statement)
        report.filter_transactions()
        assert report.total_expense == 0
        assert report.ignore_payment == -1500.00
