# momentum-investing-methods
Momentum Investing Backtesting and Simulation using Pure price based Momentum and Volatility-Adjusted Returns on NIFTY 50.

This backtest is done from **2015 to 2025**.

Momentum Investing is a way of investing in which we prefer high momentum stocks that are currently outperforming the market and try to capture these sustained movements so that they will outperform the market in the future too.

**How is it done ?**

Rank Stocks according to some criteria (2 ways are discussed below) in the decided **lookback period** and select** top-n stocks**. Ex-1 month, 3 month, 6 month, 12month etc. We can also use a combination of these lookback periods. Select top-n stocks and hold in the portfolio until the next rebalancing date. The stocks could be assigned an equal weight in the portfolio or can be assigned custom weights.Ex- Top 5 stocks account for 50% and next 10 stocks account for remaining 50%. Hold this portfolio till the next rebalancing date and continue the same.

There are 2 ways of Stocks Selection discussed here.
1) **Pure Price Based Momentum**
Rank Stocks according to **% Rate Of Change in Price (ROC**) in the decided lookback period and select top-n stocks.

Also check out the **Momentum Dashboard** from the repositories.It combines 3 timeframes 1M,3M,6M.
Ranks the stocks based on ROC and gives them a score according to the percentile.
Then displays stocks having ranks > 90 in all 3 timeframes.

**2) Volatility-Adjusted Returns**
Rank Stocks according to a **volatility based score** in the decided lookback period and select top-n stocks.
**Score = ROC/ Std dev**
This finds out stocks displaying highest momentum but also with less standard deviation (less volatility) in those returns.

RESULTS:-
**CAGR**
Index: 0.1312
Price Momentum: 0.1123
Volatility Adjusted: 0.1578

**Max Drawdown**
Index: 0.2934
Price Momentum: 0.2067
Volatility Adjusted: 0.0900

**Annual Volatility**
Index: 0.1631
Price Momentum: 0.1478
Volatility Adjusted: 0.1573

**Sharpe Ratio**
Index: 0.5366
Price Momentum: 0.9544
Volatility Adjusted: 1.3406

Volatility Adjusted Portfolio has outperformed both Index and the Price momentum portfolio in all aspects showccasing higher CAGR, higher Sharpe ratio, lower Max Drawdown.



