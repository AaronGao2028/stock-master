import psycopg2
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from Dao import DepositDetailedStockData, CreateDetailedStockTable
from YahooFinanceAPIAdaptor import GetDetailedStockData

file_path = "C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager\\Property\\tickers.txt"
file = open (file_path, "r")

# Open database connection
conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()

CreateDetailedStockTable.create_detailed_stock_table(cur)

# Loop through tickers
for ticker in file:
    ticker = ticker.lower().strip()
    # Get dictionary of stocks and load into database
    info = GetDetailedStockData.get_detailed_stock_date(ticker)
    # Deposit the stock information into database
    DepositDetailedStockData.load_detailed_stock_date(cur, ticker, info)
 
# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()


