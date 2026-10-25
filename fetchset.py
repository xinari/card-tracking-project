import requests

url = 'https://api.tcgdex.net/v2/en/sets/30th'
response = requests.get(url)
data = response.json()

card_list = data['cards']
for card in card_list:
    print(card["localId"], card["name"])
