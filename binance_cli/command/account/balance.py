from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('balance',
        help='Show the coin balances of the account',
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
    account = client.get_account()
    result = [
        OrderedDict(sorted(row.items(),
            key=lambda t: t[0],
        ))
        for row in account['balances']
    ]
    print(cli_formatter.format(result, args.format))
