import django 
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "gaelscout3.settings")
django.setup()
from teamindex.models import *
import pandas as pd

Matches.objects.all().delete()

df = pd.read_pickle("static/data/matches.pkl")
for match, field, day, time, phase, red1, red2, blue1, blue2 in zip(df["Match"], df["Field"], df["Day"], df["Time"],df["Phase"], df["Red 1"], df["Red 2"], df["Blue 1"], df["Blue 2"],):
    red1id = Teams.objects.get(name=red1)
    red1opr = red1id.avg_opr
    red1oprpercent = red1id.opr_percentile
    red1mscore = red1id.avg_mscore
    red1mscorepercent = red1id.mscore_percentile
    red2id = Teams.objects.get(name=red2)
    red2opr = red2id.avg_opr
    red2oprpercent = red2id.opr_percentile
    red2mscore = red2id.avg_mscore
    red2mscorepercent = red2id.mscore_percentile
    blue1id = Teams.objects.get(name=blue1)
    blue1opr = blue1id.avg_opr
    blue1oprpercent = blue1id.opr_percentile
    blue1mscore = blue1id.avg_mscore
    blue1mscorepercent = blue1id.mscore_percentile
    blue2id = Teams.objects.get(name=blue2)
    blue2opr = blue2id.avg_opr
    blue2oprpercent = blue2id.opr_percentile
    blue2mscore = blue2id.avg_mscore
    blue2mscorepercent = blue2id.mscore_percentile
    # if max()
    m = Matches(number=match, field=field, day=day, time=time, phase=phase, 
    red1=red1, red1_opr=red1opr, red1_mscore=red1mscore, red1_opr_percentile=red1oprpercent, red1_mscore_percentile=red1mscorepercent, 
    red2=red2, red2_opr=red2opr, red2_mscore=red2mscore, red2_opr_percentile=red2oprpercent, red2_mscore_percentile=red2mscorepercent,
    blue1=blue1, blue1_opr=blue1opr, blue1_mscore=blue1mscore, blue1_opr_percentile=blue1oprpercent, blue1_mscore_percentile=blue1mscorepercent,  
    blue2=blue2, blue2_opr=blue2opr, blue2_mscore=blue2mscore, blue2_opr_percentile=blue2oprpercent, blue2_mscore_percentile=blue2mscorepercent,)