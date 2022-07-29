import requests
import json

url = 'https://www.alphavantage.co'
response = requests.get(url)
print(response)
#print(response.headers.get('Content-Type'))
#data = json.load(response)
data = response.json()
print(data.keys())
#print(type(data))
#def currency_exchange_rate():
   # "from Symbol": "EUR",
    #"3. To Symbol": "USD",
