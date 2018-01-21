from binance.client import Client
import json
from pathlib import Path


def get_client():
    secret_dir = Path(__file__).parents[1] / '.secret'
    api_key_file = secret_dir / 'api_key.json'
    secret = json.load(api_key_file.open())
    return Client(secret['api_key'], secret['api_secret'])
