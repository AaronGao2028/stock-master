import json
from flask import Flask, jsonify, request
from Dao import GetDetailedStockData
from flask_cors import CORS, cross_origin

stock_info = GetDetailedStockData.get_detailed_stock_data()

app = Flask(__name__)
CORS(app, support_credentials=True)

@app.route("/stocks")
@cross_origin(supports_credentials=True)
def get_stock_info():
    return stock_info

sector_preferences = []
dividend_preferences = []
marketcap_preferences = []
risk_tolerance = []

@app.route("/sector_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_sector_preferences():
    sector_preferences = request.json
    return ""

@app.route("/dividend_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_dividend_preferences():
    dividend_preferences = request.json
    return ""

@app.route("/marketcap_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_dividend_preferences():
    marketcap_preferences = request.json
    return ""

@app.route("/risk_tolerance", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_dividend_preferences():
    risk_tolerance = request.json
    return ""

if __name__ == "__main__":
    app.run(debug=True)
    
