import pandas as pd
import requests
import matplotlib.pyplot as plt
from pip._vendor.distlib.compat import raw_input
import wget

#content = requests.get(url)
change = pd.Series([])
gain = []
loss = []
gain_average = []
loss_average = []
RSI = pd.Series([])

try:
    company = raw_input('Enter the ticker symbol of a company:').strip().upper()

    url = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=' + company + '&apikey=F9HBARA0127RFBID&datatype=csv'
    path = wget.download(url)

except:
    print('Sorry we do not have data for ' + company.upper())
    exit()

Comp_Info = pd.read_csv('/Users/rishabsolanki09@gmail.com/Downloads/daily_AAPL (2).csv')
Comp_Closing = Comp_Info.loc[:, ['timestamp','close']].iloc[0:28]

change[len(Comp_Closing) - 1] = 0

for i in range(0, len(Comp_Closing) - 1):
    change[i] = Comp_Closing['close'][i] - Comp_Closing['close'][i + 1]

for value in change:
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

Comp_Closing.insert(2, 'RSI', RSI)
#print(Comp_Closing)

plt.plot(range(28), Comp_Closing['RSI'].iloc[::-1])
plt.title('RSI Values of ' + company + ' Stock over a 28 Day Period')
plt.ylabel('RSI')
plt.xlabel('Day')
plt.show()