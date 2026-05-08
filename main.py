import menu
import steam_user
from steam_user import *
import steam_id
from steam_id import *
# Load menu
menu.start()

steam_user.userSearch()
steam_user.dictToCSV()
steam_id.getSteamID()

print("Your Steam Username is: " + steam_user.name + " and your SteamID is: " + steam_id.steamID + '\n')
