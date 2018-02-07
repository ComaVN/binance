from binance.client import Client
from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("list",
        help="Show a list of orders",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )
    parser.add_argument("--format", "-f",
        choices=[
            "json",
            "plain",
        ],
        default="plain",
        help="How to display the result",
    )
    parser.add_argument("--all", "-a",
        action="store_true",
        help="Show all orders. The default is to only show open orders",
    )


def command(args):
    statuses = {
        Client.ORDER_STATUS_NEW,
        Client.ORDER_STATUS_PARTIALLY_FILLED,
    }
    client = get_client()
    orders = client.get_all_orders(
        symbol=args.symbol.upper(),
    )
    result = [
        OrderedDict(sorted(row.items(),
            key=lambda t: t[0],
        ))
        for row in orders
        if args.all or row["status"] in statuses
    ]
    print(cli_formatter.format(result, args.format))
