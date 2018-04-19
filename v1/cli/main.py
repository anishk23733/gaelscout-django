#!/usr/bin/env python3
from raschietto import Raschietto, Matcher
import time
from scouting import update
from rankings import rankings
import analyze
from sys import platform
import os
from battle import battle

time.sleep(0.1)
print("Entering GaelScout Portal... ")
time.sleep(0.1)
print("Enter 'help' for commands and uses, and 'exit' to leave.")
time.sleep(0.2)

choice = ''
url = ''
spreadsheet=''

status = '5327B'

while choice != 'exit':
    with open('data/urls.txt', 'r') as filehandle:
        info = filehandle.read()
        info = info.split("\n")
        try:
            robotevents = info[0]
            page = Raschietto.from_url(robotevents)
            title = Matcher('.panel-title')
            title = title(page, multiple=False)
            status = title
        except:
            print("No Robot Events URL Entered. To fix this issue, run 'update <url>'")

    choice = input('GaelScout: '+status+'$ ')

    if choice.startswith("help") == True:
        print("")
        print("Current commands:")
        print("about (gives brief overview)")
        print("update <robot-events-url>")
        print("rankings <vex-db> (if used after update, vexdb url is unnecessary)")
        print("current (displays currently stored tournament)")
        print("add <team-number> (adds team number to the database to be analyzed)")
        print("analyze <team-number> (gives data on team)")
        print("open <scouting or rankings> (opens excel files)")
        print("battle <red1> <red2> <blue1> <blue2> (calculates chance of winning)")
        print("exit (closes CLI)")
        print("")

    elif choice.startswith("exit") == True:
        break

    elif choice.startswith("open") == True:
        choice = choice.split(" ")
        if len(choice) == 2:
            if choice[1] == "scouting":
                if platform == "darwin":
                    try: os.system("open -a 'Microsoft Excel.app' 'data/data.xlsx'")
                    except: print("Failed to open file. Please open it on your own.")
                elif platform == "win32":
                    try: os.system("open -a 'Microsoft Excel.exe' 'data/data.xlsx'")
                    except: print("Failed to open file. Please open it on your own.")
            elif choice[1] == "ranking":
                if platform == "darwin":
                    try: os.system("open -a 'Microsoft Excel.app' 'data/rankings.xlsx'")
                    except: print("Failed to open file. Please open it on your own.")
                elif platform == "win32":
                    try: os.system("open -a 'Microsoft Excel.exe' 'data/rankings.xlsx'")
                    except: print("Failed to open file. Please open it on your own.")
            else:
                print("Error: only 1 argument accepted, which is either 'scouting' or 'ranking'.")
        else:
            print("Error: only 1 argument accepted, which is either 'scouting' or 'ranking'.")

    elif choice.startswith("analyze") == True:
        choice = choice.split(" ")
        if len(choice) == 2:
            teamNum = choice[1]
            analyze.analyze(teamNum)
        else:
            print("Error: only 1 argument accepted, which is team number.")

    elif choice.startswith("add") == True:
        choice = choice.split(" ")
        if len(choice) == 2:
            teamNum = choice[1]
            analyze.collect(teamNum)

            try:
                # analyze.collect(teamNum)
                print("Stored data for "+teamNum+" in database.")
            except:
                print("Invalid team number.")
        else:
            print("Error: only 1 argument accepted, which is team number.")

    elif choice.startswith("about") == True:
        print("")
        print("Created by Anish Kachinthaya.")
        print("As the property of team 5327B, this tool uses Excel and web scraping libraries to scout teams.")
        print("")

    elif choice.startswith("current") == True:
        print("")
        print("Current Tournament")
        print(title)
        print("")

    elif choice.startswith("battle") == True:
        choice = choice.split(" ")
        if len(choice) == 5:
            #try:
            battle(choice[1],choice[2],choice[3],choice[4])
        else:
            print("Error: only 4 arguments accepted, which are team numbers.")
            print("Remember, 1st and 2nd are Red Allience, 3nd and 4th are Blue Alliance.")


    elif choice.startswith("rankings") == True:
        choice = choice.split(" ")
        if len(choice) == 1:
            rankings()

        elif len(choice) == 2:
            url = choice[1]
            rankings(url)

        else:
            print("Invalid.")

    elif choice.startswith("update") == True:
        choice = choice.split(" ")
        if len(choice) == 1:
            update(robotevents)

        elif len(choice) == 2:
            if choice[1].startswith("http://") == True or choice[1].startswith("https://") == True or choice[1].startswith("www.") == True:
                url = choice[1]
                update(url)
            else:
                print("Invalid url.")
                pass

        else:
            print("Invalid dimensions.")
            print("Try 'update --help' for more information.")

    else:
        print("bash: " + choice + ": command not found")
