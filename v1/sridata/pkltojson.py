import pandas as pd
import json
from scipy import stats

df = pd.read_pickle("sridata.pkl")
print(df)

data = {}

for teamNum, opr, mscore in zip(df["Team Number"], df["OPR"], df["Max Score"]):
    opr_per = stats.percentileofscore(df["OPR"], opr)
    mscr_per = stats.percentileofscore(df["Max Score"], mscore)
    data[teamNum] = [opr, opr_per, mscore, mscr_per]

with open('data.json', 'w') as fjson:
    json.dump(data, fjson, ensure_ascii=False, sort_keys=True, indent=4)
