from binance.client import Client
from collections import OrderedDict
from prettytable import PrettyTable
from util.binance import get_client


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("book",
        help="Show the order book",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )


def command(args):
    client = get_client()
    order_book = client.get_order_book(
        symbol=args.symbol.upper(),
        limit=10,
    )
    order_book['asks'].reverse()
    for side in ("asks", "bids"):
        print("{side}:".format(side=side))
        table = PrettyTable()
        table.field_names = ("price", "quantity")
        for row in order_book[side]:
            table.add_row((row[0], row[1]))
        print(table.get_string())
