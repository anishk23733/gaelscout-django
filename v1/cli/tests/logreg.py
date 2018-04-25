from raschietto import Raschietto, Matcher
import pandas as pd
from collect import collect

df = pd.read_pickle("team_dataframes/teamList.pkl")

teamList = df["Team Number: "].tolist()

# List of lists, [[Ranks, MaxScores, OPRs], [Ranks, MaxScores, OPRs]... ]
# teamStats = []
# for team in teamList:
#     teamStats.append(collect(team))

def model(teamName):
    url = "https://vexdb.io/teams/view/{}?t=results".format(teamName)
    page = Raschietto.from_url(url)
    link_matcher = Matcher.link("#table-content > div > table > thead > tr > td > a", startswith="https://vexdb.io")
    # results = Matcher('.result-red' or '.result-red-fade')
    teamEvents = link_matcher(page, multiple=True)

    for i in teamEvents:
        teamEvents[teamEvents.index(i)] = "{}?t=results".format(i)

    print(teamName)
    print("Found events")
    print(teamEvents)


    for event in teamEvents:
        header = Matcher(".page-header")
        header = header(page, multiple=False)

        print("Scraping event: {}".format(header))
        url = event
        page = Raschietto.from_url(url)
        results = Matcher('.result-box')
        results = results(page, multiple=True)

        blueScores = []
        blueAlliance1 = []
        blueAlliance2 = []

        redScores = []
        redAlliance1 = []
        redAlliance2 = []
        matches = []

        for i in range(len(results)):
            if (i+1) % 6 == 0:
                blueScores = results[i]
                redScores = results[i-1]
                blueAlliance1 = results[i-3]
                blueAlliance2 = results[i-2]
                redAlliance1 = results[i-5]
                redAlliance2 = results[i-4]

                winloss = 0
                winner = ''
                if teamName == blueAlliance1 or teamName == blueAlliance2 or teamName == redAlliance1 or teamName == redAlliance2:
                    if teamName == blueAlliance1 or teamName == blueAlliance2:
                        if blueScores > redScores:
                            winloss = 1
                            winner = 'B'
                        else:
                            winloss = 0
                            winner = 'R'
                    elif teamName == redAlliance1 or teamName == redAlliance2:
                        if redScores >= blueScores:
                            winloss = 1
                            winner = 'R'
                        else:
                            winloss = 0
                            winner = 'B'

                    try: matches.append([blueAlliance1, blueAlliance2, redAlliance1, redAlliance2, int(blueScores), int(redScores), winloss, winner])
                    except: pass
                else:
                    pass

        for match in matches:
            b1 = collect(match[0])[1]
            b2 = collect(match[1])[1]
            r1 = collect(match[2])[1]
            r2 = collect(match[3])[1]

            if match[7] == "B":
                oprd = [((b1+b1)-(r1+r2)), match[6]]
            elif match[7] == "R":
                oprd = [((r1+r2)-(b1+b1)), match[6]]

            print(oprd)
print(model("86868R"))
