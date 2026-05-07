import menu
import steam_user
from steam_user import *
import steam_id
from steam_id import *

# Load menu
menu.start()

# search user
steam_user.userSearch()
# put results into csv
steam_user.dictToCSV()
# get SteamID
steam_id.getSteamID()
# print SteamID 
print(steam_id.steamID)