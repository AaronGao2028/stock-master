from flask import Flask, request
from flask_cors import CORS, cross_origin

def get_user_preferences():
    app = Flask(__name__)
    CORS(app, support_credentials=True)

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
        
    return {"sector": sector_preferences, "dividend": dividend_preferences, "marketcap": marketcap_preferences, "risk": risk_tolerance}