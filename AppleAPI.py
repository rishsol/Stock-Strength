import requests
import csv


url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=F9HBARA0127RFBID&datatype=csv'
file = requests.get(url)
reader = csv.reader(file)
header = next(reader)
data = [row for row in reader]

latestClosingPrice = data[0][4]


with open('latestClosingPrices.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([latestClosingPrice])



#with open('closingPrices.csv', 'a') as csv_file:
 #   writer = csv.writer(csv_file)
  #  writer.writecol([difference])