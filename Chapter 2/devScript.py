import os
import csv
import pandas as pd

os.chdir(r'C:\Users\drose\GitHub\Data Wrangling and Analysis with Python - Working Files\Chapter 2\data')

my_reader = csv.DictReader(open('eu_revolving_loans.csv'))

for row in my_reader:
    print(row)

#df = pd.read_csv('eu_revolving_loans.csv')
#df.head()

df = pd.read_csv('eu_revolving_loans.csv', header=[1,2,4], index_col=0)
df.head()
