# Mean Reversion Trading Strategy

## Objective
To design and evaluate a rule-based mean-reversion trading strategy using historical equity data.

## Methodology
- Computed daily returns from adjusted closing prices
- Used rolling mean and volatility to compute z-score
- Defined rule-based entry and exit conditions
- Evaluated performance using annualized Sharpe ratio

## Experiments
The same strategy was tested across multiple assets:
- AAPL
- SPY
- MSFT

## Results
- Strategy underperformed on strongly trending assets (AAPL, SPY)
- Achieved positive risk-adjusted returns on MSFT
- Demonstrated asset- and regime-dependent behavior

## Tools
Python, Pandas, NumPy, yFinance, Matplotlib
