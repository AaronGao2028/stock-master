def load_historical_date (cur, stocks, ticker):
    print(ticker)
    
    cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='{ticker}'")
    table_exist = bool(cur.rowcount)

    if (table_exist):
        for i in range (len (stocks)):
            price = stocks.loc[i, "Open"]
            date = stocks.loc[i, "Date"]
            cur.execute(f"SELECT EXISTS(SELECT 1 FROM {ticker} WHERE date='{date}')")
            date_exist = cur.fetchall()

            if (not date_exist):
               cur.execute(f"INSERT INTO {ticker} VALUES ('{date}', {price})")
    else:        
        cur.execute(f"CREATE TABLE {ticker} (date VARCHAR PRIMARY KEY, price FLOAT);")

        for i in range (len (stocks)):
            price = stocks.loc[i, "Open"]
            date = stocks.loc[i, "Date"]
            cur.execute(f"INSERT INTO {ticker} VALUES ('{date}', {price})")
            
    cur.commit


