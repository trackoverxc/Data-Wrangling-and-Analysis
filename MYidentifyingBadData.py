import pandas as pd
import os
import numpy as np
from datetime import datetime
os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 4')
weather = pd.read_csv('berlin_weather_oldest.csv')

weather.head()

weather = weather.applymap(lambda x: np.nan if x == -9999 else x)

weather.head()

weather['DATE'] = weather['DATE'].map(lambda x: datetime.strptime(str(x), '%Y%m%d').date())
weather.head()
weather.notnull().head()
weather.dropna()
weather.dropna(axis=1, how='all')
weather.shape
weather.dropna(axis=1, thresh=1000)
weather['DATE'].dtype
weather = weather.set_index(pd.DatetimeIndex(weather['DATE'])) # Change the idnex to be the date column in datetime format
weather.sort_values('DATE').head()
weather.index.duplicated()
weather['STATION_NAME'].value_counts()
weather.index.drop_duplicates().sort_values()
weather.groupby('STATION_NAME').resample('D').mean().head()
for name, group in weather.groupby('STATION_NAME'):
    print(name, group)
