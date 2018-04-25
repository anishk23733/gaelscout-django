#!/usr/bin/env python3
from raschietto import Raschietto, Matcher
import pandas as pd
from collect import collect
from progress.bar import Bar


df = pd.read_pickle("team_dataframes/teamList.pkl")

teamList = df["Team Number: "].tolist()

# page = Raschietto.from_url("https://vexdb.io/events/view/RE-VRC-17-4462")
# teamNums = Matcher('.number')
# teamList = teamNums(page, multiple=True)
teamStats = []

bar = Bar('Collecting Team Data', max=len(teamList))
for team in teamList:
    teamStats.append(collect(team))
    bar.next()
bar.finish()

page = Raschietto.from_url("https://vexdb.io/events/view/RE-VRC-17-4462?t=results")
results = Matcher('.result-box')
results = results(page, multiple=True)

blueScores = []
blueAlliance1 = []
blueAlliance2 = []

redScores = []
redAlliance1 = []
redAlliance2 = []

for i in range(len(results)):
    if (i+1) % 6 == 0:
        blueScores.append(results[i])
        redScores.append(results[i-1])
        blueAlliance1.append(results[i-3])
        blueAlliance2.append(results[i-2])
        redAlliance1.append(results[i-5])
        redAlliance2.append(results[i-4])

redScores = list(map(float, redScores))
blueScores = list(map(float, blueScores))

# print(redScores, blueScores)

winners = []

for r, b in zip(redScores, blueScores):
    if max(r, b) == r:
        winners.append("R")
    elif max(r, b) == b:
        winners.append("B")

blue1Data = []
blue2Data = []
red1Data = []
red2Data = []


bar = Bar('Appending Team Data to Matches', max=len(blueAlliance1)+len(blueAlliance2)+len(redAlliance1)+len(redAlliance2))

for b1, b2, r1, r2 in zip(blueAlliance1, blueAlliance2, redAlliance1, redAlliance2):
    blue1Data.append(teamStats[teamList.index(b1)])
    bar.next()
    blue2Data.append(teamStats[teamList.index(b2)])
    bar.next()
    red1Data.append(teamStats[teamList.index(r1)])
    bar.next()
    red2Data.append(teamStats[teamList.index(r2)])
    bar.next()

bar.finish()


main = pd.DataFrame({"Blue 1":blueAlliance1, "Data B1":blue1Data, "Blue 2":blueAlliance2,"Data B2":blue2Data,"Red 1":redAlliance1,"Data R1":red1Data, "Red 2":redAlliance2, "Data R2":red2Data,"Winner":winners})
main = main[["Blue 1", "Data B1", "Blue 2","Data B2", "Red 1", "Data R1", "Red 2", "Data R2", "Winner"]]

print(main)
