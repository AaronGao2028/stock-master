import pandas as pd

def load_detailed_stock_date (cur, ticker, info):
    print (ticker)
    
    risk_free_return = 4.80

    try:
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
        name = info['shortName'].replace("'","")
        price = info['open']    
        marketcap = info['marketCap']       
        dividend_yield = info['dividendYield']       
        pe = info['trailingPE']
        beta = info['beta']
        sector = info['sector']
        industry = info['industry']
        volume = info['volume']
        payout_ratio = info['payoutRatio']    
        peg_ratio = info['pegRatio']    
        revenue_per_share = info['revenuePerShare']
        sharesOutstanding = info["sharesOutstanding"]
        shareTurnover = volume/sharesOutstanding
        standard_deviation = std
        sharpe_ratio = (avg - risk_free_return)/standard_deviation
        
        cur.execute(f"SELECT EXISTS(SELECT 1 FROM stocks WHERE ticker='{ticker}')")
        ticker_exist = cur.fetchall()

        if (ticker_exist[0][0]): 
            cur.execute(f"UPDATE stocks SET price = {price}, marketcap = {marketcap}, dividend_yield = {dividend_yield}, pe = {pe}, beta = {beta}, sector = '{sector}', industry = '{industry}', volume = {volume}, payout_ratio = {payout_ratio}, peg_ratio = {peg_ratio}, revenue_per_share = {revenue_per_share}, standard_deviation = {standard_deviation}, sharpe_ratio = {sharpe_ratio}, shares_outstanding = {sharesOutstanding}, share_turnover = {shareTurnover} WHERE ticker = '{ticker}'")
        else:
            cur.execute(f"INSERT INTO stocks VALUES ('{ticker}', '{name}', {price}, {marketcap}, {dividend_yield}, {pe}, {beta}, '{sector}', '{industry}', {volume}, {payout_ratio}, {peg_ratio}, {revenue_per_share}, {standard_deviation}, {sharpe_ratio}, {sharesOutstanding}, {shareTurnover})")
    except: 
        print("ERROR")
