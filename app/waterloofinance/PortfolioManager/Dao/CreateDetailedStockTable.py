def create_detailed_stock_table(cur):
    # Check if table stocks exist
    cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='stocks'")
    table_exist = bool(cur.rowcount)

    # Create a new table if neccessary
    if (not table_exist):
        cur.execute("CREATE TABLE stocks (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT)")
