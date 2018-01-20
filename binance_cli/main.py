import argparse
from binance.client import Client
import json
from pathlib import Path
import sys


def _log(message):
    print(
        message,
        file=sys.stderr,
    )


def getClient():
    secret_dir = Path(__file__).parents[1] / '.secret'
    api_key_file = secret_dir / 'api_key.json'
    secret = json.load(api_key_file.open())
    return Client(secret['api_key'], secret['api_secret'])


def main():
    parser = argparse.ArgumentParser(
        description='Manage Binance trading through the REST API.',
    )
    parser.add_argument(
        'command',
        metavar='<command>',
        help='Command to execute',
    )
    args = parser.parse_args()

    {
        'account': account_command,
        'order': order_command,
    }.get(args.command, parser.print_help)()


def account_command():
    client = getClient()
    print(json.dumps(
        client.get_account(),
        indent=2,
        sort_keys=True,
    ))


def order_command():
    client = getClient()
    print(json.dumps(
        client.get_all_orders(
            symbol='NEOETH'
        ),
        indent=2,
        sort_keys=True,
    ))
