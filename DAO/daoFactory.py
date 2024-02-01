import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()

# Commit changes to the database
conn.commit()

# Close the connections to the database
cur.close()
conn.close()