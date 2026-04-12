import json
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone

# --- CONFIGURATION ---
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}

def fetch_json(url):
    """Fetch and parse JSON from URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    response = urllib.request.urlopen(req, timeout=10)
    return json.loads(response.read())

def fetch_xml(url):
    """Fetch and parse XML from URL."""
    req = urllib.request.Request(url, headers=HEADERS)
    response = urllib.request.urlopen(req, timeout=10)
    return ET.fromstring(response.read())

# --- 1. LIVE TICKER DATA: Verified #1 Rankings ---
trending_data = []

# iTunes #1 Song (US)
try:
    data = fetch_json("https://itunes.apple.com/us/rss/topsongs/limit=1/json")
    entry = data['feed']['entry'][0]
    song = entry['im:name']['label']
    artist = entry['im:artist']['label']
    trending_data.append({
        "label": "iTunes #1 Song",
        "value": f"{song} — {artist}",
        "url": entry['link'][0]['attributes']['href']
    })
except Exception as e:
    print(f"iTunes Songs error: {e}")

# iTunes #1 Podcast (US)
try:
    data = fetch_json("https://itunes.apple.com/us/rss/toppodcasts/limit=1/json")
    entry = data['feed']['entry'][0]
    podcast = entry['im:name']['label']
    trending_data.append({
        "label": "iTunes #1 Podcast",
        "value": podcast,
        "url": entry['link'][0]['attributes']['href']
    })
except Exception as e:
    print(f"iTunes Podcasts error: {e}")

# iTunes #1 Free App (US)
try:
    data = fetch_json("https://itunes.apple.com/us/rss/topfreeapplications/limit=1/json")
    entry = data['feed']['entry'][0]
    app = entry['im:name']['label']
    trending_data.append({
        "label": "iTunes #1 Free App",
        "value": app,
        "url": entry['link'][0]['attributes']['href']
    })
except Exception as e:
    print(f"iTunes Apps error: {e}")

# iTunes #1 Album (US)
try:
    data = fetch_json("https://itunes.apple.com/us/rss/topalbums/limit=1/json")
    entry = data['feed']['entry'][0]
    album = entry['im:name']['label']
    artist = entry['im:artist']['label']
    trending_data.append({
        "label": "iTunes #1 Album",
        "value": f"{album} — {artist}",
        "url": entry['link'][0]['attributes']['href']
    })
except Exception as e:
    print(f"iTunes Albums error: {e}")

# --- 2. LIVE MARKET DATA ---
btc_price = "API Offline"
btc_url = "https://blockchain.info/ticker"
try:
    data = fetch_json(btc_url)
    btc_price = f"${data['USD']['last']:,.2f}"
except Exception as e:
    print(f"Bitcoin error: {e}")

# --- 3. BUILD COMPREHENSIVE DATABASE ---
website_data = {
    "last_updated": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC"),
    "trending": trending_data,
    "categories": [
        {
            "title": "Wages & Income",
            "meta": "US averages, most recent annual data",
            "sources": "Bureau of Labor Statistics · Census Bureau · Federal Reserve",
            "items": [
                {
                    "name": "Median Household Income",
                    "value": "$80,610",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/library/publications/2024/demo/p60-282.html"
                },
                {
                    "name": "Average Hourly Earnings",
                    "value": "$35.36",
                    "source": "BLS",
                    "url": "https://www.bls.gov/news.release/empsit.t19.htm"
                },
                {
                    "name": "Average Weekly Earnings",
                    "value": "$1,207",
                    "source": "BLS",
                    "url": "https://www.bls.gov/news.release/empsit.t19.htm"
                },
                {
                    "name": "CEO-to-Worker Pay Ratio",
                    "value": "344:1",
                    "source": "EPI",
                    "url": "https://www.epi.org/publication/ceo-pay-in-2023/"
                },
                {
                    "name": "Median Household Net Worth",
                    "value": "$192,900",
                    "source": "Federal Reserve",
                    "url": "https://www.federalreserve.gov/publications/files/scf23.pdf"
                }
            ]
        },
        {
            "title": "Housing",
            "meta": "US averages, current period",
            "sources": "NAR · Freddie Mac · Census Bureau",
            "items": [
                {
                    "name": "Median Home Sale Price",
                    "value": "$407,500",
                    "source": "NAR",
                    "url": "https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales"
                },
                {
                    "name": "30-Year Mortgage Rate",
                    "value": "6.76%",
                    "source": "Freddie Mac",
                    "url": "https://www.freddiemac.com/pmms"
                },
                {
                    "name": "Median Monthly Rent",
                    "value": "$1,540",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/housing/hvs/index.html"
                },
                {
                    "name": "Average Home Size",
                    "value": "2,233 sq ft",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/construction/chars/"
                },
                {
                    "name": "Homeownership Rate",
                    "value": "65.6%",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/housing/hvs/index.html"
                }
            ]
        },
        {
            "title": "Finance & Markets",
            "meta": "Current and historical averages",
            "sources": "Federal Reserve · S&P Global · Blockchain.info",
            "items": [
                {
                    "name": "S&P 500 Avg Annual Return",
                    "value": "10.5%",
                    "source": "S&P Global",
                    "url": "https://www.spglobal.com/spdji/en/indices/equity/sp-500/"
                },
                {
                    "name": "Bitcoin Price",
                    "value": btc_price,
                    "source": "Blockchain.info",
                    "url": btc_url
                },
                {
                    "name": "Average Credit Card APR",
                    "value": "21.76%",
                    "source": "Federal Reserve",
                    "url": "https://www.federalreserve.gov/releases/g19/current/"
                },
                {
                    "name": "Personal Savings Rate",
                    "value": "4.6%",
                    "source": "BEA",
                    "url": "https://www.bea.gov/data/income-saving/personal-saving-rate"
                },
                {
                    "name": "Average 401(k) Balance",
                    "value": "$125,900",
                    "source": "Fidelity",
                    "url": "https://www.fidelity.com/learning-center/smart-money/average-401k-balance"
                }
            ]
        },
        {
            "title": "Health & Wellness",
            "meta": "US averages, most recent data",
            "sources": "CDC · CMS · KFF",
            "items": [
                {
                    "name": "Life Expectancy",
                    "value": "77.5 years",
                    "source": "CDC",
                    "url": "https://www.cdc.gov/nchs/fastats/life-expectancy.htm"
                },
                {
                    "name": "Average Health Insurance Premium",
                    "value": "$8,435/yr",
                    "source": "KFF",
                    "url": "https://www.kff.org/health-costs/report/employer-health-benefits-survey/"
                },
                {
                    "name": "Obesity Rate (Adult)",
                    "value": "41.9%",
                    "source": "CDC",
                    "url": "https://www.cdc.gov/obesity/data/adult.html"
                },
                {
                    "name": "Average Sleep Duration",
                    "value": "6.8 hours",
                    "source": "CDC",
                    "url": "https://www.cdc.gov/sleep/data-and-statistics/adults.html"
                },
                {
                    "name": "Uninsured Rate",
                    "value": "7.9%",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/library/publications/2024/demo/p60-284.html"
                }
            ]
        },
        {
            "title": "Education",
            "meta": "US averages, current academic year",
            "sources": "NCES · College Board · Federal Reserve",
            "items": [
                {
                    "name": "Average Public College Tuition",
                    "value": "$11,260/yr",
                    "source": "College Board",
                    "url": "https://research.collegeboard.org/trends/college-pricing"
                },
                {
                    "name": "Average Private College Tuition",
                    "value": "$43,350/yr",
                    "source": "College Board",
                    "url": "https://research.collegeboard.org/trends/college-pricing"
                },
                {
                    "name": "Average Student Loan Debt",
                    "value": "$37,850",
                    "source": "Federal Reserve",
                    "url": "https://www.federalreserve.gov/publications/2024-economic-well-being-of-us-households-in-2023-student-loans.htm"
                },
                {
                    "name": "High School Graduation Rate",
                    "value": "87%",
                    "source": "NCES",
                    "url": "https://nces.ed.gov/programs/coe/indicator/coi"
                },
                {
                    "name": "Bachelor's Degree Holders",
                    "value": "33.7%",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/data/tables/2023/demo/educational-attainment/cps-detailed-tables.html"
                }
            ]
        },
        {
            "title": "Transportation",
            "meta": "US averages, current data",
            "sources": "AAA · Census Bureau · DOT",
            "items": [
                {
                    "name": "Average Commute Time",
                    "value": "26.8 min",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/topics/employment/commuting.html"
                },
                {
                    "name": "Average Gas Price",
                    "value": "$3.22/gal",
                    "source": "AAA",
                    "url": "https://gasprices.aaa.com/"
                },
                {
                    "name": "Average New Car Price",
                    "value": "$48,644",
                    "source": "Kelley Blue Book",
                    "url": "https://www.coxautoinc.com/market-insights/"
                },
                {
                    "name": "Average Miles Driven/Year",
                    "value": "14,263",
                    "source": "DOT",
                    "url": "https://www.fhwa.dot.gov/policyinformation/statistics.cfm"
                },
                {
                    "name": "Remote Work Rate",
                    "value": "28.2%",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/newsroom/press-releases/2024/working-from-home.html"
                }
            ]
        },
        {
            "title": "Demographics",
            "meta": "US population statistics",
            "sources": "Census Bureau",
            "items": [
                {
                    "name": "US Population",
                    "value": "336.0M",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/popclock/"
                },
                {
                    "name": "Median Age",
                    "value": "38.9 years",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/quickfacts/"
                },
                {
                    "name": "Average Household Size",
                    "value": "2.51",
                    "source": "Census Bureau",
                    "url": "https://www.census.gov/data/tables/time-series/demo/families/households.html"
                },
                {
                    "name": "Marriage Rate",
                    "value": "6.0 per 1k",
                    "source": "CDC",
                    "url": "https://www.cdc.gov/nchs/nvss/marriage-divorce.htm"
                },
                {
                    "name": "Birth Rate",
                    "value": "10.9 per 1k",
                    "source": "CDC",
                    "url": "https://www.cdc.gov/nchs/fastats/births.htm"
                }
            ]
        },
        {
            "title": "Environment",
            "meta": "US and global metrics",
            "sources": "EPA · NOAA · EIA",
            "items": [
                {
                    "name": "US CO₂ Emissions Per Capita",
                    "value": "13.0 tons/yr",
                    "source": "EPA",
                    "url": "https://www.epa.gov/ghgemissions/inventory-us-greenhouse-gas-emissions-and-sinks"
                },
                {
                    "name": "Global Avg Temperature Anomaly",
                    "value": "+1.18°C",
                    "source": "NOAA",
                    "url": "https://www.climate.gov/news-features/understanding-climate/climate-change-global-temperature"
                },
                {
                    "name": "Renewable Energy Share",
                    "value": "21.4%",
                    "source": "EIA",
                    "url": "https://www.eia.gov/energyexplained/renewable-sources/"
                },
                {
                    "name": "Average Daily Water Use",
                    "value": "82 gal",
                    "source": "EPA",
                    "url": "https://www.epa.gov/watersense/how-we-use-water"
                }
            ]
        }
    ]
}

# --- 4. SAVE TO JSON ---
with open('data.json', 'w') as f:
    json.dump(website_data, f, indent=2)

print(f"Data updated: {website_data['last_updated']}")
print(f"Trending items: {len(trending_data)}")
print(f"Categories: {len(website_data['categories'])}")
total_items = sum(len(cat['items']) for cat in website_data['categories'])
print(f"Total data points: {total_items}")
