import os
from steam_web_api import Steam
import csv
import pandas as pd
import requests
import math

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

# search for a user 
def userSearch() :
    global name, search
    name = str(input('What is your Steam Username? (type -1 to exit)' + '\n'))
    search = steam.users.search_user(name)
    # print(steam.apps.get_app_details(1796470))
    return name, search

# convert dictioniary to CSV
def getSteamID() :
    global steamID
    # @TODO add exception if directory exists 
    # @TODO add exception if file already exists

    # This will do for now i suppose
    if os.path.exists(os.path.join(os.getcwd(), 'csv', 'search_results.csv')) :
        print("Directory and File already exists! Deleting them..." + '\n')
        os.system('rm -rf csv')
    # create directory and filename
    os.mkdir("csv")
    csv_filename = "csv/search_results.csv"

    # extract data from nested results
    if not isinstance(search, dict) or "player" not in search:
        print("Error: Invalid user search result. User may not exist or API returned unexpected data.")
        return None
    
    steam_data = search["player"]
    fieldnames = list(steam_data.keys())

    # convert dict to csv 
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(steam_data)
    
    # clean CSV
    df = pd.read_csv('csv/search_results.csv')
    df = df.filter(['steamid'])
    steamID = str(df['steamid'][0])
    return steamID 

def getWishlist() :
    wishlist = steam.users.get_profile_wishlist(steamID)
    total_price = 0
    # iterate through wishlist
    for games in wishlist :
        appid = games['appid']

        #@TODO have a user selectable country code so users can choose where they live

        r = requests.get(f'https://store.steampowered.com/api/appdetails?appids={appid}', params={'cc':'GB'})

        data = r.json() 
        game_data = data[str(appid)]['data']
        names = game_data.get('name', 'Name not found!')
        price_overview = game_data.get('price_overview')

        if price_overview is None:
            print(f'{names}: Price not available')
            continue

        price = price_overview.get('final', 0) / 100
        total_price = price + total_price
        print(f'£{total_price:.2f}')

def search() :
    while True :
        userSearch()
        if name == "-1" :
            print("Exiting...")
            break
        if getSteamID() is None:
            continue 
        print(steamID)
        getWishlist()
        print('\n')


    


