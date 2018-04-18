import pandas as pd
import numpy as np
from scipy import stats
teams = []
avg_opr = []
avg_rank = []
avg_mscore = []
opr_percentile = []
mscore_percentile = []

df = pd.read_pickle("divisionrawdata/teamList.pkl")
for team in df["Team Number: "]:
    dir = "divisionrawdata/"+team+".pkl"
    team1Stats = pd.read_pickle(dir)
    try:
        if np.isnan(team1Stats["OPR"][0:6].mean()):
            pass
        else:
            avgopr1 = team1Stats["OPR"][0:6].mean()
            avgscore1 = team1Stats["Max Score"][0:6].mean()
            avgrank1 = team1Stats["Ranks"][0:6].mean()
            teams.append(team)
            avg_opr.append(avgopr1)
            avg_rank.append(avgrank1)
            avg_mscore.append(avgscore1)
    except:
        pass
#     try:
#         avgopr1 = team1Stats["OPR"][0:6].mean()
#         avgscore1 = team1Stats["Max Score"][0:6].mean()
#         avgrank1 = team1Stats["Ranks"][0:6].mean()
#     except:
#         avgopr1 = team1Stats["OPR"].mean()
#         avgscore1 = team1Stats["Max Score"].mean()
#         avgrank1 = team1Stats["Ranks"].mean()
for team, opr, mscore in zip(teams, avg_opr, avg_mscore):
    opr_per = stats.percentileofscore(avg_opr, opr)
    opr_percentile.append(opr_per)
    mscr_per = stats.percentileofscore(avg_mscore, mscore)
    mscore_percentile.append(mscr_per)

df = pd.DataFrame({"Team":teams,"OPR":avg_opr, "Rank":avg_rank, "Max Score":avg_mscore, "OPR Percentile":opr_percentile, "Max Score Percentile":mscore_percentile,})
df = df.sort_values(["OPR Percentile"], ascending=False)

df = df[["Team", "OPR", "OPR Percentile", "Rank", "Max Score", "Max Score Percentile"]]
df.to_pickle("divisionteamdata.pkl")
writer = pd.ExcelWriter('data.xlsx')
df.to_excel(writer, "Research Division")
writer.save()