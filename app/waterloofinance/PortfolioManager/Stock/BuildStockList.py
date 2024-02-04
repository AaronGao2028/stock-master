from Stock import Stock
from Dao import GetDetailedStockData
import json

def build_stock_list():
    stock_info = GetDetailedStockData.get_detailed_stock_data()

    arr = json.loads(stock_info)
    stocks = []
    for i in range(len(arr)):
        stock_data = arr[i]
        stocks.append(Stock.Stock(
            stock_data[0], stock_data[1], stock_data[2], stock_data[3],
            stock_data[4], stock_data[5], stock_data[6], stock_data[7],
            stock_data[8], stock_data[9], stock_data[10], stock_data[11],
            stock_data[12], stock_data[13], stock_data[14], stock_data[15], 
            stock_data[16], 0, 0, 0))
        
    return stocks