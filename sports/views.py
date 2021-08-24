from django.shortcuts import render
from .forms import MatchForm
from django.http import HttpResponseRedirect

def index(request):
    return render(request, 'sports/index.html')

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('match-created')
    else:
        form = MatchForm()

    return render(request, 'sports/create-match.html', {
        'form': form
    })

def all_matches(request):
    return render(request, 'sports/matches.html')

def match_created(request):
    return render(request, 'sports/submission.html')