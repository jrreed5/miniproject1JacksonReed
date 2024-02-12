# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf


# Function to fetch stock data
def fetch_stock_data(stock_symbols, period="10d"):
    data = yf.download(stock_symbols, period=period)["Adj Close"]
    return data


# List of favorite stock tickers
tickers = ["TTWO", "MSFT", "GOOGL", "AMZN", "AAPL"]

# Fetching stock data for the last 10 trading days
stock_data = fetch_stock_data(tickers, period="10d")

# Convert data to a numpy array
stock_array = np.array(stock_data)

# Plotting the stock data
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(stock_data.index, stock_data[ticker], label=ticker)

plt.title("Closing Price")
plt.xlabel("Date")
plt.ylabel("Value")
plt.legend()
plt.grid(True)

# Saving the plot as PNG
for ticker in tickers:
    plt.figure()
    plt.plot(stock_data.index, stock_data[ticker])
    plt.title(f"Closing Prices of {ticker}")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.grid(True)
    plt.savefig(f"images/{ticker}_closing_prices.png")

plt.show()
