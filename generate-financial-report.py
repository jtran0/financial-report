#!/usr/bin/env python3
import sys
from argparse import ArgumentParser, RawTextHelpFormatter
from pathlib import Path

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
    argument_parser.add_argument("input", nargs="?")
    argument_parser.add_argument(
        "-o",
        "--output",
        default=".",
        metavar="DIR",
        help="Specify a output directory path",
    )
    return argument_parser.parse_args()


def main():
    args = get_args()


if __name__ == "__main__":
    sys.exit(main())
