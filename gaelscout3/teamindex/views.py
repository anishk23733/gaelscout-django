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
<<<<<<< HEAD
    return render(request, 'divisionindex.html', {'teams': teams})
=======
    return render(request, 'divisionindex.html', {'teams': teams})
>>>>>>> 3e66a6e39dbab0cf41a632a788883bb5fc3af2b1
