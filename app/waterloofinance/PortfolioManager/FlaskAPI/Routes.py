import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
import pickle
import psycopg2
import PortfolioCreator
from Dao import GetHistoricalData

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/form", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_form_data():    
    if request.method == 'POST':        
        form_data = request.json
        portfolio = PortfolioCreator.build_customized_portfolio(form_data)
        print(portfolio)
        return pickle.dumps(portfolio)
    elif request.method == 'GET':   
        conn = psycopg2.connect(
            host="localhost",
            database="stockmaster",
            user="postgres",
            password="password"
        )

        cur = conn.cursor()
        
        cur.execute("SELECT * FROM portfolio;")
        portfolio = cur.fetchall()

        new_portfolio = []
        
        for i in range(len(portfolio)):
            s = portfolio[i]
            # Ticker
            new_portfolio.append(s[0])
            # Name
            new_portfolio.append(s[1])
            # Price
            new_portfolio.append(s[2])
            # Market Cap
            new_portfolio.append(s[3])
            # Dividend
            new_portfolio.append(s[4])
            # Sector
            new_portfolio.append(s[7])
            # Standard Deviation
            new_portfolio.append(s[13])
            # Sharpe Ratio
            new_portfolio.append(s[14])
            # Allocation
            new_portfolio.append(s[19])

        return json.dumps(new_portfolio)

@app.route("/historical", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_historical_data():    
    if request.method == 'GET':
        ticker = request.args.get('ticker')
        data = GetHistoricalData.get_historical_data(ticker)
        
        return json.dumps(data)
    
if __name__ == "__main__":
    app.run(debug=True)
    