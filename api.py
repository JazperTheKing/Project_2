import requests, re
from pathlib import Path
import json

function = 'FX_WEEKLY'
from_currency = 'USD'
to_currency = 'SGD'
api_key = 'TYRNR04ZRXIKTHMK'
base_url = 'https://www.alphavantage.co'
main_url = base_url+'/query?function='+function+'&from_symbol='+from_currency+'&to_symbol='+to_currency+'&apikey='+api_key
response = requests.get(main_url).json()
d = response["Time Series FX (Weekly)"]
recentdate = max((x for x in d.keys()))
print(recentdate)
number1 = float(d[recentdate]["2. high"])
number2 = float(d[recentdate]["3. low"])
mean = (number1+number2)/2
print(mean)

file_path = Path.cwd()/"project_group"/"main.py"
with file_path.open(mode="w", encoding="UTF-8", newline="") as file:
    file.write("[MEAN WEEKLY CLOSING FOREX PRICE]" " " f"{from_currency} = {to_currency}{mean}")
