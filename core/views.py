from django_distill import distill_path
from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')