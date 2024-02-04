import pandas as pd

def deposit_customized_portfolio (cur, info):
    
    cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='portfolio'")
    table_exist = bool(cur.rowcount)
    
    if (table_exist):
        cur.execute("DROP TABLE portfolio;")
        cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")
        cur.execute(f"INSERT INTO stocks VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio}, {sharesOutstanding}, {shareTurnover})")

    else:
        cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")
