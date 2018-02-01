import pandas as pd
import os

os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')
df = pd.DataFrame()

df
for chunk in pd.read_csv('ext_lt_intratrd.tsv', sep='\t', chunksize=100):
    data_rows = [row for row in chunk.iloc[:,0].str.split(',')]
    print(data_rows)
    data_cols = [col.split('\\')[0] for col in chunk.columns[0].split(",")]
    print(data_cols)
    clean_df = pd.DataFrame(data_rows, columns=data_cols)
    print(clean_df)
    new_df = pd.concat([clean_df, chunk.drop(chunk.columns[0], axis=1)], axis=1)
    print(new_df)
    df = pd.concat([df, new_df])

df
df2 = pd.read_csv('ext_lt_intratrd.tsv', sep='\t')
df2


import glob
import os
import pandas as pd
os.chdir(r'C:\Users\drose\Downloads\TEMPORARY\CollegeScorecard_Raw_Data\Merged_PP')
os.getcwd()
df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('', "*.csv"))))
df['INSTNM'].unique()
df.columns
