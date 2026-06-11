from django_distill import distill_path
from django.shortcuts import render
from .football import get_matches
from .data import SWEEPSTAKE, FLAG_IMG
from collections import defaultdict

def index(request):
    matches = get_matches()

    people = defaultdict(list)
    for team, person in SWEEPSTAKE.items():
        people[person].append({
            "name": team,
            "flag": FLAG_IMG.get(team, ""),
        })

    for match in matches:
        home = match["homeTeam"]["name"]
        away = match["awayTeam"]["name"]
        match["homeTeam"]["flag"] = FLAG_IMG.get(home, "")
        match["homeTeam"]["person"] = SWEEPSTAKE.get(home, "")
        match["awayTeam"]["flag"] = FLAG_IMG.get(away, "")
        match["awayTeam"]["person"] = SWEEPSTAKE.get(away, "")

    return render(request, 'core/index.html', {
        'matches': matches,
        'people': dict(people),
    })