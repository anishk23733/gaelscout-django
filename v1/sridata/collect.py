from raschietto import Raschietto, Matcher
import pandas as pd

def collect(teamNum):
    scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(teamNum))

    # rankPointer = Matcher('.rank')
    # ranksList = rankPointer(scores, multiple=True)
    # try:
    #     ranksList.remove(ranksList[0])
    # except: pass
    # ranksList = list(map(int, ranksList))


    maxScorePointer = Matcher('.max_score')
    maxScoreList = maxScorePointer(scores, multiple=True)
    try:
        maxScoreList.remove(maxScoreList[0])
        maxScoreList = list(map(int, maxScoreList))
    except: pass

    OPRPointer = Matcher('.opr')
    OPRList = OPRPointer(scores, multiple=True)
    try:
        OPRList.remove(OPRList[0])
        OPRList = list(map(float, OPRList))
    except: pass


    # pdTeamRanks = pd.Series(data=ranksList)
    pdTeamMAXSCORES = pd.Series(data=maxScoreList)
    pdTeamOPRS = pd.Series(data=OPRList)

    # output = [pdTeamRanks[0:6].mean(), pdTeamMAXSCORES[0:6].mean(), pdTeamOPRS[0:6].mean()]
    output = [pdTeamMAXSCORES[0:3].mean(), pdTeamOPRS[0:3].mean()]

    return output
