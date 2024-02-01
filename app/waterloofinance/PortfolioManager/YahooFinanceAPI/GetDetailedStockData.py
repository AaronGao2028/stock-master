import yfinance as yf

def get_detailed_stock_date (ticker):
    # Get stock data from Yahoo Finance API
    stock = yf.Ticker(ticker)
    info = stock.info
    
    return info
    