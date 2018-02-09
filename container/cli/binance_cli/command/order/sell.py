from binance.client import Client
from collections import OrderedDict
from decimal import Decimal
from util import binance
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("sell",
        help="Place a sell order",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )
    parser.add_argument("price",
        help="Price to ask for the asset",
        type=Decimal,
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
    asset, market = binance.split_trading_pair(trading_pair)
    price_quantum = Decimal(10) ** -6 # RH: This should come from client.get_exchange_info (cached)
    quantity_quantum = Decimal(10) ** -2 # RH: This should come from client.get_exchange_info (cached)
    client = binance.get_client()
    order_book = client.get_order_book(
        symbol=trading_pair,
        limit=5,
    )
    highest_bid = Decimal(order_book["bids"][0][0])
    price = args.price
    safeguards = []
    if price <= 0:
        safeguards.append("Price ({price}) not positive".format(
            price=price,
        ))
    if price < highest_bid:
        safeguards.append("Price ({price}) is below highest bid ({highest_bid})".format(
            price=price,
            highest_bid=highest_bid,
        ))
    if safeguards:
        print("Failed to place sell order because safeguards failed:")
        print("\n".join(safeguards))
        return
    if args.quantity is None:
        quantity = Decimal(client.get_asset_balance(asset)["free"])
    else:
        quantity = Decimal(args.quantity)
    print("Attempting to place sell order of {quantity} {asset} @ {price} {market} (highest bid: {highest_bid}),".format(
        quantity=quantity,
        asset=asset,
        market=market,
        price=price,
        highest_bid=highest_bid,
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
