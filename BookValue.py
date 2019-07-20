'''
import requests
import urllib
import urllib.request
from bs4 import BeautifulSoup

url = "https://www.nasdaq.com/symbol/aapl/financials?query=balance-sheet"
#urlOpen = urllib.urlopen(url).read()

def make_soup(url):
    page = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(page, "html.parser")
    return soupdata

soup = make_soup(url)

for finance in soup.findAll("tr"):
    print(finance.text)
'''

import requests
import csv
import time
from bs4 import BeautifulSoup


url = 'https://www.nasdaq.com/symbol/aapl'

page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()

equity_box = soup.find('div', attrs={'class', 'genTable'})
equity = equity_box.text

print(equity)
#tb = soup.find('div', class_= 'genTable')


#for link in tb.find_all('tr'):
 #  name = link.find('td')
  #  print(name.get)

#for finance in soup.find_all('tr'):
 #   for data in finance.find_all('td'):
  #      print(data.text)
