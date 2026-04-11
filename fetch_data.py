import json
import urllib.request
from datetime import datetime

# 1. Fetch real-time data from a more stable API, with a safety net
try:
    url = "https://blockchain.info/ticker"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    api_data = json.loads(response.read())
    btc_price = api_data['USD']['last']
    btc_display = f"${btc_price:,.2f}"
except Exception as e:
    # If the API is down or GitHub loses internet, don't crash. Just do this:
    btc_display = "API Offline temporarily"

# 2. Compile our data points
averages = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "data": [
        {"category": "Finance", "name": "Average Bitcoin Price", "value": btc_display},
        {"category": "Environment", "name": "Global Sea Level Rise", "value": "3.4 mm/year (Static)"}
    ]
}

# 3. Save the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(averages, f, indent=4)
