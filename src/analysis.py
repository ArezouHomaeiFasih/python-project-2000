# ======================================================
# Stock Performance Analysis (Returns, Volatility, Sharpe)
# ======================================================

import numpy as np
import pandas as pd
from utils import log

def analyze_performance(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Compute annual return, volatility and Sharpe ratio.
    """
    log("Analyzing stock performance...")

    mean_returns = returns.mean() * 252
    volatility = returns.std() * np.sqrt(252)
    sharpe_ratio = mean_returns / volatility

    summary = pd.DataFrame({
        "Annual Return": mean_returns,
        "Volatility": volatility,
        "Sharpe Ratio": sharpe_ratio
    })

    log("Performance analysis completed.")
    return summary


def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Compute correlation matrix of stock returns.
    """
    log("Computing correlation matrix...")
    return returns.corr()
