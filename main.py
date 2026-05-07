import menu
import steam_user
from steam_user import *
import steam_id

# Load menu
menu.start()

# search user
# put results into csv
steam_user.userSearch()
#steam_user.dictToCSV()

# get steam id
steam_id.getSteamID()