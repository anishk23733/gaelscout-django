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
    return render(request, 'dashboard.html', data)

def divisionindex(request):
    teams = ResearchTeams.objects.all()
    return render(request, 'divisionindex.html', {'teams': teams})
def matches(request):
    matches = Matches.objects.all()
    teams = Teams.objects.all()
    return render(request, 'matches.html', {'matches': matches, 'teams':teams})
