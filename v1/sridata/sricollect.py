from raschietto import Raschietto, Matcher
import pandas as pd
from collect import collect
import random
import pickle
from progress.bar import Bar
from multiprocessing import Process

teamPage = Raschietto.from_url("https://vexdb.io/teams?p=1")
maxPageNum = Matcher(".pagination > li")
maxPageNum = maxPageNum(teamPage, multiple=True)
maxPageNum = int(maxPageNum[len(maxPageNum) - 2])

start = random.randint(1, ((maxPageNum * 50)))

try:
    with open('teams.pkl', 'rb') as f:
        teams = pickle.load(f)

    # print(len(teams))
except:
    print("No team list exists. Collecting data now.")
    bar = Bar('Collecting All Team #s', max= (maxPageNum * 50))

    teams = []
    teamList = []
    orgs = []
    for i in range(1, maxPageNum):
        teamPage = Raschietto.from_url("https://vexdb.io/teams?p={}".format(i))
        teamPointer = Matcher('.number')
        teamList = teamPointer(teamPage, multiple=True)

        orgPointer = Matcher('.program')
        orgs = orgPointer(teamPage, multiple=True)

        for team, org in zip(teamList, orgs):
            if org == "VRC":
                teams.append(team)
            bar.next()

    with open('teams.pkl', 'wb') as f:
        pickle.dump(teams, f)
    bar.finish()

data1 = {}
data2 = {}
data3 = {}
data4 = {}
data5 = {}
data6 = {}
data7 = {}
data8 = {}
data9 = {}
data10 = {}
data11= {}
data12 = {}
data13 = {}
data14 = {}
# bar = Bar('Collecting SRIs', max=len(teams))
# for team in teams:
#     data[team] = collect(team)
#     bar.next()
# bar.finish()
#
# with open('data.pkl', 'wb') as handle:
#     pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
#
# print(data)

try:
    print(0/0)
    # with open('data.pkl', 'rb') as handle:
    #     data = pickle.load(handle)
    #     print(data)
except:
    def loop1():
        bar = Bar('Collecting SRIs', max= (int((1/14)*len(teams))))
        for team in teams[0:(int((1/14)*len(teams)))]:
            data1[team] = collect(team)
            # print(data)
            bar.next()
        with open('sri/data1.pkl', 'wb') as handle:
            pickle.dump(data1, handle, protocol=pickle.HIGHEST_PROTOCOL)
        bar.finish()

    def loop2():
        for team in teams[(int((1/14)*len(teams))):(int((2/14)*len(teams)))]:
            data2[team] = collect(team)
        with open('sri/data2.pkl', 'wb') as handle:
            pickle.dump(data2, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop3():
        for team in teams[(int((2/14)*len(teams))):(int((3/14)*len(teams)))]:
            data3[team] = collect(team)
        with open('sri/data3.pkl', 'wb') as handle:
            pickle.dump(data3, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop4():
        for team in teams[(int((3/14)*len(teams))):(int((4/14)*len(teams)))]:
            data4[team] = collect(team)
        with open('sri/data4.pkl', 'wb') as handle:
            pickle.dump(data4, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop5():
        for team in teams[(int((4/14)*len(teams))):(int((5/14)*len(teams)))]:
            data5[team] = collect(team)
        with open('sri/data5.pkl', 'wb') as handle:
            pickle.dump(data5, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop6():
        for team in teams[(int((5/14)*len(teams))):(int((6/14)*len(teams)))]:
            data6[team] = collect(team)
        with open('sri/data6.pkl', 'wb') as handle:
            pickle.dump(data6, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop7():
        for team in teams[(int((6/14)*len(teams))):(int((7/14)*len(teams)))]:
            data7[team] = collect(team)
        with open('sri/data7.pkl', 'wb') as handle:
            pickle.dump(data7, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop8():
        for team in teams[(int((7/14)*len(teams))):(int((8/14)*len(teams)))]:
            data8[team] = collect(team)
        with open('sri/data8.pkl', 'wb') as handle:
            pickle.dump(data8, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop9():
        for team in teams[(int((8/14)*len(teams))):(int((9/14)*len(teams)))]:
            data9[team] = collect(team)
        with open('sri/data9.pkl', 'wb') as handle:
            pickle.dump(data9, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop10():
        for team in teams[(int((9/14)*len(teams))):(int((10/14)*len(teams)))]:
            data10[team] = collect(team)
        with open('sri/data10.pkl', 'wb') as handle:
            pickle.dump(data10, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop11():
        for team in teams[(int((10/14)*len(teams))):(int((11/14)*len(teams)))]:
            data11[team] = collect(team)
        with open('sri/data11.pkl', 'wb') as handle:
            pickle.dump(data11, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop12():
        for team in teams[(int((11/14)*len(teams))):(int((12/14)*len(teams)))]:
            data12[team] = collect(team)
        with open('sri/data12.pkl', 'wb') as handle:
            pickle.dump(data12, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop13():
        for team in teams[(int((12/14)*len(teams))):(int((13/14)*len(teams)))]:
            data13[team] = collect(team)
        with open('sri/data13.pkl', 'wb') as handle:
            pickle.dump(data13, handle, protocol=pickle.HIGHEST_PROTOCOL)
    def loop14():
        for team in teams[(int((13/14)*len(teams))):len(teams)]:
            data14[team] = collect(team)
        with open('sri/data14.pkl', 'wb') as handle:
            pickle.dump(data14, handle, protocol=pickle.HIGHEST_PROTOCOL)

    if __name__ == '__main__':
        Process(target=loop1).start()
        Process(target=loop2).start()
        Process(target=loop3).start()
        Process(target=loop4).start()
        Process(target=loop5).start()
        Process(target=loop6).start()
        Process(target=loop7).start()
        Process(target=loop8).start()
        Process(target=loop9).start()
        Process(target=loop10).start()
        Process(target=loop11).start()
        Process(target=loop12).start()
        Process(target=loop13).start()
        Process(target=loop14).start()

def load():
    with open('sri/data1.pkl', 'rb') as handle:
        data1 = pickle.load(handle)
    with open('sri/data2.pkl', 'rb') as handle:
        data2 = pickle.load(handle)
    with open('sri/data3.pkl', 'rb') as handle:
        data3 = pickle.load(handle)
    with open('sri/data4.pkl', 'rb') as handle:
        data4 = pickle.load(handle)
    with open('sri/data5.pkl', 'rb') as handle:
        data5 = pickle.load(handle)
    with open('sri/data6.pkl', 'rb') as handle:
        data6 = pickle.load(handle)
    with open('sri/data7.pkl', 'rb') as handle:
        data7 = pickle.load(handle)
    with open('sri/data8.pkl', 'rb') as handle:
        data8 = pickle.load(handle)
    with open('sri/data9.pkl', 'rb') as handle:
        data9 = pickle.load(handle)
    with open('sri/data10.pkl', 'rb') as handle:
        data10 = pickle.load(handle)
    with open('sri/data11.pkl', 'rb') as handle:
        data11 = pickle.load(handle)
    with open('sri/data12.pkl', 'rb') as handle:
        data12 = pickle.load(handle)
    with open('sri/data13.pkl', 'rb') as handle:
        data13 = pickle.load(handle)
    with open('sri/data14.pkl', 'rb') as handle:
        data14 = pickle.load(handle)
    return {**data1, **data2, **data3, **data4, **data5, **data6, **data7, **data8, **data9, **data10, **data11, **data12, **data13, **data14}
# print(load())
