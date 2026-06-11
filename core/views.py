from django_distill import distill_path
from django.shortcuts import render
from .football import get_matches
from .data import SWEEPSTAKE

def index(request):
    matches = get_matches()
    return render(request, 'core/index.html', {
        'matches': matches,
        'sweepstake': SWEEPSTAKE,
    })