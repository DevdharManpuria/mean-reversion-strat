import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# DATA
data = yf.download("MSFT", start="2020-01-01", end="2024-01-01")
# yfinance returns multi-index columns (Price, Ticker)
# We extract only MSFT prices for clean analysis
data = data.xs("MSFT", level=1, axis=1)

# RETURN CALCULATION
data["Return"] = data["Close"].pct_change()

# SIGNAL CONSTRUCTION
window = 20
# Rolling statistics define "normal" behavior
data["Mean"] = data["Close"].rolling(window).mean()
data["Std"] = data["Close"].rolling(window).std()
# Z-score normalizes price deviations
data["Z"] = (data["Close"] - data["Mean"]) / data["Std"]

# TRADING LOGIC
data["Position"] = 0
# Entry rules
data.loc[data["Z"] < -1, "Position"] = 1    # Long
data.loc[data["Z"] > 1, "Position"] = -1   # Short
# Exit rule (neutral zone)
data.loc[data["Z"].abs() < 0.2, "Position"] = 0
# Hold position until exit condition is met
data["Position"] = data["Position"].ffill()

# STRATEGY RETURNS
# Shift position to avoid look-ahead bias
data["Strategy_Return"] = data["Position"].shift(1) * data["Return"]

# PERFORMANCE METRIC
sharpe_ratio = (
    data["Strategy_Return"].mean() / data["Strategy_Return"].std()) * np.sqrt(252) 
print(f"Annualized Sharpe Ratio: {sharpe_ratio:.3f}")

# VISUALIZATION
data["Strategy_Return"].cumsum().plot(
    title="Mean Reversion Strategy – Cumulative Returns (MSFT)",
    figsize=(10, 5)
)
plt.xlabel("Date")
plt.ylabel("Cumulative Return")
plt.grid(True)
plt.show()
