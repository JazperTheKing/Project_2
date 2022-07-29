from xmlrpc.client import _datetime_type
import requests, re
import datetime

function = 'FX_WEEKLY'
from_symbol = 'USD'
to_symbol = 'SGD'
api_key = 'TYRNR04ZRXIKTHMK'
base_url = 'https://www.alphavantage.co'
main_url = base_url+'/query?function='+function+'&from_symbol='+from_symbol+'&to_symbol='+to_symbol+'&apikey='+api_key
#pageToken = 
response = requests.get(main_url).json()
empty_list = []
for item in response:
    empty_list.append(str(response))
    print(empty_list)

    for index, content in enumerate(empty_list):
        week = re.findall(pattern='\d\d\d\d[-]\d\d[-]\d\d', string=content)
        print(week)
        number1 = re.search(pattern="['2. high': +['\d.\d\d\d\d\d']+]", string=content)
        #number1 = number1.append()
        print(number1)

        #number2 = re.search

       # mean = ((number1+number2)/2)


#print(response['Time Series FX (Weekly)'])
#NOT COMPLETE
