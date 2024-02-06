import json
from flask import Flask, request
from flask_cors import CORS, cross_origin
import sys

import psycopg2
from PortfolioScore import ScoreEngine
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from Stock import BuildStockList
import CovarianceMatrixCalculator
import PortfolioAllocation
from Dao import DepositCustomizedPortfolio

def build_customized_portfolio (form_data):
    # Open database connection
    conn = psycopg2.connect(
        host="localhost",
        database="stockmaster",
        user="postgres",
        password="password"
    )

    cur = conn.cursor()

    file_path = "C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager\\Property\\scoreFactor.json"
    f = open(file_path)
    score_factor = json.load(f)

    stocks = BuildStockList.build_stock_list()

    sector_preferences=form_data[0]
    marketcap_preferences=form_data[1]
    share_turnovers = form_data[2]
    dividend_preferences = form_data[3]
    risk_tolerance = form_data[4]
    portfolio_count = form_data[5]

    for i in range(len(stocks)):
        # Get the compatibility score of the stock from the score engine
        compatibility_score = ScoreEngine.generate_score(stocks[i], sector_preferences, marketcap_preferences, share_turnovers, dividend_preferences, score_factor)
        # Assign the compatibility score
        stocks[i].compatibility_score = compatibility_score
        
    # Sort stocks by compatibility score
    sorted_stocks = sorted(stocks, key=lambda x: x.compatibility_score, reverse=True)
    
    # Take the top n stocks where n represents the number of stocks the user would like in their portfolio
    portfolio = sorted_stocks[:portfolio_count]
    
    # Get the covariance matrix of the portfolio
    covariance_matrix = CovarianceMatrixCalculator.calculate_covariance_matrix(portfolio)
    
    risk_adjusted_portfolio = PortfolioAllocation.allocate_portfolio(covariance_matrix, portfolio)
    
    DepositCustomizedPortfolio.deposit_customized_portfolio(cur, risk_adjusted_portfolio)
    
    # Commit changes to the database
    conn.commit()

    # Close the connections to the database
    cur.close()
    conn.close()

    return risk_adjusted_portfolio
    
    
    
    
    
    
        



    