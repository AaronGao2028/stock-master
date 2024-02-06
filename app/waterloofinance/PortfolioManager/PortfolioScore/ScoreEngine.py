def generate_score (stock, sector_preferences, marketcap_preferences, share_turnovers, dividend_preferences, score_factor):
    compatibility_score = 0
    
    # Check if any of the stock's parameters are invalid
    if (stock.sharpe_ratio <= 0 or stock.standard_deviation <= 0):
        compatibility_score = -999
        
    # Check if the stock's sector matches the user's preference
    if (stock.sector in sector_preferences):
        compatibility_score += score_factor["sectormatch"]
        
    # Check if the stock's market cap matches the user's preference
    if ("Micro Cap (0 - $250M)" in marketcap_preferences and stock.marketcap <= 250000000):
        compatibility_score += score_factor["marketcapmatch"]
    elif ("Small Cap ($250M - $2B)" in marketcap_preferences and stock.marketcap <= 2000000000):
        compatibility_score += score_factor["marketcapmatch"]
    elif ("Mid Cap ($2B - $10B)" in marketcap_preferences and stock.marketcap <= 10000000000):
        compatibility_score += score_factor["marketcapmatch"]
    elif ("Large Cap ($10B - $200B)" in marketcap_preferences and stock.marketcap <= 200000000000):
        compatibility_score += score_factor["marketcapmatch"]
    elif ("Mega Cap ($200B +)" in marketcap_preferences and stock.marketcap > 2000000000000):
        compatibility_score += score_factor["marketcapmatch"]
        
    # Checks if the stock's turnover ratio matches the user's preference
    if ("Low (0% - 0.1%)" in share_turnovers and stock.share_turnover <= 0.1):
        compatibility_score += score_factor["turnovermatch"]
    elif ("Medium (0.1% - 0.5%)" in share_turnovers and stock.share_turnover <= 0.5):
        compatibility_score += score_factor["turnovermatch"]
    elif ("High (0.5% - 1.0%)" in share_turnovers and stock.share_turnover <= 1.0):
        compatibility_score += score_factor["turnovermatch"]
    elif ("Ultra High (1.0% +)" in share_turnovers and stock.share_turnover > 1.0):
        compatibility_score += score_factor["turnovermatch"]
        
    # Checks if the stock's dividend yield matches the user's preference
    if ("Low (0% -0.5%)" in dividend_preferences and stock.dividend_yield <= 0.005):
        compatibility_score += score_factor["dividendmatch"]
    elif ("Medium (0.5% - 3%)" in dividend_preferences and stock.dividend_yield <= 0.03):
        compatibility_score += score_factor["dividendmatch"]
    elif ("High (3% - 6%)" in dividend_preferences and stock.dividend_yield <= 0.06):
        compatibility_score += score_factor["dividendmatch"]
    elif ("Ultra High (6% +)" in dividend_preferences and stock.dividend_yield > 0.06):
        compatibility_score += score_factor["dividendmatch"]
        
    return compatibility_score
                            
