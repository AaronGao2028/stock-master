import pandas as pd

def deposit_customized_portfolio (cur, info):    
    cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='portfolio'")
    table_exist = bool(cur.rowcount)
    
    if (table_exist):
        cur.execute("DROP TABLE portfolio;")
        cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")
        
        for i in range (len(info)):
            stock_info = info[i]
            
            ticker = stock_info.ticker
            name = stock_info.name
            price = stock_info.price
            marketcap = stock_info.marketcap
            dividend_yield = stock_info.dividend_yield
            pe = stock_info.pe
            beta = stock_info.beta
            sector = stock_info.sector
            industry = stock_info.industry
            volume = stock_info.volume
            payout_ratio = stock_info.payout_ratio
            peg_ratio = stock_info.peg_ratio
            revenue_per_share = stock_info.revenue_per_share
            standard_deviation = stock_info.standard_deviation
            sharpe_ratio = stock_info.sharpe_ratio
            sharesOutstanding = stock_info.shares_outstanding
            shareTurnover = stock_info.share_turnover
            compatibilityScore = stock_info.compatibility_score
            riskScore = stock_info.risk_score
            allocation = stock_info.allocation
            
            cur.execute(f"INSERT INTO portfolio VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio}, {sharesOutstanding}, {shareTurnover}, {compatibilityScore}, {riskScore}, {allocation})")
    else:
        cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")      
        for i in range (len(info)):
            stock_info = info[i]
            
            ticker = stock_info.ticker
            name = stock_info.name
            price = stock_info.price
            marketcap = stock_info.marketcap
            dividend_yield = stock_info.dividend_yield
            pe = stock_info.pe
            beta = stock_info.beta
            sector = stock_info.sector
            industry = stock_info.industry
            volume = stock_info.volume
            payout_ratio = stock_info.payout_ratio
            peg_ratio = stock_info.peg_ratio
            revenue_per_share = stock_info.revenue_per_share
            standard_deviation = stock_info.standard_deviation
            sharpe_ratio = stock_info.sharpe_ratio
            sharesOutstanding = stock_info.shares_outstanding
            shareTurnover = stock_info.share_turnover
            compatibilityScore = stock_info.compatibility_score
            riskScore = stock_info.risk_score
            allocation = stock_info.allocation
            
            cur.execute(f"INSERT INTO portfolio VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio}, {sharesOutstanding}, {shareTurnover}, {compatibilityScore}, {riskScore}, {allocation})")
