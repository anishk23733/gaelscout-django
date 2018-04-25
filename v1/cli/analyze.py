from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
import os
import os.path
from sys import platform

def collect(teamNum):
    scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(teamNum))
    eventPointer = Matcher('.event')
    eventsList = eventPointer(scores, multiple=True)
    try:
        eventsList.remove(eventsList[0])
    except:
        eventsList.append("New Team")
    # teamEventsDict[teamNumber] = eventsList

    rankPointer = Matcher('.rank')
    ranksList = rankPointer(scores, multiple=True)
    try:
        ranksList.remove(ranksList[0])
    except:
        pass
    ranksList = list(map(int, ranksList))

    # teamRanksDict[teamNumber] = ranksList

    wltPointer = Matcher('.wlt')
    wltList = wltPointer(scores, multiple=True)
    try:
        wltList.remove(wltList[0])
    except:
        wltList.append("New Team")
    # teamWLTsDict[teamNumber] = eventsList

    WPSPPointer = Matcher('.wpsp')
    WPSPList = WPSPPointer(scores, multiple=True)
    try:
        WPSPList.remove(WPSPList[0])
    except:
        WPSPList.append("New Team")
    # teamWPSPsDict[teamNumber] = WPSPList

    maxScorePointer = Matcher('.max_score')
    maxScoreList = maxScorePointer(scores, multiple=True)
    try:
        maxScoreList.remove(maxScoreList[0])
        maxScoreList = list(map(int, maxScoreList))
    except:
        pass
    # teamMAXSCORESDict[teamNumber] = maxScoreList

    OPRPointer = Matcher('.opr')
    OPRList = OPRPointer(scores, multiple=True)
    try:
        OPRList.remove(OPRList[0])
        OPRList = list(map(float, OPRList))
    except:
        pass
    # teamOPRSDict[teamNumber] = OPRList


    pdTeamEvents = pd.Series(data=eventsList)
    pdTeamRanks = pd.Series(data=ranksList)
    pdTeamWLTs = pd.Series(data=wltList)
    pdTeamWPSPs = pd.Series(data=WPSPList)
    pdTeamMAXSCORES = pd.Series(data=maxScoreList)
    pdTeamOPRS = pd.Series(data=OPRList)
    pdTeamStats = pd.DataFrame({"Events":pdTeamEvents, "Ranks":pdTeamRanks, "WLT":pdTeamWLTs, "WPSP":pdTeamWPSPs, "Max Score":pdTeamMAXSCORES,"OPR":pdTeamOPRS})
    pdTeamStats.to_pickle("team_dataframes/"+teamNum+".pkl")

def analyze(teamNum):
    dir = "team_dataframes/"+teamNum+".pkl"
    if os.path.exists(dir):
        teamStats = pd.read_pickle(dir)
        # print(teamStats.describe())
        print("This data is based off of {}'s last 5 tournaments.".format(teamNum))
        try:
            print("Average OPR: {}".format(str(teamStats["OPR"][0:6].mean())))
            print("Average Max Score: {}".format(str(teamStats["Max Score"][0:6].mean())))
            print("Average Rank: {}".format(str(teamStats["Ranks"][0:6].mean())))
            print("Best Rank: {}".format(str(teamStats["Ranks"][0:6].min())))
        except:
            print("Average OPR: {}".format(str(teamStats["OPR"].mean())))
            print("Average Max Score: {}".format(str(teamStats["Max Score"].mean())))
            print("Average Rank: {}".format(str(teamStats["Ranks"].mean())))
            print("Best Rank: {}".format(str(teamStats["Ranks"].min())))


    else:
        print(teamNum+" is does not exist in the collected data.")
        print("Now collecting data.")
        try:
            collect(teamNum)
            print("Data collected. Run 'analyze' again to analyze the team.")
        except:
            print("Error: team number does not exist.")
    # plt.show()
