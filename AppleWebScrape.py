import requests
import csv
from bs4 import BeautifulSoup


url = 'https://www.nasdaq.com/symbol/aapl'

page = requests.get(url)
page.content

soup = BeautifulSoup(page.content, 'html.parser')
soup.prettify()

price_box = soup.find('div', attrs={'class', 'qwidget-dollar'})
price = price_box.text
print('Current Apple Stock Price: ' + price)



with open('index.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([price])
