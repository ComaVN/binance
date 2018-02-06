from binance.client import Client
from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("mine",
        help="Show a list of my own trades",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum trades",
    )
    parser.add_argument("--format", "-f",
        choices=[
            "json",
            "plain",
        ],
        default="plain",
        help="How to display the result",
    )


def command(args):
    client = get_client()
    trades = client.get_my_trades(
        symbol=args.symbol.upper(),
    )
    result = [
        OrderedDict(sorted(row.items(),
            key=lambda t: t[0],
        ))
        for row in trades
    ]
    print(cli_formatter.format(result, args.format))
