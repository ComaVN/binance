import argparse
import re
import sys
from .command import *


def main():
    parser = argparse.ArgumentParser(
        description='Manage Binance trading through the REST API.',
    )
    subparsers = parser.add_subparsers(
        dest='command',
        metavar='<command>',
        help='Command to execute',
    )
    commands = {}
    for module_name, module in sys.modules.items():
        m = re.match(__package__ + r'\.command\.([a-z][a-z0-9]*)$', module_name)
        if m:
            module.add_arg_parser(subparsers)
            commands[m.group(1)] = module.command

    args = parser.parse_args()

    commands.get(args.command, parser.print_help)()
