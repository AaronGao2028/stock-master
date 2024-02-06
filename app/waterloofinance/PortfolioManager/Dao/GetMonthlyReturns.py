import psycopg2

def get_monthly_returns (ticker):
    # Open database connection
    conn = psycopg2.connect(
        host="localhost",
        database="stockmaster",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()
    
    cur.execute(f"SELECT price FROM (SELECT *, row_number() over() rn FROM {ticker}) foo WHERE foo.rn % 30 = 0 AND date >= '2023-01-01' AND date <= '2024-01-01';")
    monthly_returns = cur.fetchall()
    
    # Commit changes to the database
    conn.commit()

    # Close the connections to the database
    cur.close()
    conn.close()
        
    return monthly_returns
    
    