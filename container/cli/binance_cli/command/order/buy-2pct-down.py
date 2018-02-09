from binance.client import Client
from collections import OrderedDict
from decimal import Decimal
from util import binance
from util import cli_formatter


def add_arg_parser(subparsers):
    parser = subparsers.add_parser("buy-2pct-down",
        help="Place a buy order 2%% below the lowest ask in the order book",
    )
    parser.set_defaults(
        func=command,
    )
    parser.add_argument("symbol",
        help="Symbol for the trading pair, eg. NEOETH for NEO / Ethereum",
    )
    parser.add_argument("quantity",
        help="Amount of the asset to buy",
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
    latest_price = Decimal(client.get_symbol_ticker(
        symbol=trading_pair,
    )["price"])
    order_book = client.get_order_book(
        symbol=trading_pair,
        limit=5,
    )
    lowest_ask = Decimal(order_book["asks"][0][0])
    price = (lowest_ask * Decimal("0.98")).quantize(price_quantum)
    safeguards = []
    if price <= 0:
        safeguards.append("Price ({price}) not positive".format(
            price=price,
        ))
    if price >= latest_price:
        safeguards.append("Price ({price}) is not below latest price ({latest_price})".format(
            price=price,
            latest_price=latest_price,
        ))
    if safeguards:
        print("Failed to place buy order because safeguards failed:")
        print("\n".join(safeguards))
        return
    if args.quantity is None:
        quantity = (Decimal(client.get_asset_balance(market)["free"]) / price).quantize(quantity_quantum)
    else:
        quantity = Decimal(args.quantity)
    print("Attempting to place buy order of {quantity} {asset} @ {price} {market} (lowest ask: {lowest_ask}, latest price {latest_price}),".format(
        quantity=quantity,
        asset=asset,
        market=market,
        price=price,
        lowest_ask=lowest_ask,
        latest_price=latest_price,
    ))
    if args.force:
        func = client.create_order
    else:
        print("(Dry-run only, use --force to actually place the order)")
        func = client.create_test_order

    result = func(
        symbol=trading_pair,
        side=Client.SIDE_BUY,
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
