import os
from binance.client import Client


def get_client():
    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API keys not found. Set BINANCE_API_KEY and BINANCE_API_SECRET.")

    client = Client(api_key, api_secret)

    # Futures Testnet URL
    client.FUTURES_URL = "https://testnet.binancefuture.com"

    return client
