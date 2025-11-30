# ======================================================
# Main Program – Orchestrates All Modules
# ======================================================

from utils import log, save_to_csv
from config import DEFAULT_TICKERS, DEFAULT_START
from data_fetch import fetch_data
from data_processing import clean_data, compute_returns
from analysis import analyze_performance, correlation_matrix
from viz import plot_prices, plot_box_returns, plot_correlation_heatmap

# ------------------------------------------------------
# Main execution flow
# ------------------------------------------------------

if __name__ == "__main__":
    log("Starting program execution...")

    # Step 1: Download raw data
    prices = fetch_data(DEFAULT_TICKERS, start=DEFAULT_START)
    save_to_csv(prices, "raw_prices.csv")

    # Step 2: Clean data + compute returns
    prices_clean = clean_data(prices)
    returns = compute_returns(prices_clean)

    # Step 3: Analysis
    summary = analyze_performance(returns)
    corr = correlation_matrix(returns)

    # Step 4: Save analysis results
    save_to_csv(summary, "summary.csv")
    save_to_csv(corr, "correlation.csv")

    # Step 5: Visualization
    plot_prices(prices_clean)
    plot_box_returns(returns)
    plot_correlation_heatmap(corr)

    log("Program finished successfully.")
