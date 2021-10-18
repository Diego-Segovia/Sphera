from django.forms.widgets import DateInput
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MatchForm
from .models import Match

def index(request):
    return render(request, 'sports/index.html')

def create_match(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            created_match = Match(
                title = form.cleaned_data['event_name'],
                location = form.cleaned_data['event_location'],
                date = form.cleaned_data['event_date'],
                time = form.cleaned_data['event_time'],
                details = form.cleaned_data['event_details']
            )
            created_match.save()
            return HttpResponseRedirect('match-created')
    else:
        form = MatchForm()

    return render(request, 'sports/create-match.html', {
        'form': form
    })

def all_matches(request):
    matches = Match.objects.all()
    return render(request, 'sports/all-matches.html',{
        'matches': matches
    })

def match_created(request):
    return render(request, 'sports/submission.html')

def match_detail(request, id):
    match = Match.objects.get(pk=id)
    return render(request, 'sports/match-detail.html',{
        'match': match
    })