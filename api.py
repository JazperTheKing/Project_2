import requests
url = 'https://www.alphavantage.co/documentation'
r = requests.get(url)
print(r)
data = r.read()
print(data)
