import requests
import csv
import pandas as pd

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=F9HBARA0127RFBID&datatype=csv'

change = pd.Series([])
gain = []
loss = []
gain_average = []
loss_average = []
RSI = []

AAPL_Info = pd.read_csv('/Users/rishabsolanki09@gmail.com/Downloads/daily_AAPL (3).csv')
AAPL_Closing = AAPL_Info.loc[:, ['timestamp','close']].iloc[0:28]

change[len(AAPL_Closing) - 1] = 0

for i in range(0, len(AAPL_Closing) - 1):
    change[i] = AAPL_Closing['close'][i] - AAPL_Closing['close'][i + 1]

AAPL_Closing.insert(2, 'Change', change)


for value in AAPL_Closing['Change']:
    if(value > 0):
        gain.append(change)
        loss.append(0)
    else:
        loss.append(abs(change))
        gain.append(0)

gain_average[0] = sum(gain[0:14])/14
loss_average[0] = sum(loss[0:14])/14

for i in range(1, len(gain)):
    gain_average[i] = (gain_average[i-1]  * 13 + gain[i])/14
    loss_average[i] = (loss_average[i - 1] * 13 + loss[i]) / 14
    RSI[i] = gain_average[i]/loss_average[i]

print(RSI)


#print(AAPL_Closing.head())

#for num in range(len(change)):
 #   if change[i] > 0:


#AAPL_Closing['close'][0]- AAPL_Closing['close'][1])
#for closingPrice in AAPL_Closing:
 #  AAPL_Closing.insert(3, AAPL_Closing['close'][] )

#for closingPrice in AAPL_Closing:





#price in closingPrice:
# difference[0] = 0
#  difference[i] = float(price) - difference[i - 1]
# i += 1

#with open('closingPrices.csv', 'a') as csv_file:
 # writer = csv.writer(csv_file)
  #writer.writerow([latestClosingPrice])
  #writer.writecol([difference])


#with open('closingPrices.csv', 'a') as csv_file:
 #   writer = csv.writer(csv_file)
  #  writer.writecol([difference])


#rsiStepOne = 100 - (100/(1 + ()))

#with open('daily_AAPL.csv') as csvfile:
 #  csvReader = csv.reader(csvfile)
  # for row in page:
   #  print(row)