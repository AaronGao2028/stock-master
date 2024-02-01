import yfinance as yf

def get_historical_date (ticker, start_date, end_date, interval):
    # Get stock data from Yahoo Finance API
    yf.pdr_override()
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.reset_index(inplace=True) 
    df['date'] = df['Date'].dt.date
    
    return df
