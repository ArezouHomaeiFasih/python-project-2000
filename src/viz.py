# ======================================================
# Visualization Module – Price, Returns, Heatmap
# ======================================================

import matplotlib.pyplot as plt
import seaborn as sns

def plot_prices(df):
    """Plot stock prices over time."""
    plt.figure(figsize=(10, 5))
    df.plot()
    plt.title("Stock Prices Over Time")
    plt.xlabel("Date")
    plt.ylabel("Adjusted Close Price")
    plt.grid(True)
    plt.show()


def plot_box_returns(returns):
    """Boxplot of return distributions."""
    plt.figure(figsize=(8, 5))
    sns.boxplot(data=returns)
    plt.title("Return Distributions")
    plt.show()


def plot_correlation_heatmap(corr):
    """Heatmap of correlation matrix."""
    plt.figure(figsize=(7, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Correlation Matrix")
    plt.show()
