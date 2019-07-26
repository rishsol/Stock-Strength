import requests
from bs4 import BeautifulSoup
import seaborn

companyList = ["AAPL","GOOG", "MSFT"]
BVSP_and_SP_Difference =  [""]

for company in companyList:
    urlSHE = 'https://cloud.iexapis.com/v1/stock/' + company + '/balance-sheet/1/shareholderEquity?token=pk_1b777be9dae247b8b83a82df68e086cd'
    shareHolderEquity = float(requests.get(urlSHE).text)

    urlSO = 'https://cloud.iexapis.com/v1/stock/' + company + '/stats/sharesOutstanding?token=pk_1b777be9dae247b8b83a82df68e086cd'
    sharesOutstanding = float(requests.get(urlSO).text)

    companyBVPS = shareHolderEquity/sharesOutstanding

    urlSP =  'https://www.nasdaq.com/symbol/' + company
    page = requests.get(urlSP)
    page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.prettify()

    price_box = soup.find(attrs={'class', 'qwidget-dollar'})
    company_price = float(price_box.text.replace("$", ""))

    BVSP_and_SP_Difference = company_price - companyBVPS

plot = seaborn.barplot(company)



