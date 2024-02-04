import pandas as pd

def load_detailed_stock_date (cur, ticker, info):
    print (ticker)
    
    risk_free_return = 4.80
    
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

    try:
        name = info['shortName'].replace("'","")
    except:
        name = -999

    try:
        price = info['open']    
    except:
        price = -999
        
    try:
        marketcap = info['marketCap']       
    except:
        marketcap = -999
        
    try:
        dividend_yield = info['dividendYield']       
    except:
        dividend_yield = -999
            
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
        
    try:
        sharesOutstanding = info["sharesOutstanding"]
    except: 
        sharesOutstanding = -999
        
    try:
        shareTurnover = volume/sharesOutstanding
    except:
        shareTurnover = -999
        
    if (pd.isna(std)):
        standard_deviation = -999
        sharpe_ratio = -999
    else:
        standard_deviation = std
        sharpe_ratio = (avg - risk_free_return)/standard_deviation
        
    cur.execute(f"SELECT EXISTS(SELECT 1 FROM stocks WHERE ticker='{ticker}')")
    ticker_exist = cur.fetchall()

    if (ticker_exist[0][0]): 
        cur.execute(f"UPDATE stocks SET price = {price}, marketcap = {marketcap}, dividend_yield = {dividend_yield}, pe = {pe}, beta = {beta}, sector = '{sector}', industry = '{industry}', volume = {volume}, payout_ratio = {payout_ratio}, peg_ratio = {peg_ratio}, revenue_per_share = {revenue_per_share}, standard_deviation = {standard_deviation}, sharpe_ratio = {sharpe_ratio}, shares_outstanding = {sharesOutstanding}, share_turnover = {shareTurnover} WHERE ticker = '{ticker}'")
    else:
        cur.execute(f"INSERT INTO stocks VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio}, {sharesOutstanding}, {shareTurnover})")


