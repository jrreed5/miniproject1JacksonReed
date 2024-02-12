# INF601 - Advanced Programming in Python
# Jackson Reed
# Mini Project 1

import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#(5/5 points) Initial comments with your name, class and project at the top of your .py file.
#(5/5 points) Proper import of packages used.
#(20/20 points) Using an API of your choice , collect the closing price of 5
# of your favorite stock tickers for the last 10 trading days.
#(10/10 points) Store this information in a list that you will convert to a array in NumPy.
#(10/10 points) Plot these 5 graphs. Feel free to add as much information to the graphs as you like exploring
# the documentation for matplotlib. At minimum it just needs to show 10 data points.
#(10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder,
# the project should save these when it executes. You may want to add this folder to your .gitignore file.
#(10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
#(10/10 points) I will be checking out the main branch of your project. Please be sure to include a requirements.txt
# file which contains all the packages that need installed. You can create this file
# with the output of pip freeze at the terminal prompt.
#(20/20 points) There should be a README.md file in your project that explains what your project is,
# how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown.

# Function to fetch stock data
def fetch_stock_data(tickers, period="10d"):
    data = yf.download(tickers, period=period)["Adj Close"]
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
    plt.savefig(f"{ticker}_closing_prices.png")

plt.show()