from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
from progress.bar import Bar
from sys import platform
import os

# url = 'https://www.robotevents.com/robot-competitions/vex-robotics-competition/RE-VRC-17-4581.html'

def rankings(url:str=''):

    if(url != ''):
        pass
    else:
        with open('data/urls.txt', 'r') as filehandle:
            url = filehandle.read()
            url = url.replace("https://www.robotevents.com/robot-competitions/vex-robotics-competition/", '')
            url = url.replace(".html", '')
            url = url.replace("\n", '')
            if url.startswith("RE-VRC") == True:
                pass
            else:
                print("Invalid URL. Try updating again or try 'rankings <vexdb>'.")
                return 0
            url = 'https://vexdb.io/events/view/' + url+'?t=rankings'
            with open('data/urls.txt', 'a+') as filehandle2:
                filehandle2.write("\n"+url)

    page = Raschietto.from_url(url)
    rankNums = Matcher('.rank')
    rankNums = rankNums(page, multiple=True)
    try: rankNums.remove("Rank")
    except: pass
    rankNums = pd.Series(data=rankNums)

    teamNums = Matcher('.number')
    teamNums = teamNums(page, multiple=True)
    try: teamNums.remove("Number")
    except: pass
    teamNums = pd.Series(data=teamNums)

    teamNames = Matcher('.name>a')
    teamNames = teamNames(page, multiple=True)
    try: teamNames.remove("Name")
    except: pass
    teamNames = pd.Series(data=teamNames)

    wlts = Matcher('.wlt')
    wlts = wlts(page, multiple=True)
    try: wlts.remove("W-L-T")
    except: pass
    wlts = pd.Series(data=wlts)

    wpsps = Matcher('.wpsp')
    wpsps = wpsps(page, multiple=True)
    try: wpsps.remove("WP / AP / SP")
    except: pass
    wpsps = pd.Series(data=wpsps)

    maxScores = Matcher('.max_score')
    maxScores = maxScores(page, multiple=True)
    try: maxScores.remove("Max Score")
    except: pass
    maxScores = pd.Series(data=maxScores)

    trsps = Matcher('.trsp')
    trsps = trsps(page, multiple=True)
    try:
        trsps.remove("TRSPs")
    except: pass
    try:
        trsps.remove("TRSPs ")
    except: pass
    trsps = pd.Series(data=trsps)

    oprs = Matcher('.opr')
    oprs = oprs(page, multiple=True)
    try:
        oprs.remove("OPR")
    except: pass
    try:
        oprs.remove("OPR ")
    except: pass
    oprs = pd.Series(data=oprs)

    dprs = Matcher('.dpr')
    dprs = dprs(page, multiple=True)
    try:
        dprs.remove("DPR")
    except: pass
    try:
        dprs.remove("DPR ")
    except: pass
    dprs = pd.Series(data=dprs)

    ccwms = Matcher('.ccwm')
    ccwms = ccwms(page, multiple=True)
    try:
        ccwms.remove('CCWM')
    except: pass
    try:
        ccwms.remove('CCWM ')
    except: pass
    ccwms = pd.Series(data=ccwms)

    overallRankings = pd.DataFrame({"Rank":rankNums,"Numbers":teamNums,"Name":teamNames,"W-L-T":wlts,"WPSP":wpsps,"Max Score":maxScores,"TRSP":trsps,"OPR":oprs,"DPR":dprs,"CCWM":ccwms})
    overallRankings = overallRankings[["Rank", "Numbers", "Name", "W-L-T", "WPSP", "Max Score", "TRSP", "OPR", "DPR", "CCWM"]]
    # print(overallRankings)
    writer = pd.ExcelWriter("data/rankings.xlsx")
    overallRankings.to_excel(writer, sheet_name="Rankings")
    overallRankings.to_pickle("data/rankings.pkl")
    if platform == "darwin":
        try: os.system("open -a 'Microsoft Excel.app' 'data/rankings.xlsx'")
        except: print("Failed to open file. Please open it on your own.")
    elif platform == "win32":
        try: os.system("open -a 'Microsoft Excel.exe' 'data/rankings.xlsx'")
        except: print("Failed to open file. Please open it on your own.")

def collectRanking(teamNum:str, url:str=''):

    if(url != ''):
        pass
    else:
        with open('data/urls.txt', 'r') as filehandle:
            url = filehandle.read()
            url = url.replace("https://www.robotevents.com/robot-competitions/vex-robotics-competition/", '')
            url = url.replace(".html", '')
            url = url.replace("\n", '')
            if url.startswith("RE-VRC") == True:
                pass
            else:
                print("Invalid URL. Try updating again or try 'rankings <vexdb>'.")
                return 0
            url = 'https://vexdb.io/events/view/' + url+'?t=rankings'
            with open('data/urls.txt', 'a+') as filehandle2:
                filehandle2.write("\n"+url)

    page = Raschietto.from_url(url)
    rankNums = Matcher('.rank')
    rankNums = rankNums(page, multiple=True)
    try: rankNums.remove("Rank")
    except: pass

    teamNums = Matcher('.number')
    teamNums = teamNums(page, multiple=True)
    try: teamNums.remove("Number")
    except: pass

    index = teamNums.index(teamNum)
    rank = rankNums[index]
    return rank
