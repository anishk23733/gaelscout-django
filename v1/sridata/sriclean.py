import pandas as pd
import pickle
import numpy as np
from sricollect import load
# import matplotlib.pyplot as plt
# import seaborn as sns
from raschietto import Raschietto, Matcher
from progress.bar import Bar

# def loadData():
#     with open('sri/data.pkl', 'rb') as handle:
#         teamData = pickle.load(handle)
#
#     return teamData

store = "Y"

if store == "Y":
    teams = load()
    bar = Bar('Cleaning Data', max= len(teams))
    for team in list(teams):# teams.keys():
        bar.next()
        try:
            for i in teams[team]:
                if i > 239:
                    del teams[team]
                    continue
        except: pass
        try:
            if np.isnan(teams[team][0]):
                del teams[team]
                continue
        except: pass
        try:
            teamPage = Raschietto.from_url("https://vexdb.io/teams/view/{}?t=rankings".format(team))
            season = Matcher(".text-center")
            season = season(teamPage, multiple=True)
            if season[0] != "In The Zone":
                del teams[team]
                print("FOUND ONE!")
        except: pass
    bar.finish()
    with open('sri/data.pkl', 'wb') as handle:
        pickle.dump(teams, handle, protocol=pickle.HIGHEST_PROTOCOL)
    # print(teams)
    exit()

# sns.set(color_codes=True)
#
# with open('sri/data.pkl', 'rb') as handle:
#     teamData = pickle.load(handle)
#
# xs = []
# ys = []
#
# for team in teamData:
#     xs.append(teamData[team][1])
#     ys.append(teamData[team][0])
#
# plt.scatter(xs, ys)
# plt.show()
