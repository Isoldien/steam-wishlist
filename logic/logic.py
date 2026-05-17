import os, json, requests
from steam_web_api import Steam
import time
from concurrent.futures import ThreadPoolExecutor

KEY = os.environ.get("STEAM_WEB_API") # get key from system env, dependant on OS 
steam = Steam(KEY)

# search for a user 
def userSearch() :
    global name, search
    name = str(input('What is your Steam Username? (type -1 to exit)' + '\n'))
    search = steam.users.search_user(name)

# convert dictionary to JSON and extract steamID
def getSteamID() :
    global steamID
    try:
        if os.path.exists("json/search_results.json"):
            os.remove("json/search_results.json")
        if os.path.exists("json"):
            os.rmdir("json")
    except FileNotFoundError as e:
        print(f"Error: File or directory not found - {e}")
    except OSError as e:
        print(f"Error: Could not delete file or directory - {e}")

    # create directory and filename
    os.mkdir("json")
    json_filename = "json/search_results.json"

    # extract data from nested results
    if not isinstance(search, dict) or "player" not in search:
        print("Error: Invalid user search result. User may not exist or API returned unexpected data.")
        return None
    
    steam_data = search["player"]

    # convert dict to json 
    with open(json_filename, 'w') as jsonfile:
        json.dump(steam_data, jsonfile, indent=2)
    
    # extract steamID
    steamID = str(steam_data['steamid'])
    return steamID 

def getWishlist() :
    try:
        wishlist = steam.users.get_profile_wishlist(steamID)
    except KeyError:
        print(f"Error: Cannot access wishlist for this profile. The wishlist may be private or the API key may not have permission.")
        return
    
    if wishlist is None or not wishlist:
        print("Wishlist is empty or not accessible.")
        return
    
    # Extract appids from wishlist
    appids = [game['appid'] for game in wishlist]

    threads = os.cpu_count()
    
    start = time.time()
    # Use ThreadPoolExecutor to fetch game details in parallel
    with ThreadPoolExecutor(max_workers=threads) as executor:
        results = executor.map(getGameDetails, appids)
        # Process results as they complete
        for game_name, price in results:
            if price is None:
                print(f'{game_name}: Price not available')
                print("-----------------------------------")
            else:
                print(f'{game_name}: £{price}')
                print("------------------------------------")
    end = time.time()
    time_taken = end - start
    print(f'Time: {time_taken:.2f} seconds with {threads} threads')

def getGameDetails(appid) :
    try:
        r = requests.get(f'https://store.steampowered.com/api/appdetails?appids={appid}', params={'cc':'GB'})
        data = r.json()
        game_data = data[str(appid)]['data']
        
        game_name = game_data.get('name', 'Name not found!')
        price_overview = game_data.get('price_overview')
        
        if price_overview is None:
            return game_name, None
        
        price = price_overview.get('final', 0) / 100
        return game_name, price
    except Exception as e:
        return f'Error fetching game {appid}', None


def search() :
    while True :
        userSearch()
        if name == "-1" :
            print("Exiting...")
            break
        if getSteamID() is None:
            continue
        getWishlist()
        print('\n')


    


