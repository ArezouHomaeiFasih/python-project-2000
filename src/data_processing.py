# ======================================================
# Data Cleaning & Return Calculation
# ======================================================

import pandas as pd
from utils import log

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove rows with NaN values and remove all-zero columns.
    """
    log("Cleaning data...")
    df = df.dropna()
    df = df.loc[:, (df != 0).any(axis=0)]
    log("Data cleaned successfully.")
    return df


def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage returns.
    """
    log("Calculating daily returns...")
    returns = df.pct_change().dropna()
    return returns
