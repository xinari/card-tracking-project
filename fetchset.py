import requests, json

url = 'https://api.tcgdex.net/v2/en/sets/sv10.5b'
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    card_list = data['cards']
    for card in card_list:
        print(card["localId"], card["name"])
    with open("data/30th.json", "w", encoding="utf-8") as f:
        json.dump(card_list, f, indent=2, ensure_ascii=False)
else:
    print("Request failed: status", response.status_code)