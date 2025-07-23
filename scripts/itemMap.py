import requests
import json


# Fetch item mapping (name → id, etc.)
def fetch_item_mapping():
    url = "https://prices.runescape.wiki/api/v1/osrs/mapping"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return []
    
