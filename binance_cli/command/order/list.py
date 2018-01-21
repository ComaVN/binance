import json
from util.binance import get_client


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('list',
        help='Show a list of orders',
    )
    parser.set_defaults(
        func=command,
    )


def command():
    client = get_client()
    print(json.dumps(
        client.get_all_orders(
            symbol='NEOETH',
        ),
        indent=2,
        sort_keys=True,
    ))
