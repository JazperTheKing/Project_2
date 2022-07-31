import requests, re
import datetime
import json

function = 'FX_WEEKLY'
from_symbol = 'USD'
to_symbol = 'SGD'
api_key = 'TYRNR04ZRXIKTHMK'
base_url = 'https://www.alphavantage.co'
main_url = base_url+'/query?function='+function+'&from_symbol='+from_symbol+'&to_symbol='+to_symbol+'&apikey='+api_key
response = requests.get(main_url).json()
d = response["Time Series FX (Weekly)"]
recentdate = max((x for x in d.keys()))
print(recentdate)
number1 = float(d[recentdate]["2. high"])
number2 = float(d[recentdate]["3. low"])
mean = (number1+number2)/2
print(mean)
