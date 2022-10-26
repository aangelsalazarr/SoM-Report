import yfinance as yf
import pandas as pd


def data_processor(list, period):
    df = pd.DataFrame(columns=['Ticker'])

    for item in list:

        # process of grabbing data from yfinance api
        a = yf.Ticker(str(item)).history(period=period)
        a = a.assign(Delta=a['Close'].pct_change())
        a = a.assign(volumeDelta=a['Volume'].pct_change())
        df = pd.concat([df, pd.DataFrame(a)])

        # here we are adding ticker symbol to Ticker col
        if df['Ticker'].isnull:
            df['Ticker'].fillna(item, inplace=True)
        else:
            continue

    # now we want to clean up our data a bit
    df.drop(['Dividends', 'Stock Splits'], inplace=True, axis=1)
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'Date'}, inplace=True)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close'] = df['Close'].astype(float)
    df['high_low_delta'] = (df['High'] - df['Low']) / df['Low']
    df['end_day_delta'] = (df['Close'] - df['Open']) / df['Open']

    return df
