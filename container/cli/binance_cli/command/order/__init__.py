import importlib


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('order',
        help='Order related commands',
    )
    parser.set_defaults(
        func=lambda dummy: parser.print_help(),
    )
    subparsers = parser.add_subparsers(
        metavar='<subcommand>',
        help='Order subcommand to execute',
    )
    subcommands = {
        'list',
    }
    for subcommand in subcommands:
        module = importlib.import_module(__package__ + '.' + subcommand)
        module.add_arg_parser(subparsers)
