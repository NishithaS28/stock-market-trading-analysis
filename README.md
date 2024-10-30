# stock-market-trading-analysis
This project involves creating a microservice for receiving real-time stock data, developing trade algorithms, and automating trade execution to improve trading efficiency.

Features
* Real-time Stock Data Processing: Uses historical intraday data for analysis and backtesting.
* Technical Indicators: Calculates two Simple Moving Averages (SMA) to detect potential trends.
* Buy/Sell Signals: Generates buy/sell signals based on SMA crossovers.
* Strategy Simulation: Backtests the strategy performance compared to a simple buy-and-hold strategy.
* Visualization: Provides plots of stock prices, SMAs, and trade signals.
  
Project Structure

The repository contains the following files:
* AAPL_intraday.csv: Sample stock data for Apple's intraday trading data.
* symbols_valid_meta.csv: Metadata file that holds stock symbol information.
* trade_signals.py: A script that calculates the SMA and generates trading signals.
* trade_execution.py: A script that simulates trade executions and compares strategy performance.
* README.md: The file that explains the project details (this file).
  
Setup Instructions

Prerequisites
Ensure you have the following software and libraries installed:
* Python 3.x


Required Libraries:
* Pandas: pip install pandas
* Matplotlib: pip install matplotlib
* NumPy: pip install numpy

  

![Stock Price with Buy/Sell Signals](stock_price_buy_sell_signals.png)
![Strategy vs Market Returns](strategy_vs_market_returns.png)

