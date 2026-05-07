import pandas as pd

def getSteamID() :
    global steamID

    df = pd.read_csv('csv/search_results.csv')
    df = df.filter(['steamid'])

    steamID = str(df['steamid'][0])

    return steamID



