#!/usr/bin/env python3
import sys
import os
from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path
from transaction_parser.chase_transaction_parser import ChaseTransactionParser
from transaction_parser.amex_transaction_parser import AmericanExpressTransactionParser
from transaction_parser.citi_transaction_parser import CitiTransactionParser
from transaction_parser.wells_fargo_transaction_parser import (
    WellsFargoTransactionParser,
)
from report_generator.report_generator import ReportGenerator

DESCRIPTION = """\
Generate a financial report

Example usage:
{filename}
""".format(
    filename=Path(__file__).name
)


def get_args():
    argument_parser = ArgumentParser(
        description=DESCRIPTION, formatter_class=RawTextHelpFormatter
    )

    def colon_separated(arg):
        bank_type, filepath = arg.split(":")
        return bank_type, os.path.expanduser(filepath)

    argument_parser.add_argument("input", nargs="*", type=colon_separated)
    argument_parser.add_argument(
        "-o",
        "--output",
        default="./financial-report.txt",
        metavar="FILE",
        help="Specify a output file path",
    )
    return argument_parser.parse_args()


def main():
    args = get_args()
    report_generator = ReportGenerator()

    for bank, filepath in args.input:
        print(bank, filepath)
        if bank == "chase":
            chase_transaction_parser = ChaseTransactionParser()
            chase_transaction_parser.parse_statement(filepath)
            report_generator.import_transactions(chase_transaction_parser.statement)
        elif bank == "amex":
            amex_transaction_parser = AmericanExpressTransactionParser()
            amex_transaction_parser.parse_statement(filepath)
            report_generator.import_transactions(amex_transaction_parser.statement)
        elif bank == "citi":
            citi_transaction_parser = CitiTransactionParser()
            citi_transaction_parser.parse_statement(filepath)
        elif bank == "wellsfargo":
            wells_fargo_transaction_parser = WellsFargoTransactionParser()
            wells_fargo_transaction_parser.parse_statement(filepath)
    report_generator.filter_transations()


if __name__ == "__main__":
    sys.exit(main())
