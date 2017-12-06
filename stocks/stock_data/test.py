from stockData import financeData

x = financeData()
x.fetch_ticker_data(["BABA"],"2017-01-01","2017-12-04")
x.extract_panel_data()
print(x.extracted_data)
