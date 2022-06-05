import requests

base_url = "https://api.binance.com"
path = "/api/v3/exchangeInfo"
r = requests.get(base_url)

r
