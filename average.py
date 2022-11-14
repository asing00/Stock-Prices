
import pandas as pd
from datetime import date, datetime, timedelta
import numpy as np
import matplotlib.pyplot as plt


df = pd.read_csv("stock_prices.csv")

# Extra column where average is calculated
df.columns = [*df.columns[:-1], 'Average']

# clean the date column
df['Date'] = pd.to_datetime(df['Date'])

df = df.drop(df.columns[4], axis=1)

# Simple Moving Average
df['microsoft'] = df['Microsoft'].rolling(30).mean()
df['apple'] = df['Apple'].rolling(30).mean()
df['google'] = df['Google'].rolling(30).mean()

sma_df = df[['Date', 'microsoft', 'apple', 'google']].copy()


# Cumulative Moving Average
df['microsoft_cma'] = df['Microsoft'].expanding().mean()
df['apple_cma'] = df['Apple'].expanding().mean()
df['google_cma'] = df['Google'].expanding().mean()

cma_df = df[['Date', 'microsoft_cma', 'apple_cma', 'google_cma']].copy()


#print(cma_df)


# This includes NaN values 
#df.plot(x="Date", y=["microsoft", "apple", "google"], kind="bar")
#plt.show()

sma_df = sma_df.dropna()

#sma_df.plot(x="Date", y=["microsoft", "apple", "google"], kind='bar', rot=0)
#plt.show()

sma_df.plot(x="Date", y=["microsoft", "apple", "google"])
plt.show()