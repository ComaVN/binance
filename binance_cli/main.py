import argparse
import re
import sys
from .command import *


def main():
    parser = argparse.ArgumentParser(
        description='Manage Binance trading through the REST API.',
    )
    parser.set_defaults(
        func=parser.print_help,
    )
    subparsers = parser.add_subparsers(
        metavar='<command>',
        help='Command to execute',
    )
    for module_name, module in sys.modules.items():
        if re.match(__package__ + r'\.command\.([a-z][a-z0-9]*)$', module_name):
            module.add_arg_parser(subparsers)

    args = parser.parse_args()
    args.func()
