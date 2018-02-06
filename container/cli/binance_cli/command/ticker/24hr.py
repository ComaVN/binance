from binance.client import Client
from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("24hr",
        help="Show 24 hour price change statistics",
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


def command(args):
    client = get_client()
    ticker = client.get_ticker(
        symbol=args.symbol.upper(),
    )
    result = [ticker]
    print(cli_formatter.format(result, args.format))
