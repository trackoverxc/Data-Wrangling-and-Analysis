import pandas as pd
import numpy as np
import os

os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 5')
df = pd.read_csv('berlin_weather_oldest.csv')
df.shape

df.head()
%timeit df.applymap(lambda x: np.nan if x == -9999 else x)

def return_row(row):
    return [x if x != -9999 else np.nan for x in row]

%timeit df.apply(return_row)
def iter_columns(df):
    for col in df.columns:
        df[col] = df[col].map(lambda x: x if x != -9999 else np.nan)
        return df

new_df = df.copy()

%timeit iter_columns(new_df)

%prun df.applymap(lambda x: np.nan if x == -9999 else x)

%prun

%load_ext memit

%memit df.applymap(lambda x: np.nan if x == -9999 else x)
