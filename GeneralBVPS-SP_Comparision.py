import requests
from bs4 import BeautifulSoup
from pip._vendor.distlib.compat import raw_input


def isOvervalued(bvps, price):
    if(price > bvps):
        return True
    return False

company = raw_input('Enter the ticker symbol of a company:').strip()
url = 'https://www.nasdaq.com/symbol/' + company

page = requests.get(url)
page.content

soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()

price_box = soup.find(attrs={'class', 'qwidget-dollar'})
price_string = price_box.text
price = float(price_string.replace("$", ""))

urlshe = 'https://cloud.iexapis.com/v1/stock/' + company + '/balance-sheet/1/shareholderEquity?token=pk_1b777be9dae247b8b83a82df68e086cd'
shareHolderEquity = float(requests.get(urlshe).text)
urlso = 'https://cloud.iexapis.com/v1/stock/' + company + '/stats/sharesOutstanding?token=pk_1b777be9dae247b8b83a82df68e086cd'
outstandingShares = float(requests.get(urlso).text)

bookValuePerShare = shareHolderEquity/outstandingShares

try:
    if(isOvervalued(bookValuePerShare, price)):
        print(company.upper() + ' stock may be overvalued since its actual stock price is higher than its book value per share. Invest with '
          'caution')
    else:
        print(company.upper() + ' stock may be undervalued since its actual stock price is lower than its book value per share. Consider '
      'investing in' + company.upper())
except:
    print('Sorry, we do not have data for ' + company.upper())