import requests

url = 'https://api.tcgdex.net/v2/en/sets'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    for setdata in data:
        print(setdata["id"], setdata["name"], setdata["cardCount"]["total"])
else:
    print("Request failed: status", response.status_code)