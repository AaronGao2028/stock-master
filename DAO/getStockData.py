import psycopg2
import yfinance as yf
from datetime import date
import pandas as pd

start_date =  '2015-01-01'
end_date = date.today()
interval = '1d'
risk_free_return = 4.80

conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()

cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='stocks'")
table_exist = bool(cur.rowcount)

if (not table_exist):
    cur.execute("CREATE TABLE stocks (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT)")

file = open("tickers.txt", "r")

for x in file:
    ticker = x.lower().strip()
    print(ticker)
    
    # Calculate annualized standard deviation of returns and Sharpe's ratio for each stock
    cur.execute(f"SELECT price FROM (SELECT *, row_number() over() rn FROM {ticker}) foo WHERE foo.rn % 365 = 0;")
    arr = cur.fetchall()
    for i in range(len(arr)):
        arr[i] = arr[i][0]
    temp = arr[0]
    
    std = [0]*(len(arr)-1)
        
    for i in range (len(arr)):
        if (i > 0):
            std[i-1] = (arr[i] - arr[i-1])/arr[i-1]
    std = pd.Series(std)
    avg = std.mean()
    std = std.std()

    # Get stock data from Yahoo Finance API
    stock = yf.Ticker(ticker)
    info = stock.info

    name = info['shortName'].replace("'","")
    price = info['open']    

    try:
        marketcap = info['marketCap']       
    except:
        marketcap = -999
        
    try:
        dividend_yield = info['dividendYield']       
    except:
        dividned_yield = -999
            
    try:
        pe = info['trailingPE']
    except:
        pe = -999
            
    try:
        beta = info['beta']
    except:
        beta = -999
            
    try:
        sector = info['sector']
    except:
        sector = -999
        
    try:
        industry = info['industry']
    except:
        industry = -999

    try:
        volume = info['volume']
    except:
        volume = -999
    
    try:
        payout_ratio = info['payoutRatio']    
    except:
        payout_ratio = -999
        
    try:
        peg_ratio = info['pegRatio']    
    except:
        peg_ratio = -999
        
    try:
        revenue_per_share = info['revenuePerShare']
    except:
        revenue_per_share = -999
        
    if (pd.isna(std)):
        standard_deviation = -999
        sharpe_ratio = -999
    else:
        standard_deviation = std
        sharpe_ratio = (avg - risk_free_return)/standard_deviation
    print (ticker, name, price, marketcap)
    cur.execute(f"SELECT EXISTS(SELECT 1 FROM stocks WHERE ticker='{ticker}')")
    ticker_exist = cur.fetchall()

    if (ticker_exist):
        cur.execute(f"UPDATE stocks SET price = {price}, marketcap = {marketcap}, dividend_yield = {dividend_yield}, pe = {pe}, beta = {beta}, sector = '{sector}', industry = '{industry}', volume = {volume}, payout_ratio = {payout_ratio}, peg_ratio = {peg_ratio}, revenue_per_share = {revenue_per_share}, standard_deviation = {standard_deviation}, sharpe_ratio = {sharpe_ratio} WHERE ticker = '{ticker}'")
    else:
        cur.execute(f"INSERT INTO stocks VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio})")

# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()


