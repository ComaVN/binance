import importlib


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('trade',
        help='Trade related commands',
    )
    parser.set_defaults(
        func=lambda dummy: parser.print_help(),
    )
    subparsers = parser.add_subparsers(
        metavar='<subcommand>',
        help='Trade subcommand to execute',
    )
    subcommands = {
        'mine',
    }
    for subcommand in subcommands:
        module = importlib.import_module(__package__ + '.' + subcommand)
        module.add_arg_parser(subparsers)
