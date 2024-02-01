import psycopg2
from datetime import date
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from app.waterloofinance.PortfolioManager.Dao import DepositHistoricalData
from YahooFinanceAPI import GetHistoricalData

file = open ("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager\\Build\\tickers.txt", "r")

# Open database connection
conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()

# Loop through tickers
for ticker in file:
    ticker = ticker.lower().strip()
    # Get dictionary of stocks and load into database
    stocks = GetHistoricalData.get_historical_date(ticker, '2015-01-01', date.today(), '1d')
    DepositHistoricalData.load_historical_date(cur, stocks, ticker)

# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()


