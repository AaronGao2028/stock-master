import psycopg2
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from app.waterloofinance.PortfolioManager.Dao import DepositDetailedStockData
from YahooFinanceAPI import GetDetailedStockData

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
    info = GetDetailedStockData.get_detailed_stock_date(ticker)
    DepositDetailedStockData.load_detailed_stock_date(cur, ticker, info)

# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()


