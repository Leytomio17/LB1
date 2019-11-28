import pandas as pd
import numpy as np
import matplotlib
import seaborn as sns
import glob

files = glob.glob("states*.csv")

us_census = []
for filename in files:
    us_census.append(pd.read_csv(filename))

us_census = pd.concat(us_census)

us_census.Income = us_census['Income'].replace(['^\$'], '', regex=True)
us_census.Income = pd.to_numeric(us_census['Income'])

gender_split = us_census['GenderPop'].str.split("_")
us_census['men'] = gender_split.str.get(0)
us_census['women'] = gender_split.str.get(1)

us_census.men = us_census['men'].replace(['M$'], '', regex=True)
us_census.men = pd.to_numeric(us_census['men'])

us_census.women = us_census['women'].replace(['F$'], '', regex=True)
us_census.women = pd.to_numeric(us_census['women'])

print(us_census.head())
print(us_census.dtypes)

plt.scatter(women, Income)
