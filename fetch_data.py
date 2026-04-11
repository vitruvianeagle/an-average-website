import json
import urllib.request
from datetime import datetime

# 1. Fetch real-time data from a free public API (CoinDesk for Bitcoin)
url = "https://api.coindesk.com/v1/bpi/currentprice.json"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
api_data = json.loads(response.read())
btc_price = api_data['bpi']['USD']['rate_float']

# 2. Compile our data points
averages = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "data": [
        {"category": "Finance", "name": "Average Bitcoin Price", "value": f"${btc_price:,.2f}"},
        {"category": "Environment", "name": "Global Sea Level Rise", "value": "3.4 mm/year (Static)"}
    ]
}

# 3. Save the data to a JSON file
with open('data.json', 'w') as f:
    json.dump(averages, f, indent=4)
