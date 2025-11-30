# ======================================================
# Data Downloading Module – Yahoo Finance API
# ======================================================

import yfinance as yf
import pandas as pd
from datetime import datetime
from utils import log

def fetch_data(tickers: list, start: str = "2020-01-01", end: str = None) -> pd.DataFrame:
    """
    Download stock price data using Yahoo Finance.
    """
    if end is None:
        end = datetime.now().strftime("%Y-%m-%d")

    log(f"Downloading data from {start} to {end} for: {', '.join(tickers)}")

    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True
    )["Close"]

    log("Data download completed.")
    return data
