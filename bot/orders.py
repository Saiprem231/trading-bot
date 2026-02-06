import logging
from .client import get_client


def place_market_order(symbol, side, quantity):
    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="MARKET",
            quantity=float(quantity)
        )

        logging.info(f"Market Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Market Order Failed: {str(e)}")
        raise


def place_limit_order(symbol, side, quantity, price):
    client = get_client()

    try:
        order = client.futures_create_order(
            symbol=symbol.upper(),
            side=side.upper(),
            type="LIMIT",
            quantity=float(quantity),
            price=str(price),
            timeInForce="GTC"
        )

        logging.info(f"Limit Order Response: {order}")
        return order

    except Exception as e:
        logging.error(f"Limit Order Failed: {str(e)}")
        raise
