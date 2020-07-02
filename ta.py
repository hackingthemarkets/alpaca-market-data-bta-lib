import btalib
import pandas as pd

# Read a csv file into a pandas dataframe
df = pd.read_csv('data/ohlc/AAPL.txt', parse_dates=True, index_col='Date')

sma = btalib.sma(df, period=5)

#print(sma.df)

rsi = btalib.rsi(df)

df['sma'] = sma.df
df['rsi'] = rsi.df

print(df)

oversold_days = df[df['rsi'] < 30]

print(oversold_days)

overbought_days = df[df['rsi'] > 70]

print(overbought_days)

macd = btalib.macd(df)

print(macd.df)

df['macd'] = macd.df['macd']
df['signal'] = macd.df['signal']
df['histogram'] = macd.df['histogram']

print(df)