import sys
from yahoo_finance_api2 import share
from yahoo_finance_api2.exceptions import YahooFinanceError
import pandas as pd

key = ['MSFT', 'AAPL', 'NFLX', 'AMZN', 'GOOGL', 'BTC-USD']

for stock in key:
    my_share = share.Share(stock)
    symbol_data = None
    
    try:
        symbol_data = my_share.get_historical(share.PERIOD_TYPE_DAY,
                                            1825,
                                            share.FREQUENCY_TYPE_MINUTE,
                                            5)
    except YahooFinanceError as e:
        print(e.message)
        sys.exit(1)

    f = pd.DataFrame.from_dict(symbol_data)
    f.to_csv(f'{stock}.csv', index = False)
