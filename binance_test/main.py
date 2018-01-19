from binance.client import Client
import json
from pathlib import Path
import sys


def _log(message):
    print(
        message,
        file=sys.stderr,
    )


def main():
    secret_dir = Path(__file__).parents[1] / '.secret'
    api_key_file = secret_dir / 'api_key.json'
    secret = json.load(api_key_file.open())
    client = Client(secret['api_key'], secret['api_secret'])
    print(json.dumps(client.get_account()))
