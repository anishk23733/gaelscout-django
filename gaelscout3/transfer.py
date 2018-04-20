import django 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gaelscout3.settings")
django.setup()
from teamindex.models import *
import pandas as pd
from scipy import stats
def getMatches():
    Matches.objects.all().delete()

    matchpkl = pd.read_pickle("static/data/matches.pkl")
    teamdatapkl = pd.read_pickle("static/data/sridata.pkl")
    print(teamdatapkl)
    for match, field, day, time, phase, red1, red2, blue1, blue2 in zip(matchpkl["Match"], matchpkl["Field"], matchpkl["Day"], matchpkl["Time"],matchpkl["Phase"], matchpkl["Red 1"], matchpkl["Red 2"], matchpkl["Blue 1"], matchpkl["Blue 2"],):
        try:
            red1id = list(teamdatapkl["Team Number"]).index(red1)
            red1opr = teamdatapkl["OPR"][red1id]
            red1mscore = teamdatapkl["Max Score"][red1id]
        except ValueError:
            red1opr = 0
            red1mscore = 0
        try:
            red2id = list(teamdatapkl["Team Number"]).index(red2)
            red2opr = teamdatapkl["OPR"][red2id]
            red2mscore = teamdatapkl["Max Score"][red2id]
        except ValueError:
            red2opr = 0
            red2mscore = 0
        try:
            blue1id = list(teamdatapkl["Team Number"]).index(blue1)
            blue1opr = teamdatapkl["OPR"][blue1id]
            blue1mscore = teamdatapkl["Max Score"][blue1id]
        except ValueError:
            blue1opr = 0
            blue1mscore = 0
        try:
            blue2id = list(teamdatapkl["Team Number"]).index(blue2)
            blue2opr = teamdatapkl["OPR"][blue2id]
            blue2mscore = teamdatapkl["Max Score"][blue2id]
        except:
            blue2opr = 0
            blue2mscore = 0

        totalscore1 = red1mscore + red2mscore
        totalscore2 = blue1mscore + blue2mscore
        if max(totalscore1, totalscore2) == totalscore1:
            winner = "R"
            percent = (-(totalscore2 - totalscore1) / totalscore2) * 100
        elif max(totalscore1, totalscore2) == totalscore2:
            winner = "B"
            percent = (-(totalscore1 - totalscore2) / totalscore1) * 100
        m = Matches(number=match, field=field, day=day, time=time, phase=phase, 
        red1=red1, red1_opr=red1opr, red1_mscore=red1mscore, 
        red2=red2, red2_opr=red2opr, red2_mscore=red2mscore, 
        blue1=blue1, blue1_opr=blue1opr, blue1_mscore=blue1mscore, 
        blue2=blue2, blue2_opr=blue2opr, blue2_mscore=blue2mscore, 
        winner=winner, chance=percent)
        m.save()     

def saveWinsLoss():
    for team in ResearchTeams.objects.all():
        t = team
        team_number = team.name
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
        t.w = wins
        t.l = losses
        t.save()

saveWinsLoss()