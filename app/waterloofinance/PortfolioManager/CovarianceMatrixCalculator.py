import numpy as np
import sys
sys.path.append("C:\\Users\\aaron\\Stock Master PERN\\app\\waterloofinance\\PortfolioManager")
from Dao import GetMonthlyReturns

def calculate_covariance_matrix(portfolio):
    monthly_prices = [[0 * 8] * len(portfolio) for i in range(len(portfolio))]
    monthly_returns =  [[0 * 7] * len(portfolio) for i in range(len(portfolio))]

    for i in range(len(portfolio)):
        monthly_prices[i] = GetMonthlyReturns.get_monthly_returns(portfolio[i].ticker)
    
    for i in range(len(portfolio)):
        for j in range (7):
            monthly_returns[i][j] = 100*(monthly_prices[i][j+1][0]-monthly_prices[i][j][0])/monthly_prices[i][j][0]
            
    data = np.array(monthly_returns).squeeze()

    cov_matrix = np.cov(data,bias=True)  
      
    return cov_matrix
    
