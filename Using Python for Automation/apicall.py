import requests
import json
baseurl= 'https://api.upcitemdb.com/prod/trial/lookup'
parameters = {'upc': '012993441012'}
response = requests.get(baseurl, params = parameters)
print(response.url)
content = response.content

info = json.loads(content)
item = info['items']
itemsInfo = item[0]
title = itemsInfo['title']
brand = itemsInfo['brand']
print(title)
print(brand)
