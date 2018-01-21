from binance.client import Client
import json
from pathlib import Path


def add_arg_parser(subparsers):
    parser = subparsers.add_parser('order',
        help='Order related commands',
    )


def get_client():
    secret_dir = Path(__file__).parents[2] / '.secret'
    api_key_file = secret_dir / 'api_key.json'
    secret = json.load(api_key_file.open())
    return Client(secret['api_key'], secret['api_secret'])


def command():
    client = get_client()
    print(json.dumps(
        client.get_all_orders(
            symbol='NEOETH',
        ),
        indent=2,
        sort_keys=True,
    ))
