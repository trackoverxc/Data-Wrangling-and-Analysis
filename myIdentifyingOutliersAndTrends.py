import pandas as pd
import os
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')
%pylab inline
df = pd.read_csv('eu_trade_sums.csv')

df.head()

df.dtypes
df = df.set_index('geo')

yrs = [str(yr) for yr in range(2002, 2016)]

export_df = df[(df['trade_type'] == 'Export')]
export_df
export_df = df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')]
export_df
export_df = df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')].loc[['EU28', 'UK']]
export_df
export_df = df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')].loc[['EU28', 'UK']][yrs]
export_df
export_df = df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')].loc[['EU28', 'UK']][yrs].T
export_df
export_df = export_df.rename(columns={'EU28': 'EU28_TO_EXT', 'UK': 'UK_TO_EXT'})
export_df = pd.concat([export_df, df[(df['trade_type'] == 'Export') & (df['partner'] == 'EU28')].loc[['EU28', 'UK']][yrs].T], axis=1)
export_df.head()
export_df = export_df.rename(columns={'EU28':'EU28_TO_INT','UK':'UK_TO_INT'})
export_df.head()
export_df.plot()
export_df[['UK_TO_EXT', 'UK_TO_INT']].plot()
df = df[~df.index.isin(['EU28'])]
df.index.unique()
pct_change_df = df.copy()
for yr in yrs:
    pct_change_df[yr] = (df[yr] - df[str(int(yr)-1)]) / df[str(int(yr)-1)]
pct_change_df.head()
