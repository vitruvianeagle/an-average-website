import json
import urllib.request
from datetime import datetime

# 1. Fetch live data (Bitcoin as an example of dynamic data)
try:
    url = "https://blockchain.info/ticker"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    response = urllib.request.urlopen(req)
    api_data = json.loads(response.read())
    btc_price = f"${api_data['USD']['last']:,.2f}"
except:
    btc_price = "API Offline"

# 2. Build the massive data dictionary
website_data = {
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "trending": [
        {"label": "Box Office", "value": "Dune: Part Two"},
        {"label": "Billboard Hot 100", "value": "Texas Hold 'Em"},
        {"label": "Netflix TV", "value": "3 Body Problem"},
        {"label": "NYT Fiction", "value": "The Women"},
        {"label": "Spotify Global", "value": "Beautiful Things"}
    ],
    "categories": [
        {
            "title": "Wages & Income",
            "meta": "US averages, most recent period",
            "sources": "BLS · Federal Reserve · Census Bureau",
            "items": [
                {"name": "Median Household Income", "value": "$80,610", "source": "Census Bureau"},
                {"name": "Avg Hourly Earnings", "value": "$34.28", "source": "BLS"},
                {"name": "Avg Weekly Earnings", "value": "$1,170", "source": "BLS"},
                {"name": "Avg CEO-to-Worker Pay Ratio", "value": "344:1", "source": "EPI"},
                {"name": "Avg Household Net Worth", "value": "$1.06M", "source": "Federal Reserve"}
            ]
        },
        {
            "title": "Housing",
            "meta": "US averages",
            "sources": "NAR · Census · Freddie Mac · Harvard JCHS",
            "items": [
                {"name": "Median Home Sale Price", "value": "$384,500", "source": "NAR"},
                {"name": "Avg 30-Yr Mortgage Rate", "value": "6.8%", "source": "Freddie Mac"},
                {"name": "Avg Monthly Rent (1BR)", "value": "$1,510", "source": "Census / Zillow"},
                {"name": "Avg Home Size (sq ft)", "value": "2,299", "source": "Census Bureau"},
                {"name": "Avg Years to Save Down Payment", "value": "11.5", "source": "Harvard JCHS"}
            ]
        },
        {
            "title": "Health & Medicine",
            "meta": "US & global averages",
            "sources": "CDC · WHO · Kaiser Family Foundation",
            "items": [
                {"name": "US Life Expectancy", "value": "77.5 yrs", "source": "CDC / NCHS"},
                {"name": "Avg Annual Healthcare Cost", "value": "$13,493", "source": "CMS"},
                {"name": "Avg Employer Health Premium", "value": "$23,968", "source": "KFF"},
                {"name": "Avg Nightly Sleep (US Adults)", "value": "6.8 hrs", "source": "CDC / Gallup"},
                {"name": "Avg BMI (US Adults)", "value": "29.6", "source": "CDC / NHANES"}
            ]
        },
        {
            "title": "Education",
            "meta": "US averages",
            "sources": "NCES · College Board · Fed Reserve",
            "items": [
                {"name": "Avg Student Loan Debt", "value": "$37,574", "source": "Federal Reserve"},
                {"name": "Avg Public College Tuition", "value": "$11,260", "source": "College Board"},
                {"name": "Avg Private College Tuition", "value": "$41,540", "source": "College Board"},
                {"name": "Avg K-12 Per-Pupil Spending", "value": "$14,347", "source": "NCES"}
            ]
        },
        {
            "title": "Finance & Markets",
            "meta": "Historical and current averages",
            "sources": "Federal Reserve · S&P Global · BLS",
            "items": [
                {"name": "S&P 500 Historical Avg Return", "value": "10.5%", "source": "S&P Global"},
                {"name": "Current Bitcoin Price", "value": btc_price, "source": "Blockchain.info"},
                {"name": "Avg US Credit Card APR", "value": "21.6%", "source": "Federal Reserve"},
                {"name": "Avg US Credit Card Debt", "value": "$6,501", "source": "Federal Reserve"},
                {"name": "US Avg Personal Savings Rate", "value": "3.8%", "source": "BEA"}
            ]
        }
    ]
}

# 3. Save it to data.json
with open('data.json', 'w') as f:
    json.dump(website_data, f, indent=4)
