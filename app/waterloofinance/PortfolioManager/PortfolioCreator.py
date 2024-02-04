import json
from flask import Flask, jsonify, request
from Dao import GetDetailedStockData
from flask_cors import CORS, cross_origin
from Stock import Stock

stock_info = GetDetailedStockData.get_detailed_stock_data()

app = Flask(__name__)
CORS(app, support_credentials=True)

sector_preferences = []
dividend_preferences = []
marketcap_preferences = []
risk_tolerance = []
share_turnovers = []

@app.route("/sector_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_sector_preferences():
    sector_preferences = request.json
    print(sector_preferences)
    return ""

@app.route("/dividend_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_dividend_preferences():
    dividend_preferences = request.json
    print(dividend_preferences)
    return ""

@app.route("/marketcap_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_marketcap_preferences():
    marketcap_preferences = request.json
    print(marketcap_preferences)
    return ""

@app.route("/shareturnover_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_shareturnover_preferences():
    share_turnovers = request.json
    print(share_turnovers)
    return ""

@app.route("/risk_tolerance", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_risktolerance_preferences():
    risk_tolerance = request.json
    print(risk_tolerance)
    return ""

arr = json.loads(stock_info)
stocks = []

for i in range(len(arr)):
    stock_data = arr[i]
    stocks.append(Stock(stock_data[0], stock_data[1], stock_data[2], stock_data[3], stock_data[4], stock_data[5], stock_data[6], stock_data[7], stock_data[8], stock_data[9], stock_data[10], stock_data[11], stock_data[12], stock_data[13], stock_data[14], stock_data[15], stock_data[16], 0, 0))
    print(stocks[i].ticker)
    print("________________________________________")

print(len(arr))
if __name__ == "__main__":
    app.run(debug=True)