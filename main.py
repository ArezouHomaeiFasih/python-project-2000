import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# ---------------------------
# utils.py - Utility Functions
# ---------------------------

def log(message: str) -> None:
    """
    Print a timestamped log message.

    Parameters:
        message (str): The message to print.
    """
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}")


def save_to_csv(df: pd.DataFrame, filename: str) -> None:
    """
    Save a pandas DataFrame to a CSV file.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        filename (str): The name of the output CSV file.
    """
    df.to_csv(filename, index=True)
    log(f"Data saved to file: {filename}")


# ---------------------------
# data_fetch.py - Data Downloading
# ---------------------------

def fetch_data(tickers: list, start: str = "2020-01-01", end: str = None) -> pd.DataFrame:
    """
    Download historical stock price data using Yahoo Finance API.

    Parameters:
        tickers (list): List of stock tickers (e.g., ["AAPL", "MSFT"]).
        start (str): Start date for the data in 'YYYY-MM-DD' format.
        end (str): End date for the data in 'YYYY-MM-DD' format. Defaults to today.

    Returns:
        pd.DataFrame: Adjusted close prices for the given tickers.
    """
    if end is None:
        end = datetime.now().strftime("%Y-%m-%d")
    log(f"Downloading data from {start} to {end} for: {', '.join(tickers)}")
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    log("Data download completed.")
    return data


# ---------------------------
# data_processing.py - Data Cleaning and Preparation
# ---------------------------

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean the stock price data by removing missing or zero values.

    Parameters:
        df (pd.DataFrame): Raw data with possible NaNs or zero columns.

    Returns:
        pd.DataFrame: Cleaned DataFrame ready for analysis.
    """
    log("Cleaning data...")
    df = df.dropna()
    df = df.loc[:, (df != 0).any(axis=0)]
    log("Data cleaned successfully.")
    return df


def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compute daily percentage returns of the stock prices.

    Parameters:
        df (pd.DataFrame): Cleaned stock price data.

    Returns:
        pd.DataFrame: Daily returns of each stock.
    """
    log("Calculating daily returns...")
    returns = df.pct_change().dropna()
    return returns


# ---------------------------
# analysis.py - Data Analysis
# ---------------------------

def analyze_performance(returns: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze performance metrics for each stock, including annual return,
    volatility, and Sharpe ratio.

    Parameters:
        returns (pd.DataFrame): Daily returns of stocks.

    Returns:
        pd.DataFrame: Summary of performance metrics for each ticker.
    """
    log("Analyzing stock performance...")
    mean_returns = returns.mean() * 252  # Annualized return
    volatility = returns.std() * np.sqrt(252)  # Annualized volatility
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
    Compute the correlation matrix of stock returns.

    Parameters:
        returns (pd.DataFrame): Daily returns of stocks.

    Returns:
        pd.DataFrame: Correlation matrix between tickers.
    """
    log("Computing correlation matrix...")
    return returns.corr()


# ---------------------------
# viz.py - Visualization
# ---------------------------

def plot_prices(df: pd.DataFrame) -> None:
    """
    Plot stock prices over time.

    Parameters:
        df (pd.DataFrame): Cleaned stock price data.
    """
    plt.figure(figsize=(10, 5))
    df.plot()
    plt.title("Stock Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.grid(True)
    plt.show()


def plot_box_returns(returns: pd.DataFrame) -> None:
    """
    Plot boxplots showing the distribution of daily returns.

    Parameters:
        returns (pd.DataFrame): Daily returns of stocks.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=returns)
    plt.title("Return Distributions")
    plt.show()


def plot_correlation_heatmap(corr: pd.DataFrame) -> None:
    """
    Plot a heatmap of the correlation matrix.

    Parameters:
        corr (pd.DataFrame): Correlation matrix of stock returns.
    """
    plt.figure(figsize=(7, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()


# ---------------------------
# Main Program Execution
# ---------------------------

if __name__ == "__main__":
    log("Starting program execution...")

    # Define stock tickers to analyze
    tickers = ["AAPL", "MSFT", "GOOGL", "AMZN"]

    # Step 1: Download data
    prices = fetch_data(tickers, start="2022-01-01") # Downloading data from 2022-01-01 to 2025-10-31 for: AAPL, MSFT, GOOGL, AMZN
    save_to_csv(prices, "raw_prices.csv")

    # Step 2: Clean and prepare data
    prices_clean = clean_data(prices)
    returns = compute_returns(prices_clean)

    # Step 3: Analyze performance and risk
    summary = analyze_performance(returns)
    corr = correlation_matrix(returns)

    # Step 4: Save outputs
    save_to_csv(summary, "summary.csv")
    save_to_csv(corr, "correlation.csv")

    # Step 5: Visualization
    plot_prices(prices_clean)
    plot_box_returns(returns)
    plot_correlation_heatmap(corr)

    log("Program finished successfully.")
