import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from Stock import BuildStockList
from Stock import Stock
import pickle
import psycopg2

f = open("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager\\Property\\scoreFactor.json")
score_factor = json.load(f)

stocks = BuildStockList.build_stock_list()

app = Flask(__name__)
CORS(app, support_credentials=True)

sector_preferences = []
marketcap_preferences = []
dividend_preferences = []
risk_tolerance = []
share_turnovers = []
portfolio_count = 0
form_data = []

@app.route("/form", methods=['GET', 'POST'])
@cross_origin(supports_credentials=True)
def get_form_data():
    portfolio = []
    
    if request.method == 'POST':
        conn = psycopg2.connect(
            host="localhost",
            database="stockmaster",
            user="postgres",
            password="password"
        )

        cur = conn.cursor()
        
        form_data = request.json
        sector_preferences=form_data[0]
        marketcap_preferences=form_data[1]
        share_turnovers = form_data[2]
        dividend_preferences = form_data[3]
        risk_tolerance = form_data[4]
        portfolio_count = form_data[5]
        total_risk = 0

        for i in range(len(stocks)):
            # Check if the stock's sector matches the user's preference
            if (stocks[i].sector in sector_preferences):
                stocks[i].compatibility_score += score_factor["sectormatch"]
                
            # Check if the stock's market cap matches the user's preference
            if ("Micro Cap (0 - $250M)" in marketcap_preferences and stocks[i].marketcap <= 250000000):
                stocks[i].compatibility_score += score_factor["marketcapmatch"]
            elif ("Small Cap ($250M - $2B)" in marketcap_preferences and stocks[i].marketcap <= 2000000000):
                stocks[i].compatibility_score += score_factor["marketcapmatch"]       
            elif ("Mid Cap ($2B - $10B)" in marketcap_preferences and stocks[i].marketcap <= 10000000000):
                stocks[i].compatibility_score += score_factor["marketcapmatch"]
            elif ("Large Cap ($10B - $200B)" in marketcap_preferences and stocks[i].marketcap <= 200000000000):
                stocks[i].compatibility_score += score_factor["marketcapmatch"]
            elif ("Mega Cap ($200B +)" in marketcap_preferences and stocks[i].marketcap > 2000000000000):
                stocks[i].compatibility_score += score_factor["marketcapmatch"]
                
            # Checks if the stock's turnover ratio matches the user's preference
            if ("Low (0% - 0.1%)" in share_turnovers and stocks[i].share_turnover <= 0.1):
                stocks[i].compatibility_score += score_factor["turnovermatch"]
            elif ("Medium (0.1% - 0.5%)" in share_turnovers and stocks[i].share_turnover <= 0.5):
                stocks[i].compatibility_score += score_factor["turnovermatch"]
            elif ("High (0.5% - 1.0%)" in share_turnovers and stocks[i].share_turnover <= 1.0):
                stocks[i].compatibility_score += score_factor["turnovermatch"]
            elif ("Ultra High (1.0% +)" in share_turnovers and stocks[i].share_turnover > 1.0):
                stocks[i].compatibility_score += score_factor["turnovermatch"]
                
            # Checks if the stock's dividend yield matches the user's preference
            if ("Low (0% -0.5%)" in dividend_preferences and stocks[i].dividend_yield <= 0.005):
                stocks[i].compatibility_score += score_factor["dividendmatch"]
            elif ("Medium (0.5% - 3%)" in dividend_preferences and stocks[i].dividend_yield <= 0.03):
                stocks[i].compatibility_score += score_factor["dividendmatch"]
            elif ("High (3% - 6%)" in dividend_preferences and stocks[i].dividend_yield <= 0.06):
                stocks[i].compatibility_score += score_factor["dividendmatch"]  
            elif ("Ultra High (6% +)" in dividend_preferences and stocks[i].dividend_yield > 0.06):
                stocks[i].compatibility_score += score_factor["dividendmatch"]  
                                    
            # Check if the stock's standard deviation of returns is within the user's preferences
            if ("Low (± 2% - 5%)" in risk_tolerance and stocks[i].standard_deviation <= 0.05):
                stocks[i].compatibility_score += score_factor["riskmatch"]
            elif ("Medium (± 5% - 10%)" in risk_tolerance and stocks[i].standard_deviation <= 0.10):
                stocks[i].compatibility_score += score_factor["riskmatch"]
            elif ("High (± 10% - 20%)" in risk_tolerance and stocks[i].standard_deviation <= 0.20):
                stocks[i].compatibility_score += score_factor["riskmatch"]
            elif ("Ultra High (± 20% +)" in risk_tolerance and stocks[i].standard_deviation > 0.20):
                stocks[i].compatibility_score += score_factor["riskmatch"]
        
        # Sort stocks by compatibility score
        new_stocks = sorted(stocks, key=lambda x: x.compatibility_score, reverse=True)
        
        # Determine the total sharpe ratio of the stocks in portfolio
        for i in range(portfolio_count):
            total_risk += new_stocks[i].sharpe_ratio
        
        # Use individual sharpe ratio to determine allocation of stock
        for i in range(portfolio_count):
            new_stocks[i].allocation = new_stocks[i].sharpe_ratio/total_risk
            portfolio.append(new_stocks[i])
        import pandas as pd    
        
        cur.execute(f"SELECT * FROM information_schema.tables WHERE table_name='portfolio'")
        table_exist = bool(cur.rowcount)
     
        if (table_exist):
            cur.execute("DROP TABLE portfolio;")            
            cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")
            
            for i in range (portfolio_count):
                s = new_stocks[i]
                cur.execute(f"INSERT INTO portfolio VALUES ('{s.ticker}', '{s.name}', {s.price}, {s.marketcap}, {s.dividend_yield}, {s.pe}, {s.beta}, '{s.sector}', '{s.industry}', {s.volume}, {s.payout_ratio}, {s.peg_ratio}, {s.revenue_per_share}, {s.standard_deviation}, {s.sharpe_ratio}, {s.shares_outstanding}, {s.share_turnover}, {s.compatibility_score}, {s.risk_score}, {s.allocation})")
        else:
            cur.execute("CREATE TABLE portfolio (ticker VARCHAR PRIMARY KEY, name VARCHAR, price FLOAT, marketcap FLOAT, dividend_yield FLOAT, pe FLOAT, beta FLOAT, sector VARCHAR, industry VARCHAR, volume FLOAT, payout_ratio FLOAT, peg_ratio FLOAT, revenue_per_share FLOAT, standard_deviation FLOAT, sharpe_ratio FLOAT, shares_outstanding FLOAT, share_turnover FLOAT, compatiblity_score FLOAT, risk_score FLOAT, allocation FLOAT)")

            for i in range (portfolio_count):
                s = new_stocks[i]
                cur.execute(f"INSERT INTO portfolio VALUES ('{s.ticker}', '{s.name}', {s.price}, {s.marketcap}, {s.dividend_yield}, {s.pe}, {s.beta}, '{s.sector}', '{s.industry}', {s.volume}, {s.payout_ratio}, {s.peg_ratio}, {s.revenue_per_share}, {s.standard_deviation}, {s.sharpe_ratio}, {s.shares_outstanding}, {s.share_turnover}, {s.compatibility_score}, {s.risk_score}, {s.allocation})")

        # Commit changes to the database
        conn.commit()
        
        # Close the connections to the database
        cur.close()
        conn.close()
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

if __name__ == "__main__":
    app.run(debug=True)
    