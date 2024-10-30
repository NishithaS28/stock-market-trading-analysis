import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the stock data (AAPL_intraday.csv)
data = pd.read_csv('../data/AAPL_intraday.csv', index_col='date', parse_dates=True)

# Calculate Simple Moving Averages (SMA)
data['SMA_20'] = data['4. close'].rolling(window=20).mean()
data['SMA_50'] = data['4. close'].rolling(window=50).mean()

# Generate buy/sell signals
data['Signal'] = 0
data['Signal'][20:] = np.where(data['SMA_20'][20:] > data['SMA_50'][20:], 1, 0)
data['Position'] = data['Signal'].diff()

# Save signals
data.to_csv('../data/AAPL_signals.csv')
print("Trade signals saved as AAPL_signals.csv")

# Plot the signals
plt.figure(figsize=(10,6))
plt.plot(data['4. close'], label='Stock Price')
plt.plot(data['SMA_20'], label='20-day SMA')
plt.plot(data['SMA_50'], label='50-day SMA')
plt.scatter(data.index, data['Position'] == 1, color='green', label='Buy Signal', marker='^', alpha=1)
plt.scatter(data.index, data['Position'] == -1, color='red', label='Sell Signal', marker='v', alpha=1)
plt.title('AAPL Stock Price and Trade Signals')
plt.legend()
plt.show()
