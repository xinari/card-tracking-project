import requests, json, time

sets_url = 'https://api.tcgdex.net/v2/en/sets'
sets_response = requests.get(sets_url)

if sets_response.status_code == 200:
    sets_data = sets_response.json() 
    for set_info in sets_data:
        set_id = set_info["id"]
        url = f'https://api.tcgdex.net/v2/en/sets/{set_id}'
        response = requests.get(url) 
        if response.status_code == 200:
            data = response.json()
            card_list = data['cards']
            print(set_id, len(card_list))
            with open(f"data/{set_id}.json", "w", encoding="utf-8") as f:
                json.dump(card_list, f, indent=2, ensure_ascii=False)
        else:
            print(f"Request failed for {set_id}: status", response.status_code)
        time.sleep(0.5)
else:
    print("Request failed: status", sets_response.status_code)