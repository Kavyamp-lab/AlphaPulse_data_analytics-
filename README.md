# AlphaPulse_data_analytics
Project- Financial Analytics 
 
Project Title: Investment Risk & Volatility Monitor 
Product Brand Name: "AlphaPulse" 
 
Use Case (Production): 
A boutique investment firm requires a high-fidelity, real-time view of their entire portfolio's market risk exposure. The immediate needs include calculating the critical financial metric Value at Risk (VaR) and visualizing dynamic stock correlations to inform effective portfolio diversification strategies. 
 
Product Features: 
● Basic Core Metrics: Standard stock price line charts, volume trading bars, and daily percentage returns. 
● Deep (Production) Analytics: 
   1) Monte Carlo Simulation: Implement a stochastic simulation (minimum 10,000 runs) to forecast the future distribution of portfolio performance, providing a probability-based risk profile. 
   2) Correlation Heatmaps: Dynamic, interactive matrices that instantly show how different financial assets move in relation to one another (positive, negative, or no 
correlation). 
   3) Rolling Volatility: Visualizations showing the 30-day moving standard deviation of returns, a key indicator of market uncertainty. 
 
Implementation Details: 
● Stack: Python (yfinance API for data) → NumPy (Core Mathematical Calculations) → Tableau (Dynamic Financial Visualization). 
● Key Resources: yfinance for robust API data retrieval; NumPy's capabilities for highspeed matrix multiplication (essential for Portfolio Variance calculations).
 This is my Dashboard - https://public.tableau.com/views/AlphaPulse_VaR_Dashboard_twbx/Dashboard1?:language=enUS&publish=yes&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
