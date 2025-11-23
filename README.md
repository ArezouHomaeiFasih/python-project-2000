## Market Pulse — Stock Market Analysis

This project analyzes the behavior of different sectors in the stock market.
It collects historical stock price data and evaluates performance, risk, and volatility.
The goal is to identify which stocks or sectors are more volatile, how they are correlated, and how they behave under market stress.

## Dataset

- Source: Yahoo Finance via yfinance Python library

- Stocks analyzed in this project include:

 - AAPL (Apple Inc.)

 - MSFT (Microsoft Corp.)

 - GOOGL (Alphabet Inc.)

 - AMZN (Amazon.com Inc.)

Historical period: Configurable (default start date: 2022-01-01)

## Requirements
Install dependencies using:
```bash

pip install -r requirements.txt


The required Python packages include:

yfinance for downloading stock data

pandas for data manipulation

numpy for numerical computations

matplotlib and seaborn for data visualization

Project Structure
MarketPulse/
├── data/
│   └── raw_prices.csv         # Raw stock price data (optional)
├── src/
│   └── main.py                # Main script: download, process, analyze, visualize
├── README.md                  # Project documentation
├── .gitignore                 # Files and folders to ignore in Git
└── requirements.txt           # Python dependencies

How to Run

Clone the repository:

git clone https://github.com/your-username/MarketPulse.git


Navigate to the project folder:

cd MarketPulse


Install dependencies:

pip install -r requirements.txt


Run the main script:

python src/main.py


The program will:

Download stock price data from Yahoo Finance

Clean and process the data

Compute performance metrics such as annual return, volatility, and Sharpe ratio

Compute the correlation matrix between stocks

Save summary and correlation data as CSV files

Generate visualizations including price trends, return distributions, and correlation heatmaps

Analysis and Visualizations

Descriptive statistics for stock performance

Boxplots showing return distributions

Correlation heatmap to visualize relationships between stocks

Time series plots of stock prices over the selected period

Interpretation

The analysis helps identify:

Stocks with higher volatility and risk

Stocks with better performance metrics

How different stocks move together in the market

Patterns during market fluctuations

Author