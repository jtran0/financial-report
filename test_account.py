from report_generator.report_generator import ReportGenerator
from transaction_parser.chase_transaction_parser import ChaseTransactionParser


class TestAccount:
    def test_chase_checking(self):
        report = ReportGenerator()
        chase_transaction_parser = ChaseTransactionParser()
        chase_transaction_parser.parse_statement(
            "financial-report/test_files/TestCheckingAcc.csv"
        )
        report.import_transactions(chase_transaction_parser.statement)
        report.generate_expense_report()
        assert report.total_expense == -7000.00
        assert report.total_income == 2300.00
