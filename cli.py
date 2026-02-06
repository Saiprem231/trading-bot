import argparse
import logging

from bot.orders import place_market_order, place_limit_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)
from bot.logging_config import setup_logging


def main():
    setup_logging()

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True)
    parser.add_argument("--side", required=True)
    parser.add_argument("--type", required=True)
    parser.add_argument("--quantity", required=True)
    parser.add_argument("--price", required=False)

    args = parser.parse_args()

    try:
        # Validation
        validate_symbol(args.symbol)
        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)
        validate_price(args.price, args.type)

        logging.info(f"Order Request: {vars(args)}")

        print("\n===== ORDER REQUEST SUMMARY =====")
        print(f"Symbol   : {args.symbol}")
        print(f"Side     : {args.side}")
        print(f"Type     : {args.type}")
        print(f"Quantity : {args.quantity}")
        if args.price:
            print(f"Price    : {args.price}")

        # Order Execution
        if args.type.upper() == "MARKET":
            response = place_market_order(
                args.symbol,
                args.side,
                args.quantity
            )
        else:
            response = place_limit_order(
                args.symbol,
                args.side,
                args.quantity,
                args.price
            )

        print("\n✅ ORDER SUCCESS")
        print("Order ID:", response.get("orderId"))
        print("Status:", response.get("status"))
        print("Executed Qty:", response.get("executedQty"))
        print("Avg Price:", response.get("avgPrice", "N/A"))

        logging.info(f"Order Success Response: {response}")

    except Exception as e:
        print("\n❌ ORDER FAILED")
        print("Error:", str(e))
        logging.error(f"Order Failed: {str(e)}")


if __name__ == "__main__":
    main()
