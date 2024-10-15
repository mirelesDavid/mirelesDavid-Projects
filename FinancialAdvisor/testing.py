import requests
import pandas as pd

api_key = '1VKWV4J8YLYTW55M'

symbols = [
    'AAPL', 'MSFT', 'NVDA', 'AVGO', 'AMZN', 'META', 'TSLA', 'COST', 
    'GOOGL', 'GOOG', 'NFLX', 'AMD', 'TMUS', 'PEP', 'ADBE', 'LIN',
    'CSCO'
]
count = 0
for symbol in symbols:
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey={api_key}&outputsize=full'
    response = requests.get(url)
    data = response.json()

    if 'Time Series (Daily)' in data:
        time_series = data['Time Series (Daily)']
        df = pd.DataFrame.from_dict(time_series, orient='index', dtype=float)
        df.index = pd.to_datetime(df.index)
        df = df.sort_index(ascending=False)

        df['close'] = df['4. close']
        average_52_weeks = df['close'].head(260).mean()
        current_price = df['close'].iloc[0]

        print(f"52-Week Average for {symbol}: {average_52_weeks:.2f}")
        print(f"Current Price for {symbol}: {current_price:.2f}")

        if current_price < (average_52_weeks * 0.8):
            print(f"The current price of {symbol} is below 20% of the 52-week average.")
        else:
            print(f"The current price of {symbol} is above 20% of the 52-week average.")
        
        print("")
    else:
        print(f"Data for {symbol} not found or an error occurred.")
        count += 1

    if count > 3:
        print(data)
        break