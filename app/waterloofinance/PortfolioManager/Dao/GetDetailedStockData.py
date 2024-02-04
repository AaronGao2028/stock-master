import json
import psycopg2

def get_detailed_stock_data():
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
    query = "SELECT * FROM stocks"
    cursor.execute(query)

    # Fetch all rows and convert to a list of dictionaries
    rows = cursor.fetchall()
    result = []
    for row in rows:
        d = {}
        for i, col in enumerate(cursor.description):
            d[col[0]] = row[i]
            result.append(d)

    # Convert the list of dictionaries to JSON and print it
    json_result = json.dumps(result)

    # Commit changes to the database
    conn.commit()

    # Close the connections to the database
    cursor.close()
    conn.close()
    
    return json_result