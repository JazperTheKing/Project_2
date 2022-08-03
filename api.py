import requests, re
from pathlib import Path
import json

function = 'CURRENCY_EXCHANGE_RATE'
from_currency = 'USD'
to_currency = 'SGD'
api_key = 'TYRNR04ZRXIKTHMK'
base_url = 'https://www.alphavantage.co'
main_url = base_url+'/query?function='+function+'&from_currency='+from_currency+'&to_currency='+to_currency+'&apikey='+api_key
response = requests.get(main_url).json()

for item in response:
    rate = float(response[item]["5. Exchange Rate"])
    fcurrency = response[item]["1. From_Currency Code"]
    tcurrency = response[item]["3. To_Currency Code"]


file_path = Path.cwd()/"project_group"/"main.py"
with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
    file.write("[REAL TIME CURRENCY CONVERSION RATE]" " " f"{fcurrency}1 = {tcurrency}{rate}")
