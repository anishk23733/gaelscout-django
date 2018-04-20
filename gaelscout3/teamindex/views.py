from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from teamindex.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.contrib.auth.models import User

import arrow

# Create your views here.
def home(request):
    return render(request, 'index.html')

def teamindex(request):
    teams = Teams.objects.all()
    paginator = Paginator(teams, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    teams = paginator.get_page(page)
    return render(request, 'teamindex.html', {'teams': teams})

def dashboard(request, team_number):

    team = Teams.objects.get(name=team_number)
    data = {
        'team':team,
    }
    wins = 0
    losses = 0
    matchesr1 = Matches.objects.filter(red1=team_number)
    for i in matchesr1:
        if i.winner == "R":
            wins+=1
        else:
            losses+=1
    matchesr2 = Matches.objects.filter(red2=team_number)
    for i in matchesr2:
        if i.winner == "R":
            wins+=1
        else:
            losses+=1
    matchesb1 = Matches.objects.filter(blue1=team_number)
    for i in matchesb1:
        if i.winner == "B":
            wins+=1
        else:
            losses+=1
    matchesb2 = Matches.objects.filter(blue2=team_number)
    for i in matchesb2:
        if i.winner == "B":
            wins+=1
        else:
            losses+=1
    try:
        t = ResearchTeams.objects.get(name=team_number)
        data['matches'] = matchesr1, matchesr2, matchesb1, matchesb2
        data['research'] = t
    except:
        pass # team is not in research division
    return render(request, 'dashboard.html', data)

def divisionindex(request):
    teams = ResearchTeams.objects.all()
    return render(request, 'divisionindex.html', {'teams': teams})

def matches(request):
    matches = Matches.objects.all()
    teams = Teams.objects.all()
    return render(request, 'matches.html', {'matches': matches, 'teams':teams})
