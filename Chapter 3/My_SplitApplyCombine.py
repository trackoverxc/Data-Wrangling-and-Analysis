import pandas as pd
import os
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')
df = pd.read_csv('eu_trade_sums.csv')
df
df.head()
grp = df.groupby(['partner', 'trade_type'])
grp2 = df.groupby(['trade_type'])
grp2.mean()
grp
for name, group in grp:
    print(name, group)
grp.mean()
grp.min()
%pylab inline
grp.mean().T.plot()
mean_df = grp.mean()[grp.mean().columns[::-1]]
mean_df.T.plot()
import numpy as np
grp.agg([np.sum, np.mean, 'count'])
grp.agg({'2015': lambda x: '$ {:,.2f}'.format(np.sum(x))})
df['2015_avg'] = df.groupby(['partner', 'trade_type'])['2015'].transform(np.mean)
df[['geo', 'trade_type', '2015', '2015_avg']].head()


os.chdir(r'C:\Users\drose\OneDrive - University of New Haven\Data ScientistLearning\CollegeScorecard_Raw_Data\Merged_PP')
import glob
schoolFiles = glob.glob("*.csv")
print(schoolFiles)
oneSchool = pd.read_csv('MERGED1996_97_PP.csv')
df2 = oneSchool.dropna(axis=1, how='all')
df2
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis')
dataDict = pd.read_excel('Copy of CollegeScorecardDataDictionary.xlsx', sheetname='data_dictionary')
varNames = dataDict['developer-friendly name']# 'VARIABLE NAME']
varNames
print(dataDict.columns)
dataDict.drop([['NAME OF DATA ELEMENT'],['dev-category']])
# 'API data type', 'VALUE', 'LABEL', 'SOURCE', 'NOTES']])
df2 = dataDict[dataDict.columns.difference(['B', 'D'])]
len(df2.columns)
len(oneSchool.columns)
df2.count().sort_values(ascending=False)
state = oneSchool.groupby(['STABBR'])
for name, group in state:
    print(name, group)
state['DEBT_MDN'].mean()
df = pd.concat((pd.read_csv(f) for f in schoolFiles))
df.columns
[int(x).split(".")[0] for x in df['AGE_ENTRY']]

.value_counts()
df
"""df = pd.DataFrame()
list_ = []
for file_ in schoolFiles:
    df = pd.read_csv(file_, index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
frame"""
