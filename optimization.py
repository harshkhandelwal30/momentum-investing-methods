roc_periods = [3, 6, 12]
stock_numbers = [5, 10, 15, 20, 25, 30]

results = []

for roc_period in roc_periods:
    # Compute ROC for this period
    roc = monthly_prices_df.pct_change(roc_period)
    
    for no_of_stocks in stock_numbers:
        # Build top-N momentum picks
        picks = []
        for date, row in df_month_end.iterrows():
            if date not in roc.index:
                continue
            roc_vals = roc.loc[date, row['Constituents']].dropna()
            top_n = roc_vals.sort_values(ascending=False).head(no_of_stocks)
            for stock, val in top_n.items():
                picks.append({'Date': date, 'Stock': stock})
        picks_df = pd.DataFrame(picks)
        
        # Compute portfolio returns
        returns = monthly_prices_df.pct_change()
        portfolio = []
        for date in picks_df['Date'].unique():
            stocks = picks_df[picks_df['Date'] == date]['Stock'].tolist()
            next_month = date + pd.DateOffset(months=1)
            if next_month not in returns.index:
                continue
            rets = returns.loc[next_month, stocks]
            w = np.ones(len(stocks)) / len(stocks)
            port_ret = np.dot(rets.values, w)
            portfolio.append({'Date': next_month, 'Return': port_ret})
        backtest = pd.DataFrame(portfolio).set_index('Date')
        backtest['Cumulative'] = (1 + backtest['Return']).cumprod()
        
        # Calculate metrics
        cagr = calculate_cagr(backtest['Cumulative'])
        mdd = max_drawdown(backtest['Cumulative'])
        sr = sharpe_ratio(backtest['Return'])
        
        results.append({
            'ROC_Months': roc_period,
            'Num_Stocks': no_of_stocks,
            'CAGR': cagr,
            'Max_Drawdown': mdd,
            'Sharpe': sr
        })

# Compile results
results_df = pd.DataFrame(results)

# Find best combinations
best_cagr = results_df.loc[results_df['CAGR'].idxmax()]
best_sharpe = results_df.loc[results_df['Sharpe'].idxmax()]
least_dd = results_df.loc[results_df['Max_Drawdown'].idxmin()]

print("Best CAGR combination:\n", best_cagr, "\n")
print("Best Sharpe combination:\n", best_sharpe, "\n")
print("Least Max Drawdown combination:\n", least_dd, "\n")

# Display full results table
results_df