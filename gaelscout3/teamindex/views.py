from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from teamindex.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import TemplateView
from django.contrib.auth.models import User
import json
from raschietto import Matcher, Raschietto
import arrow
import pandas as pd
from itertools import chain
from operator import attrgetter

# Create your views here.
def home(request):
    return render(request, 'index.html')

def teamindex(request):
    teams = Teams.objects.all()
    paginator = Paginator(teams, 50) # Show 25 contacts per page
    page = request.GET.get('page')
    teams = paginator.get_page(page)
    query = request.GET.get("q")
    if query:
        teams = Teams.objects.filter(name__icontains=query)
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
    # data['matches'] =  sorted(chain(matchesr1, matchesr2, matchesb1, matchesb2), key=lambda instance: instance.order)
    # matchlist = []
    # matches = matchesr1, matchesr2, matchesb1, matchesb2
    # for match in matches:
    #     for m in match:
    #         matchlist.append(m)
    # for i in matchlist:
    #     q = i.number
    #     q = q.replace("Q", "")
    #     q = int(q)
    #     i.order = q
    # data['matches'] =  sorted(chain(matchesr1, matchesr2, matchesb1, matchesb2), key=attrgetter('order'))
    try:
        t = ResearchTeams.objects.get(name=team_number)
        matchlist = []
        matches = matchesr1, matchesr2, matchesb1, matchesb2
        for match in matches:
            for m in match:
                matchlist.append(m)
        for i in matchlist:
            q = i.number
            q = q.replace("Q", "")
            q = int(q)
            i.order = q
        data['matches'] = sorted(chain(matchesr1, matchesr2, matchesb1, matchesb2), key=attrgetter('order'))
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
    query = request.GET.get("q")
    if query:
        teams = ResearchTeams.objects.filter(name__icontains=query)
    return render(request, 'divisionindex.html', {'teams': teams})

def rankings(request):
    teams = ResearchTeams.objects.all()
    query = request.GET.get("q")
    if query:
        teams = ResearchTeams.objects.filter(name__icontains=query)
    ranks = []
    teams = sorted(teams, key = attrgetter("l"))

    for team, rank in zip(teams, range(len(teams))):
        ranks.append(rank+1)
    ranklist = zip(teams, ranks)
    return render(request, 'rankings.html', {'teams': ranklist})

def researchview(request):
    teams = ResearchTeams.objects.all()
    return render(request, 'ninuse/researchbubble.html', {'teams': teams})

def sri(request):
    teams = ResearchTeams.objects.all()
    df = pd.read_pickle("static/data/sridata.pkl")
    nums = list(df["Team Number"])
    js_nums = json.dumps(nums)
    oprs = list(df["OPR"])
    js_oprs = json.dumps(oprs)
    mscores = list(df["Max Score"])
    js_mscores = json.dumps(mscores)

    data = {
        'nums' : js_nums,
        'mscores' : js_mscores,
        'oprs' : js_oprs,
    }
    return render(request, 'sri.html', data)


def matches(request):
    matches = Matches.objects.all()
    teams = ResearchTeams.objects.all()
    bluecount = 0
    redcount = 0
    for match in matches:
        if match.winner == "B":
            bluecount+=1
        elif match.winner == "R":
            redcount+=1
    return render(request, 'matches.html', {'matches': matches, 'teams':teams, 'redcount':redcount, 'bluecount':bluecount})

def specmatch(request, match_number):
    matches = Matches.objects.get(number=match_number)
    try:
        redteam1 = ResearchTeams.objects.get(name=matches.red1)
        redteam2 = ResearchTeams.objects.get(name=matches.red2)
        blueteam1 = ResearchTeams.objects.get(name=matches.blue1)
        blueteam2 = ResearchTeams.objects.get(name=matches.blue2)
    except:
        return render(request, 'specmatch.html')
    data = {
        'matchnum' : match_number,
        'match' : matches,
        'red1' : redteam1,
        'red2' : redteam2,
        'blue1' : blueteam1,
        'blue2' : blueteam2,
    }
    return render(request, 'specmatch.html', data)
