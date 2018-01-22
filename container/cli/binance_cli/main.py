import argparse
import importlib


def main():
    parser = argparse.ArgumentParser(
        description='Manage Binance trading through the REST API.',
    )
    parser.set_defaults(
        func=lambda dummy: parser.print_help(),
    )
    subparsers = parser.add_subparsers(
        metavar='<command>',
        help='Command to execute',
    )
    commands = {
        'account',
        'order',
    }
    for command in commands:
        module = importlib.import_module(__package__ + '.command.' + command)
        module.add_arg_parser(subparsers)

    args = parser.parse_args()
    args.func(args)
