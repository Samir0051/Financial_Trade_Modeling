#!/usr/bin/env python3
"""
A minimal script to test fetching data from Yahoo Finance via yfinance.
"""

import sys

try:
    import yfinance as yf
except ImportError:
    print("Please install dependencies by running 'pip install -r requirements.txt'")
    sys.exit(1)

def fetch_and_print_close(ticker_symbol: str):
    """
    Fetches the last month's closing prices for the given ticker
    and prints them to stdout.
    """
    # Create a Ticker object
    ticker = yf.Ticker(ticker_symbol)

    # Fetch historical market data for the last month
    hist = ticker.history(period="1mo")
    if hist.empty:
        print(f"No data retrieved for {ticker_symbol}")
        return

    print(f"\nClosing prices for {ticker_symbol} over the past month:\n")
    print(hist["Close"].to_string())

if __name__ == "__main__":
    symbol = "AAPL"  # default ticker
    if len(sys.argv) > 1:
        symbol = sys.argv[1].upper()
    fetch_and_print_close(symbol)
