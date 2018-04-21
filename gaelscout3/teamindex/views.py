from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from teamindex.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import json
from raschietto import Matcher, Raschietto
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
    matchesr1 = Matches.objects.filter(red1=team_number)
    matchesr2 = Matches.objects.filter(red2=team_number)
    matchesb1 = Matches.objects.filter(blue1=team_number)
    matchesb2 = Matches.objects.filter(blue2=team_number)
    try:
        t = ResearchTeams.objects.get(name=team_number)
        data['matches'] = matchesr1, matchesr2, matchesb1, matchesb2
        data['research'] = t
    except:
        pass # team is not in research division
    scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(team_number))
    OPRPointer = Matcher('.opr')
    OPRList = OPRPointer(scores, multiple=True)
    try: OPRList.remove(OPRList[0])
    except: pass
    OPRList = list(map(float, OPRList))
    js_opr = json.dumps(OPRList)

    rankPointer = Matcher('.rank')
    ranksList = rankPointer(scores, multiple=True)
    try: ranksList.remove(ranksList[0])
    except: pass
    ranksList = list(map(int, ranksList))
    js_ranks = json.dumps(ranksList)

    maxScorePointer = Matcher('.max_score')
    maxScoreList = maxScorePointer(scores, multiple=True)
    try: maxScoreList.remove(maxScoreList[0])
    except: pass
    maxScoreList = list(map(int, maxScoreList))
    js_mscores = json.dumps(maxScoreList)

    data["js_oprs"] = js_opr
    data["js_ranks"] = js_ranks
    data["js_mscores"] = js_mscores
    return render(request, 'dashboard.html', data)

def divisionindex(request):
    teams = ResearchTeams.objects.all()
    return render(request, 'divisionindex.html', {'teams': teams})

def matches(request):
    matches = Matches.objects.all()
    teams = Teams.objects.all()
    return render(request, 'matches.html', {'matches': matches, 'teams':teams})
