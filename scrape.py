import requests
import urllib.request
from bs4 import BeautifulSoup as bs
import pandas as pd
from datetime import date, datetime, timedelta
import csv
from csv import writer

urls = [ 'https://finance.yahoo.com/quote/MSFT',
        
        'https://finance.yahoo.com/quote/AAPL',
        'https://finance.yahoo.com/quote/GOOG',
          ]




df = []



for url in urls:
    prices = requests.get(url)
    soup = bs(prices.text, 'html.parser')
    #stock_name = soup.find(class_="D(ib) Fz(18px)").text
    close_price = soup.find(class_= 'Ta(end) Fw(600) Lh(14px)').text
    df.append(close_price)
    #df.append(f'{stock_name} - {close_price}')


df = pd.DataFrame(df)

df['Date']= datetime.today().strftime('%m/%d/%Y')


# Add the company name for each scraped price

company = ['Microsoft', 'Apple', 'Google']

df['Company'] = company

# Rename first column

df = df.rename(columns={df.columns[0]: 'Price($)'})



fc2 = df.iloc[:, 0].tolist()
#print('list of first column: ')
#print(fc2)


fc3 = df.iloc[:,1].tolist()
#print(fc3)

#print(df)


# No copied script, at all.

list = (fc3 + fc2)
list = (list[2:])

#df = list

#to convert list to new pandas dataframe
append_df = pd.DataFrame(list).T

append_df.columns =['Date', 'Microsoft', 'Apple', 'Google']

# As using close price, make sure date is accurate by subtracting 1

append_df['Date'] = pd.to_datetime(append_df['Date'])

append_df['Date'] = append_df['Date'] - pd.to_timedelta(1, unit='d')

# append this data to existing csv

append_df.to_csv('stock_prices.csv', mode='a', header=False, index=False)

