import pandas as pd

def getSteamID() :
    df = pd.read_csv('csv/search_results.csv')
    df = df.filter(['steamid'])
    print(df)
    print(df.columns)



