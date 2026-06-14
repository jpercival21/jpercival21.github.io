import requests
from dotenv import load_dotenv
from datetime import datetime
from zoneinfo import ZoneInfo
import os

load_dotenv()
BASE_URL = "https://api.football-data.org/v4"
FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY", "")
HEADERS = {"X-Auth-Token": FOOTBALL_API_KEY}

UK_TZ = ZoneInfo("Europe/London")


def get_matches():
    response = requests.get(
        f"{BASE_URL}/competitions/WC/matches",
        headers=HEADERS
    )
    response.raise_for_status()
    matches = response.json()["matches"]

    for match in matches:
        utc_dt = datetime.fromisoformat(match["utcDate"].replace("Z", "+00:00"))
        uk_dt = utc_dt.astimezone(UK_TZ)

        match["date"] = uk_dt.strftime("%Y-%m-%d")
        match["time"] = uk_dt.strftime("%H:%M")

        print(match["date"], match["time"], match["homeTeam"]["name"], "vs", match["awayTeam"]["name"])

    return matches