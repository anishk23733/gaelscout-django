# https://hackernoon.com/raschietto-a-simple-library-for-web-scraping-46957c6aa5b7

from raschietto import Raschietto, Matcher
import pandas as pd
import os
from sys import platform
import pygsheets
import pickle
def predictions():
    gc = pygsheets.authorize(service_file='service_creds.json')
    sh = gc.open('Research Match Schedule Python')

    wks = sh.worksheet_by_title("Schedule")


    string = []
    array = []
    for row in wks:
        for i in row:
            if i != '':
                string.append(i)
    # for i in array:
    #     if i in array:
    #         array.remove(i)
    with open('rawmatches.pkl', 'wb') as f:
        pickle.dump(string, f)

def split():
    number = []
    field = []
    day = []
    time = []
    phase = []
    red1 = []
    red2 = []
    blue1 = []
    blue2 = []

    with open('rawmatches.pkl', 'rb') as f:
        matches = pickle.load(f)
    for i in matches:
        i = i.split(" ")
        number.append(i[0].replace("*", ""))
        field.append(i[1].replace("*", ""))
        day.append(i[2].replace("*", ""))
        time.append(i[3].replace("*", ""))
        phase.append(i[4].replace("*", ""))
        red1.append(i[5].replace("*", ""))
        red2.append(i[6].replace("*", ""))
        blue1.append(i[7].replace("*", ""))
        blue2.append(i[8].replace("*", ""))
    df = pd.DataFrame({"Match":number, "Field":field, "Day":day, "Time":time,"Phase":phase, "Red 1":red1,"Red 2":red2,"Blue 1":blue1,"Blue 2":blue2})
    df = df[["Match", "Field", "Day", "Time", "Phase", "Red 1", "Red 2", "Blue 1", "Blue 2"]]
    df.to_pickle("matches.pkl")
    print(df)
split()