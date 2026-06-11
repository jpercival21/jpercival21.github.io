import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.football-data.org/v4"
FOOTBALL_API_KEY = os.environ.get("FOOTBALL_API_KEY", "")
HEADERS = {"X-Auth-Token": FOOTBALL_API_KEY}

def get_matches():
    response = requests.get(
        f"{BASE_URL}/competitions/WC/matches",
        headers=HEADERS
    )
    print(response)
    response.raise_for_status()
    return response.json()["matches"]