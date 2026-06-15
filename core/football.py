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

    next_match = None

    for match in matches:
        utc_dt = datetime.fromisoformat(match["utcDate"].replace("Z", "+00:00"))
        uk_dt = utc_dt.astimezone(UK_TZ)

        match["date"] = uk_dt.strftime("%A, %d %B")
        match["time"] = uk_dt.strftime("%H:%M")
        if match["status"] == "IN_PLAY":
            next_match = match
        elif match["status"] != "FINISHED" and not next_match:
            next_match = match

        # print(match["date"], match["time"], match["homeTeam"]["name"], "vs", match["awayTeam"]["name"])

    return matches, next_match