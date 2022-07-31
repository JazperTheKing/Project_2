import requests, re
import datetime
import json

#wrting the function, from_symbol, and to_symbol to insert it into the api parameters to excess the forex (FX)
function = 'FX_WEEKLY'
from_symbol = 'USD'
to_symbol = 'SGD'
#get the api_key to acess the api call
api_key = 'TYRNR04ZRXIKTHMK'
#get the base url
base_url = 'https://www.alphavantage.co'
#create the main url with the api parameters and keys
main_url = base_url+'/query?function='+function+'&from_symbol='+from_symbol+'&to_symbol='+to_symbol+'&apikey='+api_key
#request and get the api link and convert it to an json
response = requests.get(main_url).json()
#select the data from time seriec fx (weekly) to narrow down what we need
d = response["Time Series FX (Weekly)"]
#find the most recent week using max() by using the dates as keys
recentdate = max((x for x in d.keys()))

print(recentdate)

#find the highest number in the week and convert it to a float 
number1 = float(d[recentdate]["2. high"])
#find the lowest number in the week and convert it to a float 
number2 = float(d[recentdate]["3. low"])
#calcualting the mean by combinding the 2 numbers and dividing it
mean = (number1+number2)/2
print(mean)
