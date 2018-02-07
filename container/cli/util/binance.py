from binance.client import Client
import json
import os
from pathlib import Path
import re


def get_client():
    secret_dir = Path(os.environ["BINANCE_SECRET_DIR"]) if "BINANCE_SECRET_DIR" in os.environ else Path(__file__).parents[1] / ".secret"
    api_key_file = secret_dir / "api_key.json"
    secret = json.load(api_key_file.open())
    return Client(secret["api_key"], secret["api_secret"])

def get_asset_from_trading_pair(trading_pair):
    for market in ("BTC", "ETH", "BNB", "USDT"):
        m = re.search(r"^(\w+){market}$".format(market=market), trading_pair)
        if m:
            return m.group(1)
