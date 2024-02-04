from flask import Flask, request
from flask_cors import CORS, cross_origin

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
    return sector_preferences

@app.route("/dividend_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_dividend_preferences():
    dividend_preferences = request.json
    print(dividend_preferences)
    return dividend_preferences

@app.route("/marketcap_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_marketcap_preferences():
    marketcap_preferences = request.json
    print(marketcap_preferences)
    return marketcap_preferences

@app.route("/shareturnover_preferences", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_shareturnover_preferences():
    share_turnovers = request.json
    print(share_turnovers)
    return share_turnovers

@app.route("/risk_tolerance", methods=["POST"])
@cross_origin(supports_credentials=True)
def get_risktolerance_preferences():
    risk_tolerance = request.json
    print(risk_tolerance)
    return risk_tolerance

def get_user_preferences():
    return {"sector": sector_preferences, "dividend": dividend_preferences, "marketcap": marketcap_preferences, "turnover": share_turnovers, "risk": risk_tolerance}

if __name__ == "__main__":
    app.run(debug=True)