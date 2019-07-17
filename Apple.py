import urllib2
import csv
import numpy

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=F9HBARA0127RFBID&datatype=csv'
file = urllib2.urlopen(url)
reader = csv.reader(file)
header = next(reader)
data = [row for row in reader]

dataArray = numpy.array(data)
allClosingPrice = dataArray[:,4]
closingPrice = allClosingPrice[:,5]
latestClosingPrice = data[0][4]
difference = ['']

i = 1
for price in closingPrice:
    difference[0] = 0
    difference[i] = float(price) - difference[i - 1]
    i += 1

with open('closingPrices.csv', 'a') as csv_file:
  writer = csv.writer(csv_file)
  writer.writerow([latestClosingPrice])
  writer.writecol([difference])



#with open('closingPrices.csv', 'a') as csv_file:
 #   writer = csv.writer(csv_file)
  #  writer.writecol([difference])


#rsiStepOne = 100 - (100/(1 + ()))

#with open('daily_AAPL.csv') as csvfile:
 #  csvReader = csv.reader(csvfile)
  # for row in page:
   # print(row)

