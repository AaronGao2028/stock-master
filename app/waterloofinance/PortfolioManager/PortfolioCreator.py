import psycopg2
import yfinance as yf
from datetime import date

conn = psycopg2.connect(
    host="localhost",
    database="stockmaster",
    user="postgres",
    password="password"
)

cur = conn.cursor()



