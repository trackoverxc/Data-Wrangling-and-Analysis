    %pylab inline
    import pandas as pd
    import os
    import numpy as np
    os.chdir(r'C:\Users\drose\Documents\GitHub\Data-Wrangling-and-Analysis\Chapter 3')
    df = pd.read_csv('eu_trade_sums.csv')
    df.head()
    df = df.set_index('geo')
    df.head()
    np.unique(df.index)
    df = df.drop('EU28')
    df
    np.unique(df.index)
    means = df.groupby(['trade_type', 'partner'])
    for name, group in means:
        print(name, group)
    means = df.groupby(['trade_type', 'partner']).transform(np.mean)
    for name, group in means:
    std_dev = df.groupby(['trade_type', 'partner']).transform(np.std)
    std_df = df.copy()
    for col in df.columns:
        try:
            std_df[col] = (df[col] - means[col]) / std_dev[col]
        except Exception as e:
            print(e)
    std_df.head()
    yrs = [str(yr) for yr in range(2002, 2016)]
    yrs
    df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')][yrs].T.plot(legend=False)
    df[(df['trade_type'] == 'Export') & (df['partner'] == 'EXT_EU28')].loc[['DE', 'UK', 'FR', 'IT', 'NL', 'PL']][yrs].T.plot()
std_df[(std_df['trade_type'] == 'Export') & (std_df['partner'] == 'EXT_EU28')][yrs].T.plot(legend=False)
std_df[(std_df['trade_type'] == 'Export') & (std_df['partner'] == 'EXT_EU28')].loc[['DE', 'UK', 'FR', 'IT', 'NL', 'PL']][yrs].T.plot()
