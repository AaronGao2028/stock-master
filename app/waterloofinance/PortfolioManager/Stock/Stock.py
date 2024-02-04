class Stock:
    def __init__(self, ticker, name, price, marketcap, dividend_yield, pe, beta, sector, industry, volume, payout_ratio, peg_ratio, revenue_per_share, standard_deviation, sharpe_ratio, shares_outstanding, share_turnover, compatiblity_score, risk_score, allocation):
        self.ticker = ticker
        self.name = name
        self.price = price
        self.marketcap = marketcap
        self.dividend_yield = dividend_yield
        self.pe = pe
        self.beta = beta
        self.sector = sector
        self.industry = industry
        self.volume = volume
        self.payout_ratio = payout_ratio
        self.peg_ratio = peg_ratio
        self.revenue_per_share = revenue_per_share
        self.standard_deviation = standard_deviation
        self.sharpe_ratio = sharpe_ratio
        self.shares_outstanding = shares_outstanding
        self.share_turnover = share_turnover
        self.compatibility_score = compatiblity_score
        self.risk_score = risk_score
        self.allocation = allocation
        
def print_stock (stock):
    print("Ticker: " + stock.ticker, "Name: " + stock.name, "Price: " + str(stock.price), "Market Cap: " + str(stock.marketcap), "Dividend Yield: "+ str(stock.dividend_yield), "PE: " + str(stock.pe), "Beta: "+ str(stock.beta), "Sector: " + stock.sector, "Industry: " + stock.industry, "Volume: " + str(stock.volume), "Payout Ratio: " + str(stock.payout_ratio), "Peg Ratio: " + str(stock.peg_ratio), "Revenue Per Share: " + str(stock.revenue_per_share), "Standard Deviation: " + str(stock.standard_deviation), "Sharpe Ratio: " + str(stock.sharpe_ratio), "Shares Outstanding: " + str(stock.shares_outstanding), "Share Turnover: " + str(stock.share_turnover), "Compatibility Score: " + str(stock.compatibility_score), "Risk Score: " + str(stock.risk_score), "Allocation: " + str(stock.allocation))
        
        