import pandas as pd
import os
from alpha_vantage.timeseries import TimeSeries
from pandas_datareader import data, wb
from datetime import datetime
from sqlalchemy import create_engine

os.chdir(r'C:\Users\drose\sqlite_databases')
ts = TimeSeries(key='13NK6LQQTBX98JCO', output_format='pandas', indexing_type='date')
data, meta_data = ts.get_intraday('GOOGL')
data

engine = create_engine('sqlite:///stocks.db')
data.to_sql('GOOG', engine)
