import importlib


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('account',
        help='Account related commands',
    )
    parser.set_defaults(
        func=parser.print_help,
    )
    subparsers = parser.add_subparsers(
        metavar='<subcommand>',
        help='Account subcommand to execute',
    )
    subcommands = {
        'balance',
    }
    for subcommand in subcommands:
        module = importlib.import_module(__package__ + '.' + subcommand)
        module.add_arg_parser(subparsers)
