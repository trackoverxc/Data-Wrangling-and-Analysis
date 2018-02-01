import pandas as pd
import os
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')
os.getcwd()
eu_trade = pd.read_csv('ext_lt_intratrd.tsv',sep='\t')
eu_trade.dtypes
eu_trade.2013
eu_trade['my_col'] = 1
new_columns = dict([(col, col.strip()) for col in eu_trade.columns])
eu_trade = eu_trade.rename(columns=new_columns)
eu_trade.head()
eu_trade.ix[3]
eu_trade.iloc[:,0]
eu_trade['geo'] = eu_trade.iloc[:,0].map(lambda row: row.split(',')[-1])
eu_trade['geo'].head()
eu_trade['mycol'] = eu_trade.iloc[:,1].map(lambda row: row.split('.')[-1])
eu_trade.head(10)
eu_trade.columns
eu_trade[eu_trade['geo'].isin(['UK', 'DE'])]
eu_trade[(eu_trade['2014'] > eu_trade['2013']) & (eu_trade['2013'] > eu_trade['2012'])]
eu_trade['2013_increase'] = eu_trade['2013'] < eu_trade['2012']
eu_trade['2013_increase'].head()
eu_trade = eu_trade.set_index('geo')
eu_trade.head()
eu_trade.loc['DE']
eu_trade.iloc[:100]
