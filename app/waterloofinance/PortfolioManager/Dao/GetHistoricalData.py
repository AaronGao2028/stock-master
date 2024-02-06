import json
import psycopg2

def get_historical_data(ticker):
    # Open database connection
    conn = psycopg2.connect(
        host="localhost",
        database="stockmaster",
        user="postgres",
        password="password"
    )

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the SQL query
    cursor.execute(f"SELECT * FROM {ticker}")

    # Fetch all rows and convert to a list of dictionaries
    result = list(cursor.fetchall())

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result)

    # Commit changes to the database
    conn.commit()

    # Close the connections to the database
    cursor.close()
    conn.close()
    
    return json_result