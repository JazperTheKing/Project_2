import requests
url = 'https://www.alphavantage.co/documentation'
r = requests.get(url)
data = r.json()
print(data)
