import requests
import csv
import time
from bs4 import BeautifulSoup

def isOvervalued(bvps, price):
    if(price > bvps):
        return True
    return False

url = 'https://www.nasdaq.com/symbol/aapl'

page = requests.get(url)
page.content

soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()

price_box = soup.find('div', attrs={'class', 'qwidget-dollar'})
price_string = price_box.text
price = float(price_string.replace("$", ""))

urlshe = 'https://cloud.iexapis.com/v1/stock/AAPL/balance-sheet/1/shareholderEquity?token=pk_1b777be9dae247b8b83a82df68e086cd'
shareHolderEquity = float(requests.get(urlshe).text)
urlso = 'https://cloud.iexapis.com/v1/stock/AAPL/stats/sharesOutstanding?token=pk_1b777be9dae247b8b83a82df68e086cd'
outstandingShares = float(requests.get(urlso).text)

bookValuePerShare = shareHolderEquity/outstandingShares

if(isOvervalued(bookValuePerShare, price)):
    print("AAPL stock may be currently overvalued since its actual stock price is higher than its book value per share. Invest with "
          "caution")
else:
    print("AAPL stock may be currently undervalued since its actual stock price is lower than its book value per share. Consider "
          "investing in AAPL")