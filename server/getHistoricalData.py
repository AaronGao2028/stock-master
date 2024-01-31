import psycopg2
import yfinance as yf
from datetime import date

start_date =  '2015-01-01'
end_date = date.today()
interval = '1d'

conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()

def trimZero(str):
    newStr = ""
    for i in range (len(str)):
        if (str[i] == '/'):
            newStr += '-'
        elif (str[i] != ' '):
            newStr += str[i]
    return newStr

file = open("tickers.txt", "r")

for x in file:
    ticker = x.lower().strip()
    print(ticker)
    
    # Get stock data from Yahoo Finance API
    yf.pdr_override()
    df = yf.download(tickers=ticker, start=start_date, end=end_date, interval=interval)
    df.reset_index(inplace=True) 
    df['date'] = df['Date'].dt.date

    cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='{ticker}'")
    table_exist = bool(cur.rowcount)

    if (table_exist):
        for i in range (len (df)):
            price = df.loc[i, "Open"]
            date = df.loc[i, "Date"]
            cur.execute(f"SELECT EXISTS(SELECT 1 FROM {ticker} WHERE date='{date}')")
            date_exist = cur.fetchall()

            if (not date_exist):
               cur.execute(f"INSERT INTO {ticker} VALUES ('{date}', {price})")
    else:        
        cur.execute(f"CREATE TABLE {ticker} (date VARCHAR PRIMARY KEY, price FLOAT);")

        for i in range (len (df)):
            price = df.loc[i, "Open"]
            date = df.loc[i, "Date"]
            cur.execute(f"INSERT INTO {ticker} VALUES ('{date}', {price})")

# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()


