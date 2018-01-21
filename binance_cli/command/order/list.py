from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('list',
        help='Show a list of orders',
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument('--format', '-f',
        choices=[
            'json',
            'plain',
        ],
        default='plain',
    )


def command(args):
    client = get_client()
    orders = client.get_all_orders(
        symbol='NEOETH',
    )
    result = [
        OrderedDict(sorted(row.items(),
            key=lambda t: t[0],
        ))
        for row in orders
    ]
    print(cli_formatter.format(result, args.format))
