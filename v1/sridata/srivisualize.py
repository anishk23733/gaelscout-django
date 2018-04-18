# https://elitedatascience.com/python-seaborn-tutorial
from matplotlib import pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sridata = pd.read_pickle("sridata.pkl")
# sridataplain = sridata.drop(["Category", "Team Number"], axis=1)

# for i in range(len(sridata)):
#     if sridata["Max Score"][i] > 150:
#         print(sridata["Team Number"][i])
# X = sridata["OPR"]
# y = sridata["Max Score"]
#
# model = sm.OLS(y, X).fit()
# predictions = model.predict(X)
# model.summary()

# sns.jointplot(x='OPR', y='Max Score', data=sridataplain)

# For Hue
# sns.lmplot(x='OPR', y='Max Score', data=sridata, fit_reg=True, hue="Category")

# plot.get_lines()[0].get_xdata()
# plot.get_lines()[0].get_ydata()

# BOX PLOT
# sns.boxplot(data=sridata)

# VIOLIN PLOT
# sns.set_style('whitegrid')
# sns.violinplot(x='OPR', y='Max Score', data=sridataplain)

# Histogram
# sns.distplot(sridataplain["Max Score"])

# Density Plot
# sns.kdeplot(sridataplain["OPR"], sridataplain["Max Score"])

# LINEAR REGRESSION SCATTER PLOT
# print(sridata["Team Number"])
plot = sns.lmplot(x='OPR', y='Max Score', data=sridata, fit_reg=True)
plt.ylim(0, None)
plt.title("Score Rating Index")
plt.show()
