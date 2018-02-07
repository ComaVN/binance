from binance.client import Client
from collections import OrderedDict
from decimal import Decimal
from util import binance
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("sell-2pct-up",
        help="Place a sell order 2%% above the highest bid in the order book",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )
    parser.add_argument("quantity",
        help="Amount of the asset to sell",
        type=Decimal,
        nargs="?",
        default=None,
    )
    parser.add_argument("--force",
        help="Actually create the order. If not specified, a dry-run/test is done",
        action="store_true",
    )


def command(args):
    trading_pair = args.symbol.upper()
    quantum = Decimal(10) ** -6
    client = binance.get_client()
    latest_price = Decimal(client.get_symbol_ticker(
        symbol=trading_pair,
    )["price"])
    order_book = client.get_order_book(
        symbol=trading_pair,
        limit=5,
    )
    highest_bid = Decimal(order_book["bids"][0][0])
    price = (highest_bid * Decimal("1.02")).quantize(quantum)
    if price <= 0 or price <= latest_price:
        print("Failed to place sell order because a safeguard failed: intended price ({price}) lower than or equal to 0 or latest price ({latest_price})".format(
            price=price,
            latest_price=latest_price,
        ))
        return
    if args.quantity is None:
        quantity = Decimal(client.get_asset_balance(binance.get_asset_from_trading_pair(trading_pair))["free"])
    else:
        quantity = Decimal(args.quantity)
    print("Attempting to place sell order of {quantity} {trading_pair} for price {price} (highest bid: {highest_bid}, latest price {latest_price}),".format(
        quantity=quantity,
        trading_pair=trading_pair,
        price=price,
        highest_bid=highest_bid,
        latest_price=latest_price,
    ))
    if args.force:
        func = client.create_order
    else:
        print("(Dry-run only, use --force to actually place the order)")
        func = client.create_test_order

    result = func(
        symbol=trading_pair,
        side=Client.SIDE_SELL,
        type=Client.ORDER_TYPE_LIMIT,
        timeInForce='GTC',
        quantity=quantity,
        price=price,
    )
    if isinstance(result, dict):
        print("Success")
        print(cli_formatter.format([result], 'plain'))
    else:
        print("Failed: {error}".format(error=result))
