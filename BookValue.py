import requests
import csv

url1 = 'https://cloud.iexapis.com/v1/stock/AAPL/balance-sheet/1/shareholderEquity?token=pk_1b777be9dae247b8b83a82df68e086cd'
shareHolderEquity = float(requests.get(url1).text)
url2 = 'https://cloud.iexapis.com/v1/stock/AAPL/stats/sharesOutstanding?token=pk_1b777be9dae247b8b83a82df68e086cd'
outstandingShares = float(requests.get(url2).text)

bookValuePerShare = shareHolderEquity/outstandingShares

def isOvervalued(bv, price):
    if(price > bv):
        return True
    return False


print(bookValuePerShare)







