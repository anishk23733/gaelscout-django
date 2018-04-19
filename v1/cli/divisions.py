<<<<<<< HEAD
# https://hackernoon.com/raschietto-a-simple-library-for-web-scraping-46957c6aa5b7

from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
from progress.bar import Bar
import os
from sys import platform
import pygsheets

def predictions(division):
    gc = pygsheets.authorize(service_file='service_creds.json')
    sh = gc.open('Bot_Predictions')
    output = gc.open('Engineering Division')

    divisions = ["Science", "Technology", "Research", "Engineering", "Arts", "Math"]
    wks = sh.worksheet_by_title(division)

    teams = []
    teamNames = []
    organizations = []
    locations = []
    for row in wks:
        for column in row:
            if row.index(column) % 6 == 0:
                teams.append(column)
                teamNames.append(row[row.index(column) + 1])
                organizations.append(row[row.index(column) + 2])
                locations.append(row[row.index(column) + 3])

    teams.remove(teams[0])
    teamNames.remove(teamNames[0])
    organizations.remove(organizations[0])
    locations.remove(locations[0])

    teamNums = []
    teamNums = teams
    # teamNames = []
    # organizations = []
    # locations = []
    #
    # for i in range(len(teams)):
    #     if (i + 1) % 4 == 0:
    #         locations.append(teams[i].replace('\n', ' '))
    #         organizations.append(teams[i - 1])
    #         teamNames.append(teams[i - 2])
    #         teamNums.append(teams[i - 3])


    allEvents = []
    allRanks = []
    allWLTs = []
    allWPSPs = []
    allMAXSCORES = []
    allOPRS = []

    bar = Bar('Collecting Data', max=len(teamNums))


    for teamNumber in teamNums:
        scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(teamNumber))
        eventPointer = Matcher('.event')
        eventsList = eventPointer(scores, multiple=True)
        try: allEvents.append(eventsList[1])
        except: allEvents.append("New Team")
        try: eventsList.remove(eventsList[0])
        except: pass
        # teamEventsDict[teamNumber] = eventsList

        rankPointer = Matcher('.rank')
        ranksList = rankPointer(scores, multiple=True)
        try: allRanks.append(ranksList[1])
        except: allRanks.append("New Team")
        try: ranksList.remove(ranksList[0])
        except: pass
        ranksList = list(map(int, ranksList))

        # teamRanksDict[teamNumber] = ranksList

        wltPointer = Matcher('.wlt')
        wltList = wltPointer(scores, multiple=True)

        try: allWLTs.append(wltList[1] + " W-L-T")
        except: allWLTs.append("New Team")
        try: wltList.remove("W-L-T")
        except: pass

        newWLTList = []
        for i in wltList:
            i += " score"
            newWLTList.append(i)
        # teamWLTsDict[teamNumber] = eventsList

        WPSPPointer = Matcher('.wpsp')
        WPSPList = WPSPPointer(scores, multiple=True)
        try: allWPSPs.append(WPSPList[1])
        except: allWPSPs.append("New Team")
        try: WPSPList.remove(WPSPList[0])
        except: pass
        # teamWPSPsDict[teamNumber] = WPSPList

        maxScorePointer = Matcher('.max_score')
        maxScoreList = maxScorePointer(scores, multiple=True)
        try: allMAXSCORES.append(maxScoreList[1])
        except: allMAXSCORES.append("New Team")
        try: maxScoreList.remove(maxScoreList[0])
        except: pass
        maxScoreList = list(map(int, maxScoreList))

        # teamMAXSCORESDict[teamNumber] = maxScoreList

        OPRPointer = Matcher('.opr')
        OPRList = OPRPointer(scores, multiple=True)
        try: allOPRS.append(OPRList[1])
        except: allOPRS.append("New Team")
        try: OPRList.remove(OPRList[0])
        except: pass
        OPRList = list(map(float, OPRList))

        # teamOPRSDict[teamNumber] = OPRList

        pdTeamEvents = pd.Series(data=eventsList)

        pdTeamRanks = pd.Series(data=ranksList)

        pdTeamWLTs = pd.Series(data=newWLTList)

        pdTeamWPSPs = pd.Series(data=WPSPList)

        pdTeamMAXSCORES = pd.Series(data=maxScoreList)

        pdTeamOPRS = pd.Series(data=OPRList)

        pdAverages = pd.DataFrame([["Mean: ", pdTeamRanks.mean, '', '', pdTeamMAXSCORES.mean, pdTeamOPRS.mean]])
        pdTeamStats = pd.DataFrame({"Events":pdTeamEvents, "Ranks":pdTeamRanks, "WLT":pdTeamWLTs, "WPSP":pdTeamWPSPs, "Max Score":pdTeamMAXSCORES,"OPR":pdTeamOPRS})
        pdTeamStats.append(pdAverages)
        # pdTeamStats.to_excel(writer, sheet_name=teamNumber)
        pdTeamStats.to_pickle("divisiondata/"+teamNumber+".pkl")

        # wks = output.add_worksheet(teamNumber)
        # wks.set_dataframe(pdTeamStats, (1,1))

        # events = wks.cell('A1')
        # events.color = (0, 0, 0, 0)
        # events.set_text_format("foregroundColor", "#ffffff")
        bar.next()

    pdEvents = pd.Series(data=allEvents)
    pdRanks = pd.Series(data=allRanks)
    pdWLT = pd.Series(data=allWLTs)
    print(pdWLT)
    pdWPSP = pd.Series(data=allWPSPs)
    pdMaxScore = pd.Series(data=allMAXSCORES)
    pdOPR = pd.Series(data=allOPRS)

    pdTeamNums = pd.Series(data=teamNums)
    # pdTeamNames = pd.Series(data=teamNames)
    # pdOrganizations = pd.Series(data=organizations)
    # pdLocations = pd.Series(data=locations)

    # teamList = pd.DataFrame({ "Team Number: " : pdTeamNums, "Team Name: ": pdTeamNames, "Organization: ": pdOrganizations, "Location: ": pdLocations, "Most Recent Event: ": pdEvents, "Rank: ": pdRanks, "W-L-T: ": pdWLT, "WPSP: ": pdWPSP, "Max Score: ": pdMaxScore, "OPR: ": pdOPR})
    teamList = pd.DataFrame({ "Team Number: " : pdTeamNums, "Most Recent Event: ": pdEvents, "Rank: ": pdRanks, "W-L-T: ": pdWLT, "WPSP: ": pdWPSP, "Max Score: ": pdMaxScore, "OPR: ": pdOPR})
    # teamList = teamList[["Team Number: ", "Team Name: ", "Organization: ", "Location: ", "Most Recent Event: ", "Rank: ", "W-L-T: ", "WPSP: ", "Max Score: ", "OPR: "]]
    teamList = teamList[["Team Number: ", "Most Recent Event: ", "Rank: ", "W-L-T: ", "WPSP: ", "Max Score: ", "OPR: "]]

    # wks = output.add_worksheet("teamlist")
    # wks.set_dataframe(teamList, (1,1))

    teamList.to_pickle("divisiondata/teamList.pkl")
    bar.finish()
    print("Completed")
    print(output.url)

predictions("Engineering")
=======
# https://hackernoon.com/raschietto-a-simple-library-for-web-scraping-46957c6aa5b7

from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
from progress.bar import Bar
import os
from sys import platform
import pygsheets

def predictions(division):
    gc = pygsheets.authorize(service_file='service_creds.json')
    sh = gc.open('VEX Worlds 2018 High School Divisions')
    output = gc.open('Engineering Division')

    divisions = ["Science", "Technology", "Research", "Engineering", "Arts", "Math"]
    wks = sh.worksheet_by_title(division)

    teams = []
    teamNames = []
    organizations = []
    locations = []
    for row in wks:
        for column in row:
            if row.index(column) % 6 == 0:
                teams.append(column)
                teamNames.append(row[row.index(column) + 1])
                organizations.append(row[row.index(column) + 2])
                locations.append(row[row.index(column) + 3])

    teams.remove(teams[0])
    teamNames.remove(teamNames[0])
    organizations.remove(organizations[0])
    locations.remove(locations[0])

    teamNums = []
    teamNums = teams
    # teamNames = []
    # organizations = []
    # locations = []
    #
    # for i in range(len(teams)):
    #     if (i + 1) % 4 == 0:
    #         locations.append(teams[i].replace('\n', ' '))
    #         organizations.append(teams[i - 1])
    #         teamNames.append(teams[i - 2])
    #         teamNums.append(teams[i - 3])


    allEvents = []
    allRanks = []
    allWLTs = []
    allWPSPs = []
    allMAXSCORES = []
    allOPRS = []

    bar = Bar('Collecting Data', max=len(teamNums))


    for teamNumber in teamNums:
        scores = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(teamNumber))
        eventPointer = Matcher('.event')
        eventsList = eventPointer(scores, multiple=True)
        try: allEvents.append(eventsList[1])
        except: allEvents.append("New Team")
        try: eventsList.remove(eventsList[0])
        except: pass
        # teamEventsDict[teamNumber] = eventsList

        rankPointer = Matcher('.rank')
        ranksList = rankPointer(scores, multiple=True)
        try: allRanks.append(ranksList[1])
        except: allRanks.append("New Team")
        try: ranksList.remove(ranksList[0])
        except: pass
        ranksList = list(map(int, ranksList))

        # teamRanksDict[teamNumber] = ranksList

        wltPointer = Matcher('.wlt')
        wltList = wltPointer(scores, multiple=True)

        try: allWLTs.append(wltList[1] + " W-L-T")
        except: allWLTs.append("New Team")
        try: wltList.remove("W-L-T")
        except: pass

        newWLTList = []
        for i in wltList:
            i += " score"
            newWLTList.append(i)
        # teamWLTsDict[teamNumber] = eventsList

        WPSPPointer = Matcher('.wpsp')
        WPSPList = WPSPPointer(scores, multiple=True)
        try: allWPSPs.append(WPSPList[1])
        except: allWPSPs.append("New Team")
        try: WPSPList.remove(WPSPList[0])
        except: pass
        # teamWPSPsDict[teamNumber] = WPSPList

        maxScorePointer = Matcher('.max_score')
        maxScoreList = maxScorePointer(scores, multiple=True)
        try: allMAXSCORES.append(maxScoreList[1])
        except: allMAXSCORES.append("New Team")
        try: maxScoreList.remove(maxScoreList[0])
        except: pass
        maxScoreList = list(map(int, maxScoreList))

        # teamMAXSCORESDict[teamNumber] = maxScoreList

        OPRPointer = Matcher('.opr')
        OPRList = OPRPointer(scores, multiple=True)
        try: allOPRS.append(OPRList[1])
        except: allOPRS.append("New Team")
        try: OPRList.remove(OPRList[0])
        except: pass
        OPRList = list(map(float, OPRList))

        # teamOPRSDict[teamNumber] = OPRList

        pdTeamEvents = pd.Series(data=eventsList)

        pdTeamRanks = pd.Series(data=ranksList)

        pdTeamWLTs = pd.Series(data=newWLTList)

        pdTeamWPSPs = pd.Series(data=WPSPList)

        pdTeamMAXSCORES = pd.Series(data=maxScoreList)

        pdTeamOPRS = pd.Series(data=OPRList)

        pdAverages = pd.DataFrame([["Mean: ", pdTeamRanks.mean, '', '', pdTeamMAXSCORES.mean, pdTeamOPRS.mean]])
        pdTeamStats = pd.DataFrame({"Events":pdTeamEvents, "Ranks":pdTeamRanks, "WLT":pdTeamWLTs, "WPSP":pdTeamWPSPs, "Max Score":pdTeamMAXSCORES,"OPR":pdTeamOPRS})
        pdTeamStats.append(pdAverages)
        # pdTeamStats.to_excel(writer, sheet_name=teamNumber)
        pdTeamStats.to_pickle("divisiondata/"+teamNumber+".pkl")

        # wks = output.add_worksheet(teamNumber)
        # wks.set_dataframe(pdTeamStats, (1,1))

        # events = wks.cell('A1')
        # events.color = (0, 0, 0, 0)
        # events.set_text_format("foregroundColor", "#ffffff")
        bar.next()

    pdEvents = pd.Series(data=allEvents)
    pdRanks = pd.Series(data=allRanks)
    pdWLT = pd.Series(data=allWLTs)
    print(pdWLT)
    pdWPSP = pd.Series(data=allWPSPs)
    pdMaxScore = pd.Series(data=allMAXSCORES)
    pdOPR = pd.Series(data=allOPRS)

    pdTeamNums = pd.Series(data=teamNums)
    # pdTeamNames = pd.Series(data=teamNames)
    # pdOrganizations = pd.Series(data=organizations)
    # pdLocations = pd.Series(data=locations)

    # teamList = pd.DataFrame({ "Team Number: " : pdTeamNums, "Team Name: ": pdTeamNames, "Organization: ": pdOrganizations, "Location: ": pdLocations, "Most Recent Event: ": pdEvents, "Rank: ": pdRanks, "W-L-T: ": pdWLT, "WPSP: ": pdWPSP, "Max Score: ": pdMaxScore, "OPR: ": pdOPR})
    teamList = pd.DataFrame({ "Team Number: " : pdTeamNums, "Most Recent Event: ": pdEvents, "Rank: ": pdRanks, "W-L-T: ": pdWLT, "WPSP: ": pdWPSP, "Max Score: ": pdMaxScore, "OPR: ": pdOPR})
    # teamList = teamList[["Team Number: ", "Team Name: ", "Organization: ", "Location: ", "Most Recent Event: ", "Rank: ", "W-L-T: ", "WPSP: ", "Max Score: ", "OPR: "]]
    teamList = teamList[["Team Number: ", "Most Recent Event: ", "Rank: ", "W-L-T: ", "WPSP: ", "Max Score: ", "OPR: "]]

    # wks = output.add_worksheet("teamlist")
    # wks.set_dataframe(teamList, (1,1))

    teamList.to_pickle("divisiondata/teamList.pkl")
    bar.finish()
    print("Completed")
    print(output.url)

predictions("Research")
>>>>>>> 59ecc5e3e7774a69622649af8fe8c253c343f9d1
