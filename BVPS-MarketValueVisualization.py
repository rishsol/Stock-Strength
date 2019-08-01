import requests
from bs4 import BeautifulSoup
import seaborn
import numpy
import matplotlib.pyplot as plt

companyList = ["AAPL","GOOG", "MSFT", "RLGY", "PLD", "MAC", "KO", "PEP", "KDP"]
BVSP_and_SP_Difference = list(range(len(companyList)))

i = 0
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

    BVSP_and_SP_Difference[i]= company_price - companyBVPS
    i = i + 1

plt.bar(companyList, BVSP_and_SP_Difference)
plt.xlabel('Company')
plt.ylabel('Difference in BVPS and Share Price ($)')
plt.title('Difference in BVPS and Market Price of Companies in Various Sectors')
plt.show()


