from raschietto import Raschietto, Matcher
import pandas as pd
from openpyxl import load_workbook, Workbook
from progress.bar import Bar
import os
from sys import platform
import pygsheets


gc = pygsheets.authorize(service_file='../service_creds.json')
sh = gc.open('Bot_Predictions')
output = gc.open('Engineering Division')

divisions = ["Science", "Technology", "Research", "Engineering", "Arts", "Math"]
wks = sh.worksheet_by_title(divisions[3])

teams = []
teamNames = []
organization = []
location = []

for row in wks:
    for column in row:
        if row.index(column) % 6 == 0:
            teams.append(column)
            teamNames.append(row[row.index(column) + 1])
            organization.append(row[row.index(column) + 2])
            location.append(row[row.index(column) + 3])

teams.remove(teams[0])
teamNames.remove(teamNames[0])
organization.remove(organization[0])
location.remove(location[0])

print(teams)
print(teamNames)
print(organization)
print(location)
