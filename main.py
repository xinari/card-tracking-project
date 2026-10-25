import requests

url = 'https://api.tcgdex.net/v2/en/sets'
response = requests.get(url)
data = response.json()

print(response.status_code)

for setdata in data:
    print(setdata["id"], setdata["name"], setdata["cardCount"]["total"])