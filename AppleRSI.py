import pandas as pd
import matplotlib

url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=AAPL&apikey=F9HBARA0127RFBID&datatype=csv'

change = pd.Series([])
gain = []
loss = []
gain_average = []
loss_average = []
RSI = pd.Series([])

AAPL_Info = pd.read_csv('/Users/rishabsolanki09@gmail.com/Downloads/daily_AAPL (3).csv')
AAPL_Closing = AAPL_Info.loc[:, ['timestamp','close']].iloc[0:28]

change[len(AAPL_Closing) - 1] = 0

for i in range(0, len(AAPL_Closing) - 1):
    change[i] = AAPL_Closing['close'][i] - AAPL_Closing['close'][i + 1]

AAPL_Closing.insert(2, 'Change', change)


for value in AAPL_Closing['Change']:
    if(value > 0):
        gain.append(value)
        loss.append(0)
    else:
        loss.append(abs(value))
        gain.append(0)


gain_average.append(sum(gain[0:14])/14)
loss_average.append(sum(loss[0:14])/14)
RSI[0] = 100 - (100/(1 + gain_average[0]/loss_average[0]))

for i in range(1, len(gain)):
    gain_average.append((gain_average[i-1]  * 13 + gain[i]) / 14)
    loss_average.append((loss_average[i - 1] * 13 + loss[i]) / 14)
    RSI[i] = 100 - (100/(1 + gain_average[i]/loss_average[i]))

print(RSI)