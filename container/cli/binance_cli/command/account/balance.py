from collections import OrderedDict
from util.binance import get_client
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("balance",
        help="Show the coin balances of the account",
    )
    parser.set_defaults(
        func=command,
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
        help="Show the balance for all coins. The default is to only show non-zero balances",
    )


def command(args):
    client = get_client()
    account = client.get_account()
    result = [
        OrderedDict(sorted(row.items(),
            key=lambda t: t[0],
        ))
        for row in account["balances"]
        if args.all or float(row["free"]) > 0 or float(row["locked"]) > 0
    ]
    result.sort(
        key=lambda row: row["asset"],
    )
    print(cli_formatter.format(result, args.format))
