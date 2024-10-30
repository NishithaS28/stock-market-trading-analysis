import pandas as pd

# Load the signals data
data = pd.read_csv('../data/AAPL_signals.csv')

# Simulate trades based on signals
initial_balance = 100000  # Start with $100,000
position = 0
balance = initial_balance
for i in range(len(data)):
    if data['Position'].iloc[i] == 1 and position == 0:  # Buy
        position = balance / data['4. close'].iloc[i]
        balance = 0
        print(f"Bought {position:.2f} shares at {data['4. close'].iloc[i]} on {data['date'].iloc[i]}")
    elif data['Position'].iloc[i] == -1 and position > 0:  # Sell
        balance = position * data['4. close'].iloc[i]
        position = 0
        print(f"Sold shares at {data['4. close'].iloc[i]} on {data['date'].iloc[i]}")

# Print final balance
print(f"Final Balance: ${balance:.2f}")
