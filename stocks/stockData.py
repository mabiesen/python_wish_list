from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd

class financeData:

    #pre-defined
    data_source = 'google'
    #these are the set user inputs
    start_date = ''
    end_date = ''
    tickers = []
    #this is raw return
    panel_data = ''
    #this is specified the data by weekday, extracted using the 'extract_panel_data' function
    extracted_data = ''

    def __init__(self):
        print("Finance data class initialized.")

    def fetch_and_extract(self,tickers,start_date,end_date,datatype):
        fetch_ticker_data(tickers,start_date,end_date)
        extract_panel_data(datatype)

    def fetch_ticker_data(self, tickers, start_date, end_date):
        self.tickers = tickers
        self.start_date = start_date
        self.end_date = end_date
        # User pandas_reader.data.DataReader to load the desired data. As simple as that.
        self.panel_data = data.DataReader(self.tickers, self.data_source, self.start_date, self.end_date)
        #Clear extracted data to avoid confusion
        self.extracted_data = ''

    def extract_panel_data(self,datatype):
        # 'Close' for getting closing prices. This will return a Pandas DataFrame
        # The index in this DataFrame is the major index of the panel_data.
        thisdata = self.panel_data.ix[datatype]
        all_weekdays = pd.date_range(start=self.start_date, end=self.end_date, freq='B')
        self.extracted_data = thisdata.reindex(all_weekdays)

    def plot_each_ticker(self):
        for t in self.tickers:
            make_plot(t)

    def make_plot(self,whichticker):
        # Get the MSFT time series. This now returns a Pandas Series object indexed by date.
        tickerdata = self.extracted_data.ix[:, whichticker]
        # Calculate the 20 and 100 days moving averages of the closing prices
        short_rolling = tickerdata.rolling(window=20).mean()
        long_rolling = tickerdata.rolling(window=100).mean()
        # Plot everything by leveraging the very powerful matplotlib package
        fig = plt.figure()
        ax = fig.add_subplot(1,1,1)
        ax.plot(tickerdata.index, tickerdata, label=whichticker)
        ax.plot(short_rolling.index, short_rolling, label='20 days rolling')
        ax.plot(long_rolling.index, long_rolling, label='100 days rolling')
        ax.set_xlabel('Date')
        ax.set_ylabel('Closing price ($)')
        ax.legend()
        plt.show()

    def print_data_tail(self,timeframe):
        print(self.extracted_data.tail(timeframe))






# # Define the instruments to download. We would like to see Apple, Microsoft and the S&P500 index.
# tickers = ['BABA', 'BBY']
#
# # Define which online source one should use
# data_source = 'google'
#
# # We would like all available data from 01/01/2010 until 11/20/2017.
# start_date = '2010-01-01'
# end_date = '2017-11-20'
#
# # User pandas_reader.data.DataReader to load the desired data. As simple as that.
# panel_data = data.DataReader(tickers, data_source, start_date, end_date)
#
# # Getting just the adjusted closing prices. This will return a Pandas DataFrame
# # The index in this DataFrame is the major index of the panel_data.
# close = panel_data.ix['Close']
#
# # Getting all weekdays between 01/01/2000 and 12/31/2016
# all_weekdays = pd.date_range(start=start_date, end=end_date, freq='B')
#
# # How do we align the existing prices in adj_close with our new set of dates?
# # All we need to do is reindex close using all_weekdays as the new index
# close = close.reindex(all_weekdays)
#
# print(close.tail(10))
