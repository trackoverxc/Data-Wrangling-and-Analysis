import pandas as pd
import os
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')

df = pd.read_csv('eu_revolving_loans.csv', header=[1,2,3], skiprows=1, index_col=0, na_values=['-'])
df.head()
df.columns = df.columns.droplevel(1)
df.head()
df.describe()
df.corr()
df_corr = df.corr()
df_corr[(df_corr.abs() > .5) & (df_corr < 1)].dropna(thresh=4)
df.cov()
df.cov().min()
df.cov().max()
%pylab inline
df[['Latvia', 'Estonia', 'Greece (GR)', 'Ireland']].plot()
df.index
import datetime
df.index.map(lambda x: datetime.datetime.strptime(x, '%Y%b').date())
df.index = df.index.map(lambda x: datetime.datetime.strptime(x, '%Y%b').date())
df.index
df[['Latvia', 'Estonia', 'Greece (GR)', 'Ireland']].plot()
df['Latvia'].loc[df.index > datetime.date(2013, 9, 1)]
