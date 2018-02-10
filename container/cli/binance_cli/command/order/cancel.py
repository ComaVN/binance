from binance.client import Client
from collections import OrderedDict
from decimal import Decimal
from util import binance
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("cancel",
        help="Cancel an order",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )
    parser.add_argument("order_id",
        metavar="order-id",
        help="ID of the order to cancel",
    )


def command(args):
    trading_pair = args.symbol.upper()
    asset, market = binance.split_trading_pair(trading_pair)
    order_id = args.order_id
    client = binance.get_client()
    print("Attempting to cancel {trading_pair} order {order_id}".format(
        trading_pair=trading_pair,
        order_id=order_id,
    ))

    result = client.cancel_order(
        symbol=trading_pair,
        orderId=args.order_id,
    )
    if isinstance(result, dict):
        print("Success")
        print(cli_formatter.format([result], 'plain'))
    else:
        print("Failed: {error}".format(error=result))
