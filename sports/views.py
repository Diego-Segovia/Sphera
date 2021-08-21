from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'sports/index.html')

def create_match(request):
    return render(request, 'sports/create-match.html')

def all_matches(request):
    return render(request, 'sports/matches.html')