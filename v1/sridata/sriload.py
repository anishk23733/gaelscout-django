# from sriclean import loadData
import pickle
import pandas as pd

def loadData():
    with open('sri/data.pkl', 'rb') as handle:
        teamData = pickle.load(handle)

    return teamData

teamData = loadData()

teams = list(teamData)
oprs = []
mscores = []

for team in teamData:
    oprs.append(teamData[team][1])
    mscores.append(teamData[team][0])

# plt.scatter(oprs, mscores)
# plt.show()

teams = pd.Series(teams)
oprs = pd.Series(oprs)
category = []
for i in oprs:
    if i  > oprs.quantile(.9):
        category.append("A")
    elif i > oprs.quantile(.75):
        category.append("B")
    elif i > oprs.quantile(.5):
        category.append("C")
    else:
        category.append("D")

mscores = pd.Series(mscores)
sri = pd.DataFrame({"Team Number":teams, "OPR":oprs, "Max Score":mscores, "Category":category})
sri = sri[["Team Number", "OPR", "Max Score", "Category"]]

sri.to_pickle("sridata.pkl")
# print(sri)
# sns.lmplot(x='OPR', y='Max Score', data=sri, fit_reg=True, hue='Category')

# Using Code
# sns.lmplot(x='OPR', y='Max Score', data=sri, fit_reg=True)
# plt.ylim(0, None)
#
# plt.show()
