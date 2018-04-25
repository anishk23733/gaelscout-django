from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
import os
import os.path
from sys import platform
import analyze

def battle(team1, team2, team3, team4):
    dir1 = "team_dataframes/"+team1+".pkl"
    dir2 = "team_dataframes/"+team2+".pkl"
    dir3 = "team_dataframes/"+team3+".pkl"
    dir4 = "team_dataframes/"+team4+".pkl"

    if os.path.exists(dir1):
        team1Stats = pd.read_pickle(dir1)
        # print(teamStats.describe())
        try:
            avgopr1 = team1Stats["OPR"][0:6].mean()
            avgscore1 = team1Stats["Max Score"][0:6].mean()
            avgrank1 = team1Stats["Ranks"][0:6].mean()
        except:
            avgopr1 = team1Stats["OPR"].mean()
            avgscore1 = team1Stats["Max Score"].mean()
            avgrank1 = team1Stats["Ranks"].mean()

    else:
        print(team1 + " does not exist in database.")
        print("Try adding it with 'add <team-num>'.")
        analyze.collect(team1)
        return 0;

    if os.path.exists(dir2):
        team2Stats = pd.read_pickle(dir2)
        # print(teamStats.describe())
        try:
            avgopr2 = team2Stats["OPR"][0:6].mean()
            avgscore2 = team2Stats["Max Score"][0:6].mean()
            avgrank2 = team2Stats["Ranks"][0:6].mean()
        except:
            avgopr2 = team2Stats["OPR"].mean()
            avgscore2 = team2Stats["Max Score"].mean()
            avgrank2 = team2Stats["Ranks"].mean()

    else:
        print(team2 + " does not exist in database.")
        print("Try adding it with 'add <team-num>'.")
        analyze.collect(team2)
        return 0;

    if os.path.exists(dir3):
        team3Stats = pd.read_pickle(dir3)
        # print(teamStats.describe())
        try:
            avgopr3 = team3Stats["OPR"][0:6].mean()
            avgscore3 = team3Stats["Max Score"][0:6].mean()
            avgrank3 = team3Stats["Ranks"][0:6].mean()
        except:
            avgopr3 = team3Stats["OPR"].mean()
            avgscore3 = team3Stats["Max Score"].mean()
            avgrank3 = team3Stats["Ranks"].mean()

    else:
        print(team3 + " does not exist in database.")
        print("Try adding it with 'add <team-num>'.")
        analyze.collect(team3)
        return 0;


    if os.path.exists(dir4):
        team4Stats = pd.read_pickle(dir4)
        # print(teamStats.describe())
        avgopr4 = team4Stats["OPR"].mean()
        avgscore4 = team4Stats["Max Score"].mean()
        avgrank4 = team4Stats["Ranks"].mean()
    else:
        print(team4 + " does not exist in database.")
        print("Try adding it with 'add <team-num>'.")
        analyze.collect(team4)
        return 0;

    totalscore1 = avgscore1 + avgscore2
    totalscore2 = avgscore3 + avgscore4

    # points1 = 0
    # points2 = 0
    #
    # if max(totalscore1, totalscore2) == totalscore1:
    #     points1 += 3
    # elif max(totalscore1, totalscore2) == totalscore2:
    #     points2 += 3
    #
    # if avgopr1 > avgopr3:
    #     points1 + 1

    if max(totalscore1, totalscore2) == totalscore1:
        percent = (-(totalscore2 - totalscore1) / totalscore2) * 100
        print("{} and {} have a {}% greater chance of winning to {} and {}.".format(team1, team2, str(percent), team3, team4))
    elif max(totalscore1, totalscore2) == totalscore2:
        percent = (-(totalscore1 - totalscore2) / totalscore1) * 100
        print("{} and {} have a {}% greater chance of winning to {} and {}.".format(team3, team4, str(percent), team1, team2))
