import re
import sys
from . import list


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('order',
        help='Order related commands',
    )
    parser.set_defaults(
        func=parser.print_help,
    )
    subparsers = parser.add_subparsers(
        metavar='<subcommand>',
        help='Order subcommand to execute',
    )
    for module_name, module in sys.modules.items():
        if re.match(__package__ + r'\.([a-z][a-z0-9]*)$', module_name):
            module.add_arg_parser(subparsers)
