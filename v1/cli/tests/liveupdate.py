from raschietto import Raschietto, Matcher
import time
from scouting import update
from rankings import rankings
import analyze
from sys import platform
import os
from battle import battle
from analyze import collect
from rankings import rankings, collectRanking

# with open('data/urls.txt', 'r') as filehandle:
#     info = filehandle.read()
#     info = info.split('\n')
#     if len(info) == 2:
#         vexdb = info[1]
#     else:
#         pass
#
# try:
#     rank = collectRanking('5327B', vexdb)
# except:
#     rank = collectRanking('5327B')
# print(rank)
def collectRankRE():
    with open('data/urls.txt', 'r') as filehandle:
        url = filehandle.read()
        url = url.split('\n')
        url = url[0]
    page = Raschietto.from_url(url)
    table = Matcher('#division-1 > div > div.col-md-4 > h4')
    table = table(page, multiple=True)
    print(table)

        # print("Run 'update <robot-events>' first.")
    #division-1 > div > div.col-md-4 > div > div > table > thead > tr > th
collectRankRE()
