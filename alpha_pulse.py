import yfinance as yf
import pandas as pd
import numpy as np

# ---- 1. Define stocks ----
stocks = ['AAPL','MSFT','GOOG','AMZN','TSLA']

# ---- 2. Download stock data safely ----
data = yf.download(stocks, start="2020-01-01", auto_adjust=True, threads=True)
prices = data['Close']

# Drop any stock with all NaNs (failed download)
missing = prices.columns[prices.isnull().all()]
if len(missing) > 0:
    print(f"Warning: No data for {missing.tolist()}, removing from analysis")
    prices = prices.drop(columns=missing)

# Save prices for future use
prices.to_csv("../data/price_data.csv")

# ---- 3. Daily returns ----
returns = prices.fillna(method='ffill').pct_change().dropna()
returns.to_csv("../data/daily_returns.csv")

# ---- 4. Rolling 30-day volatility ----
rolling_vol = returns.rolling(30).std()
rolling_vol.to_csv("../data/rolling_volatility.csv")

# ---- 5. Correlation matrix ----
corr = returns.corr()
corr.to_csv("../data/correlation_matrix.csv")

# Remove index/column names to avoid reset_index conflict
corr.index.name = None
corr.columns.name = None

# Reshape to long format for Tableau
corr_long = corr.stack().reset_index(name='Correlation')
corr_long.columns = ['Stock1', 'Stock2', 'Correlation']
corr_long.to_csv("../data/correlation_long.csv", index=False)
print("Reshaped correlation CSV saved as correlation_long.csv")

# ---- 6. Monte Carlo simulation ----
mean_returns = returns.mean()
cov_matrix = returns.cov()

# Adjust weights to number of available stocks
weights = np.array([1/len(returns.columns)] * len(returns.columns))
num_simulations = 10000

# Run Monte Carlo simulation safely
simulated_returns = np.random.multivariate_normal(
    mean_returns.values, cov_matrix.values, num_simulations
)

portfolio_sim = simulated_returns @ weights
pd.DataFrame(portfolio_sim, columns=["Portfolio_Return"]).to_csv(
    "../data/monte_carlo.csv", index=False
)

# ---- 7. Value at Risk (VaR 95%) ----
VaR_95 = np.percentile(portfolio_sim, 5)
print("VaR (95% confidence):", VaR_95)
