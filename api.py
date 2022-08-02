import requests, re
import pathlib
import json

#wrting the function to insert it into the api parameters to excess the currency exchange rate
function = 'CURRENCY_EXCHANGE_RATE'
from_currency = 'USD'
to_currency = 'SGD'
#get the api_key to acess the api call
api_key = 'TYRNR04ZRXIKTHMK'
#get the base url
base_url = 'https://www.alphavantage.co'
#create the main url with the api parameters and keys
main_url = base_url+'/query?function='+function+'&from_currency='+from_currency+'&to_currency='+to_currency+'&apikey='+api_key
#request and get the api link and convert it to an json
response = requests.get(main_url).json()

print(response)
for value in response:
    function = float(response[value]["5. Exchange Rate"])
    fromcurrency = response[value]["1. From_Currency Code"]
    tocurrency = response[value]["3. To_Currency Code"]

file_path = Path.cwd()/"group_project"

