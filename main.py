# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 1

import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

tickers = ["TTWO", "MSFT", "GOOGL", "AMZN", "AAPL"]

def getClosing(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="10d")
    closingList = []
    for price in hist['Close']:
        closingList.append(price)
    return closingList


def plotGraph(stock):
    stockClosing = np.array(getClosing(stock))
    days = list(range(1, len(stockClosing)+1))
    plt.plot(days, stockClosing)
    prices = getClosing(stock)
    prices.sort()
    low_price = prices[0]
    high_price = prices[-1]
    plt.axis([1, 10, low_price-2, high_price+2])
    plt.grid(True)
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.title(f"Closing Prices of {stock}")
    plt.savefig(f"images/{stock}.png")
    plt.show()

# !Program runs here!
# Tries to make image path
try:
    Path("images").mkdir()
except FileExistsError:
    pass

tickers = ["TTWO", "MSFT", "GOOGL", "AMZN", "AAPL"]

for stock in tickers:
    getClosing(stock)
    plotGraph(stock)